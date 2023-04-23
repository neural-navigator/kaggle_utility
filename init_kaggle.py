import json
import os
import pickle


class KaggleUser:
    """
    It's a singleton object to set the kaggle username, apikey and
    competition
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def set_kaggle(conf_json: str, competition_name: str):
    os.mkdir('.cache')
    kaggle_user = KaggleUser()
    kaggle_user.competition = competition_name

    with open(os.path.abspath(conf_json), 'r') as file:
        data = json.load(file)

    kaggle_user.username = data['username']
    kaggle_user.api_key = data['key']
    kaggle_user.conf_json = conf_json

    # open the file for reading
    with open('.cache/conf.pkl', 'wb') as f:
        # deserialize the object from the file
        pickle.dump(data, f)
