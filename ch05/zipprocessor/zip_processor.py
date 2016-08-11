import os
import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    """
    Abstract base class for a generic ZIP file processor that implements the
    following process:
    1. Unzip files from the given ZIP file.
    2. Process the files (user defined function).
    3. Zip the processes files overwriting the original ZIP file.
    """

    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_zip(self):
        """Implement the processing steps."""
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """Unzip the files into a temporary directory."""
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """Zip the files into the original zip file."""
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
