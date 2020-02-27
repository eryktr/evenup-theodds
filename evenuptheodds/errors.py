class NoConfigFileError(Exception):
    def __init__(self):
        super().__init__("No players.cfg file found. It should reside in the root of the project.")