import shutil
import os.path


def augmented_move(target_folder, *filenames, verbose=False, **specific):
    """
    Process an arbitrary list of files with the default behaviour being to move
    all remaining non-keyword argument files into that folder.

    NOTE: This function only prints the operation selected. It does not actually
    perform the operation on the files.
    :param target_folder: target folder for the operation (default is move).
    :param filenames: variables length argument of filenames to operate on.
    :param verbose: flag for verbose output; default=False.
    :param specific: variable length dictionary of keywords specifying the
    operation to perform on the specified file. Supported values include:
        'ignore': to ignore and exclude the file from the operation.
        'copy': to copy the file to the target folder.
    """

    def print_verbose(message, filename):
        """Print the message only if verbose is enabled."""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == 'ignore':
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == 'copy':
                print_verbose("copying {0}", filename)
            # shutil.copyfile(filename, target_path)
        else:
            print_verbose("Moving {0}", filename)
            # shutil.move(filename, target_path)
