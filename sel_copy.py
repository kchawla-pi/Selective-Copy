import os, shutil


def selective_copy(folder, extension, copy_folder=''):
    folder = os.path.abspath(folder)
    if extension.startswith('.'):
        copy_folder = extension[1:] + '_folder'
    else:
        copy_folder = extension + '_folder'
    if not os.path.exists(copy_folder):
        os.makedirs(copy_folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                shutil.copy(filename, copy_folder)
    print('Done.')


selective_copy('.', '.txt')
