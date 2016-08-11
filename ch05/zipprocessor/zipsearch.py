import sys

from zip_processor import ZipProcessor


class ZipReplace(ZipProcessor):
    """
    Class used to perform a find and replace action for text files stored in a
    compressed ZIP file. This class is responsible for performing the find and
    replace action.
    """

    def __init__(self, filename, search_string, replace_string):
        """
        The class is initialised with the ZIP filename and search and replace
        strings.
        :param filename: ZIP filename
        :param search_string: String to search for in the files.
        :param replace_string: Replacement string.
        """
        super(ZipReplace, self).__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """
        Find and replace the strings in all of the files in the temporary
        directory.
        """
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()
