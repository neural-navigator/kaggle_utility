import os
import typer


class KaggleUser:
    """
    It's a singleton object to set the kaggle username, apikey and
    competition
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def set_kaggle(kaggle_username: str, kaggle_api_token: str, competition_name: str):
    kaggle_user = KaggleUser()
    kaggle_user.username = kaggle_username
    kaggle_user.api_key = kaggle_api_token
    kaggle_user.competition = competition_name

    os.environ['KAGGLE_USERNAME'] = kaggle_user.username
    os.environ['KAGGLE_KEY'] = kaggle_user.api_key

