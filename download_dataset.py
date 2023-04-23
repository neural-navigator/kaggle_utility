import os
import subprocess
import constants

import kaggle
import zipfile


def download_data(comp_name: str, target_dir: str):
    """
    Downloads a dataset from Kaggle using the Kaggle API.

    Args:
        comp_name (str): The name of the Kaggle dataset to download.
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
        download_cmd = f"""
        kaggle competitions download -c {comp_name} --path {target_dir}
        """
        process = subprocess.Popen(download_cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        zip_files = [i for i in os.listdir(target_dir) if i.endswith('.zip')]
        for file in zip_files:
            file_path = os.path.join(target_dir, file)
            if file.endswith(".zip"):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(target_dir)
            os.remove(file_path)

    except Exception as e:
        print(f"Error downloading dataset '{comp_name}': {e}")
        return

    # Print a message confirming the download
    print(f"Dataset '{comp_name}' downloaded successfully to '{target_dir}'.")
