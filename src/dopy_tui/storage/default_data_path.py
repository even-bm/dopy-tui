import os
from pathlib import Path
# This function returns the default directory for user-data
def default_data_path():
    return Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share") / "dopy-tui"
