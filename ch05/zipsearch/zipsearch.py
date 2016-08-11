import sys
import shutil
import zipfile
from pathlib import Path


class ZipReplace:
    """
    Class used to perform a find and replace action for text files stored in a
    compressed ZIP file. This class is responsible for:
        1. Unzipping the compressed file.
        2. Performing the find and replace action.
        3. Zipping up the new files.
    """

    def __init__(self, filename, search_string, replace_string):
        """
        The class is initialised with the ZIP filename and search and replace
        strings.
        :param filename: ZIP filename
        :param search_string: String to search for in the files.
        :param replace_string: Replacement string.
        """
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        # A temporary directory is used to store the unzipped files during
        # processing for search & replace.
        self.temp_directory = Path("unzipped-{}".format(filename))

    def zip_find_replace(self):
        """
        Top-level method used to perform all of the steps in the process by
        delegating to the specialist methods.
        """
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        """Unzip the ZIP file into the temporary directory."""
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def find_replace(self):
        """Find and replace the strings in all of the files in the directory."""
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        """Zip (compress) the files in the directory."""
        with zipfile.ZipFile(self.filename, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()
