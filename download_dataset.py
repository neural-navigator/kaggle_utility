import os

import kaggle
import kaggle.api
import typer


def download_data(dataset_name: str, target_dir: str):
    """
    Downloads a dataset from Kaggle using the Kaggle API.

    Args:
        dataset_name (str): The name of the Kaggle dataset to download.
        target_dir (str): The directory to save the dataset to.

    Returns:
        None
    """
    try:
        # Set up the Kaggle API credentials
        kaggle.api.authenticate()
    except Exception as e:
        print(f"Error authenticating with Kaggle API: {e}")
        return

    try:
        # Download the dataset from Kaggle
        kaggle.api.dataset_download_files(dataset_name, path=target_dir, unzip=True)
    except Exception as e:
        print(f"Error downloading dataset '{dataset_name}': {e}")
        return

    # Print a message confirming the download
    print(f"Dataset '{dataset_name}' downloaded successfully to '{target_dir}'.")

