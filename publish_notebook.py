import json

import constants

import kaggle

import kaggle

import kaggle


def publish_notebook(notebook_path, title, competition, kernel_type):
    kaggle.api.authenticate()
    competition_id = kaggle.api.competitions_list(search=competition)[0].id
    print(competition_id)
    kernel_metadata = {
        "id": "username/" + title.replace(" ", "-"),
        "title": title,
        "code_file": notebook_path,
        "language": "python",
        "kernel_type": kernel_type,
        "is_private": True,
        "enable_gpu": True,
        "enable_internet": True,
        "competition_sources": [competition_id]
    }
    with open(".cache/kernel-metadata.json", "w") as file:
        json.dump(kernel_metadata, file)
    kaggle.api.kernels_push(".cache")


if __name__ == "__main__":
    publish_notebook("/home/warmachine/Workspace/learning/Kaggle/kaggle_utility/new.ipynb",
                     "testnotebook",
                     "cafa-5-protein-function-prediction",
                     "notebook")