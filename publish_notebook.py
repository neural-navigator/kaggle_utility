import constants

import kaggle


def publish_notebook_to_kaggle(notebook_path: str, title: str, description: str, dataset: str):
    """
    Publishes a Jupyter notebook to Kaggle using the Kaggle API.

    Args:
        notebook_path (str): The file path of the Jupyter notebook to publish.
        title (str): The title of the notebook.
        description (str): A description of the notebook.
        dataset (str): The name of the Kaggle dataset to associate the notebook with.

    Returns:
        None
    """
    try:
        # Authenticate with the Kaggle API
        kaggle.api.authenticate()

        # Create a new Kaggle notebook
        notebook_id = kaggle.api.kernels_init_new(title=title, kernel_type="notebook", language="python")

        # Read the notebook file
        with open(notebook_path, "r") as f:
            notebook_contents = f.read()

        # Update the notebook with the contents of the Jupyter notebook file
        kaggle.api.kernels_push(notebook_id, notebook_contents)

        # Update the notebook metadata with a description and the associated dataset
        metadata = {
            "id": notebook_id,
            "title": title,
            "code_file": "",
            "language": "python",
            "kernel_type": "notebook",
            "is_private": False,
            "enable_gpu": False,
            "enable_internet": True,
            "dataset_sources": [dataset],
            "kernel_sources": [],
            "competition_sources": [],
            "collaborator_usernames": [],
            "output_files": []
        }
        kaggle.api.kernels_push_metadata(notebook_id, metadata)

        # Publish the notebook
        kaggle.api.kernels_push(notebook_id, notebook_contents, message=description, quiet=False)

        # Print a message confirming that the notebook was published successfully
        print(f"Notebook '{title}' published successfully to Kaggle.")
    except Exception as e:
        print(f"Error: {e}")
