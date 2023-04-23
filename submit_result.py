import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi


def submit_result(competition_name, file_path, message):
    """
    Submit a result to a Kaggle competition using the Kaggle API.

    Args:
        competition_name (str): The name of the Kaggle competition to submit to.
        file_path (str): The path to the file containing the results to submit.
        message (str): A message to include with the submission.

    Returns:
        None
    """
    # Authenticate with the Kaggle API
    try:
        kaggle_api = KaggleApi()
        kaggle_api.authenticate()

        # Initialize a Kaggle competition client
        kaggle_api.competition_submit(file_path, message, competition_name, quiet=False)
        print(f"Result submitted successfully to competition '{competition_name}'!")
    except Exception as e:
        print(e)
