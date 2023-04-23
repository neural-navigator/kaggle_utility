import os
import json
import pickle
from init_kaggle import KaggleUser

CACHE_DIR = '.cache/'

MAIN_FILE_TEXT = """
# Hello World

def main():
    ''' print hello world '''
    print("Hello World!")

"""

kaggle_user = KaggleUser()
kaggle_user.DIRECTORIES = ['dataset', 'src', 'docs', 'configs', 'notebooks', 'tests', 'models',
                           'dataset/raw', 'dataset/interim', 'dataset/processed', 'dataset/submissions']
kaggle_user.FILES = {'src/__init__.py': "", 'src/main.py': MAIN_FILE_TEXT}

with open('.cache/conf.pkl', 'rb') as f:
    # deserialize the object from the file
    conf_dict = pickle.load(f)


os.environ['KAGGLE_USERNAME'] = conf_dict['username']
os.environ['KAGGLE_KEY'] = conf_dict['key']
