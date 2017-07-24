import os, shutil


def selective_copy(folder, extension, copy_folder=None):
    """."""
    folder = os.path.abspath(folder)  # Get the absolute path

    #  Create a new folder if the copy folder does not exists
    if copy_folder:
        if not os.path.exists(os.path.join(folder, copy_folder)):
            os.makedirs(os.path.join(folder, copy_folder))
    else:
        if extension.startswith('.'):
            copy_folder = extension[1:] + '_folder'
        else:
            copy_folder = extension + '_folder'
        try:
            os.makedirs(os.path.join(folder, copy_folder))
        except FileExistsError:
            print('A folder called "{}" will be used.'.format(copy_folder))

    #  Walk through the entire folder and copy the corresponding files
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                print('Copying {} to {}...'.format(filename, copy_folder))
                shutil.copy(os.path.join(foldername, filename), copy_folder)
    print('Done.')


selective_copy('.', '.txt', 'my_file')
