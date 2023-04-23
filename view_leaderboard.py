import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi


def get_leaderboard(competition_name):
    """
    Get the leaderboard data for a Kaggle competition.

    Args:
        competition_name (str): The name of the Kaggle competition.

    Returns:
        A list of dictionaries containing the leaderboard data.
    """
    # Authenticate with the Kaggle API
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()
    import csv
    # Get the leaderboard data as a CSV file
    kaggle_api.competition_leaderboard_cli(competition_name, download=False, view=True)
