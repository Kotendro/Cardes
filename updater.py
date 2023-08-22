import logging
import os
import pathlib
import shutil
import subprocess
import sys
import tarfile
from ctypes import windll
from typing import List, Union, Optional

from tuf.api.metadata import Metadata
from tuf.ngclient import Updater
from tuf.api.exceptions import RepositoryError, DownloadError

from settings import LOG_FILE, WIN_BATCH_TEMPLATE, UPDATE_CACHE_DIR, METADATA_DIR, TARGET_DIR, EXTRACT_DIR, \
    METADATA_BASE_URL, TARGET_BASE_URL, CURRENT_VERSION, INSTALL_DIR

logger = logging.getLogger()


def install(
        purge_dst_dir: bool,
        exclude_from_purge: List[Union[pathlib.Path, str]]):
    purge_options = []
    if purge_dst_dir:
        purge_options = ['/purge']
        if exclude_from_purge:
            purge_options.append('/xf')
            purge_options.extend(exclude_from_purge)
    options_str = ' '.join(purge_options)

    script_content = WIN_BATCH_TEMPLATE.format(
        src_dir=EXTRACT_DIR,
        dst_dir=INSTALL_DIR,
        purge=options_str,
        log_file_path=LOG_FILE,
        exe=INSTALL_DIR + r'\Cardes.exe'
    )
    with open(file=UPDATE_CACHE_DIR + "install.bat", mode='w') as bat_file:
        bat_file.write(script_content)
    script_path = pathlib.Path(bat_file.name).resolve()

    # Run as admin
    windll.shell32.ShellExecuteW(
        None,  # handle to parent window
        'runas',  # verb
        'cmd.exe',  # file on which verb acts
        ' '.join(['/c', str(script_path)]),  # parameters
        None,  # working directory (default is cwd)
        1,  # show window normally
    )
    # Swap to this if administrative privileges are not required

    # subprocess.Popen(
    #     [script_path], creationflags=subprocess.CREATE_NEW_CONSOLE
    # )
    sys.exit(0)


def update():
    for path in [METADATA_DIR, TARGET_DIR, EXTRACT_DIR]:
        pathlib.Path(path).mkdir(exist_ok=True, parents=True)
    if not os.path.isfile(METADATA_DIR + r"\root.json"):
        shutil.copy(INSTALL_DIR + r"\root.json", METADATA_DIR)
        logger.info("Trusted root not found. Copied from install dir.")
    try:
        logger.info("Connecting to the repository...")
        client = Updater(
            metadata_dir=METADATA_DIR,
            metadata_base_url=METADATA_BASE_URL,
            target_dir=TARGET_DIR,
            target_base_url=TARGET_BASE_URL,
        )
    except RepositoryError:
        logger.critical("Error: local root.json is invalid.")
        sys.exit(1)
    except OSError as e:
        logger.critical(e)
        sys.exit(1)
    try:
        logger.info("Downloading metadata...")
        client.refresh()
        logger.info("Metadata verified.")
    except RepositoryError:
        logger.critical("Error: could not verify metadata.")
        sys.exit(1)
    targets = Metadata.from_file(METADATA_DIR + r"\targets.json")

    latest_archive = max(targets.signed.targets.keys(), default=".tar")
    logger.debug("Latest archive file found: %s", latest_archive)
    if latest_archive[:-4] > CURRENT_VERSION:
        try:
            logger.info("New update found")

            info = client.get_targetinfo(latest_archive)
            archive = client.download_target(info)
        except RepositoryError:
            logger.critical("Failed to validate target file. Update aborted")
            sys.exit(1)
        except DownloadError:
            logger.critical("Failed to download target file. Update aborted")
            sys.exit(1)
        clear_extract_location()
        tarfile.open(archive).extractall(EXTRACT_DIR)
        install(False, [])
        clear_extract_location()


def clear_extract_location():
    for file in os.listdir(EXTRACT_DIR):
        os.remove(EXTRACT_DIR + "\\" + file)
