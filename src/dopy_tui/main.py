from dopy_tui.ui.cli import cli
from dopy_tui.storage.csv_handler import Handler
from dopy_tui.storage.default_data_path import default_data_path
def main():
    handler = Handler(default_data_path())
    cli(handler)
