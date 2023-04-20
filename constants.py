import os
from decouple import config

KAGGLE_USERNAME = config("KAGGLE_USERNAME")
KAGGLE_API_KEY = config("KAGGLE_API_KEY")

os.environ['KAGGLE_USERNAME'] = KAGGLE_USERNAME
os.environ['KAGGLE_KEY'] = KAGGLE_API_KEY
