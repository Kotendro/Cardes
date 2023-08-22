import os

CURRENT_VERSION = "0.1.3"

INSTALL_DIR = os.getenv("PROGRAMFILES") + r"\Cardes"
UPDATE_CACHE_DIR = os.getenv("LOCALAPPDATA") + r"\Cardes\update_cache"
METADATA_DIR = UPDATE_CACHE_DIR + r"\metadata"
TARGET_DIR = UPDATE_CACHE_DIR + r"\targets"
EXTRACT_DIR = UPDATE_CACHE_DIR + r"\extract"

METADATA_BASE_URL = "http://repo.aiop.su:6006/metadata"
TARGET_BASE_URL = "http://repo.aiop.su:6006/targets"

WIN_BATCH_TEMPLATE = """@echo off
call :log > "{log_file_path}" 2>&1
:log
echo Moving app files...
robocopy "{src_dir}" "{dst_dir}" /e /move /v /w:2 {purge}
echo Done.
start "" "{exe}"
(goto) 2>nul & del "%~f0"
"""
LOG_FILE = INSTALL_DIR + "\\update.log"
