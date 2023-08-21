import os

CURRENT_VERSION = "0.1.1"

INSTALL_DIR = os.getenv("LOCALAPPDATA") + r"\Programs\Cardes"
UPDATE_CACHE_DIR = os.getenv("LOCALAPPDATA") + r"\Cardes\update_cache"
METADATA_DIR = UPDATE_CACHE_DIR + r"\metadata"
TARGET_DIR = UPDATE_CACHE_DIR + r"\targets"
EXTRACT_DIR = UPDATE_CACHE_DIR + r"\extract"

METADATA_BASE_URL = "http://repo.aiop.su:6006/metadata"
TARGET_BASE_URL = "http://repo.aiop.su:6006/targets"

WIN_BATCH_TEMPLATE = """@echo off
{log_lines}
echo Moving app files...
robocopy "{src_dir}" "{dst_dir}" {robocopy_options}
echo Done.
start "" "{exe}"
(goto) 2>nul & del "%~f0"
"""
LOG_FILE = "update.log"