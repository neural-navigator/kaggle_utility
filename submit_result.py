import kaggle


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
    kaggle.api.authenticate()

    # Initialize a Kaggle competition client
    competition = kaggle.api.competition_submissions(competition_name)

    # Submit the results file to the Kaggle competition
    competition.submit(file_path, message)

    print(f"Result submitted successfully to competition '{competition_name}'!")
