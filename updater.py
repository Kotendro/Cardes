import os
import pathlib
import shutil
import subprocess
import sys
import tarfile
from typing import List, Union, Optional

from tuf.api.metadata import Metadata
from tuf.ngclient import Updater

from settings import LOG_FILE, WIN_BATCH_TEMPLATE, UPDATE_CACHE_DIR, METADATA_DIR, TARGET_DIR, EXTRACT_DIR, \
    METADATA_BASE_URL, TARGET_BASE_URL, CURRENT_VERSION, INSTALL_DIR


def install(
        src_dir: str,
        dst_dir: str,
        purge_dst_dir: bool,
        exclude_from_purge: List[Union[pathlib.Path, str]],
        batch_template_extra_kwargs: Optional[dict] = None,
):
    if batch_template_extra_kwargs is None:
        batch_template_extra_kwargs = dict()
    # collect robocopy options
    robocopy_options = ['/e', '/move', '/v', '/w:2']
    if purge_dst_dir:
        robocopy_options.append('/purge')
        if exclude_from_purge:
            robocopy_options.append('/xf')
            robocopy_options.extend(exclude_from_purge)
    options_str = ' '.join(robocopy_options)
    # handle batch file output logging
    log_lines = """
call :log > "{log_file_path}" 2>&1
:log
""".format(log_file_path=LOG_FILE)
    # write temporary batch file (NOTE: The file is placed in the system
    # default temporary dir, but the file is not removed automatically. So,
    # either the batch file should self-delete when done, or it should be
    # deleted by some other means, because windows does not clean the temp
    # dir automatically.)
    script_content = WIN_BATCH_TEMPLATE.format(
        src_dir=src_dir,
        dst_dir=dst_dir,
        robocopy_options=options_str,
        log_lines=log_lines,
        **batch_template_extra_kwargs,
    )
    with open(file=UPDATE_CACHE_DIR + "install.bat", mode='w') as bat_file:
        bat_file.write(script_content)
    script_path = pathlib.Path(bat_file.name).resolve()
    # start the script in a separate process, non-blocking
    # we use Popen() instead of run(), because the latter blocks execution
    subprocess.Popen(
        [script_path], creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    # exit current process
    sys.exit(0)


def update():
    for path in [METADATA_DIR, TARGET_DIR, EXTRACT_DIR]:
        pathlib.Path(path).mkdir(exist_ok=True, parents=True)
    if not os.path.isfile(METADATA_DIR + r"\root.json"):
        shutil.copy("root.json", METADATA_DIR + r"\root.json")
    client = Updater(
        metadata_dir=METADATA_DIR,
        metadata_base_url=METADATA_BASE_URL,
        target_dir=TARGET_DIR,
        target_base_url=TARGET_BASE_URL,
    )
    client.refresh()
    targets = Metadata.from_file(METADATA_DIR + r"\targets.json")
    latest_archive = max(targets.signed.targets.keys())
    if latest_archive[:-4] > CURRENT_VERSION:
        info = client.get_targetinfo(latest_archive)
        archive = client.download_target(info)
        clear_extract_location()
        tarfile.open(archive).extractall(EXTRACT_DIR)
        install(EXTRACT_DIR, INSTALL_DIR, False, [], {'exe': (INSTALL_DIR + '\\Cardes.exe')})


def clear_extract_location():
    for file in os.listdir(EXTRACT_DIR):
        os.remove(EXTRACT_DIR + "\\" + file)
