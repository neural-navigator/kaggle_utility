import os
import sys

import constants
import init_kaggle


def init_package(target_directory: str = '.'):
    """
    create directories for a kaggle project
    :param target_directory:
    :return:
    """

    # creating directories
    try:
        abs_parent_path = os.path.abspath(target_directory)
        for directory in constants.DIRECTORIES:
            dir_path = os.path.join(abs_parent_path, directory)
            os.mkdir(dir_path)
    except Exception as e:
        print("path error")

    # writing files
    try:
        abs_parent_path = os.path.abspath(target_directory)
        for filename, text in constants.FILES.items():
            with open(os.path.join(abs_parent_path, filename), 'w') as file:
                file.write(text)
    except Exception as e:
        print("file writing error")

    try:
        abs_parent_path = os.path.abspath(target_directory)
        kaggle_user = init_kaggle.KaggleUser()
        kaggle_user.raw_datapath = os.path.join(abs_parent_path, 'dataset/raw')
        kaggle_user.submission_datapath = os.path.join(abs_parent_path, 'dataset/submissions')
        kaggle_user.notebook_datapath = os.path.join(abs_parent_path, 'notebooks')
    except Exception as e:
        print("error occurred!")
