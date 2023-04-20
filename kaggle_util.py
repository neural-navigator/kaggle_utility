import argparse

from kaggle_utility.init_kaggle import KaggleUser, set_kaggle
from kaggle_utility.download_dataset import download_data
from kaggle_utility.package_initializer import init_package
from kaggle_utility.publish_notebook import publish_notebook_to_kaggle
from kaggle_utility.submit_result import submit_result
from kaggle_utility.view_leaderboard import view_leaderboard


def main():
    parser = argparse.ArgumentParser(description="Kaggle Command Line Interface")
    # Create subparsers for each function
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for initializing a kaggleUtil object
    init_parser = subparsers.add_parser("set_env", help="setup the environment for KaggleUtil")
    init_parser.add_argument("kaggle_username", type=str, help="Kaggle Username")
    init_parser.add_argument("kaggle_api_token", type=str, help="kaggle_api_token")
    init_parser.add_argument("competition_name", type=str, help="name of the competition")

    # Subparser for initialize the directories
    pkg_parser = subparsers.add_parser("make_dirs", help="create required directories for datascience project")
    pkg_parser.add_argument("target_dir", type=str, default='.', help='directory in which the packaging will be done')

    # download the dataset
    download_parser = subparsers.add_parser("download_data", help="download the dataset")
    download_parser.add_argument("download_path", type=str, help="path where the data will be stored")

    # Subparser for pushing a notebook
    push_parser = subparsers.add_parser("push_notebook", help="Push a Jupyter notebook to Kaggle")
    push_parser.add_argument("notebook_path", type=str, help="Path to the Jupyter notebook")
    push_parser.add_argument("title", type=str, default='', help="title of the notebook")
    push_parser.add_argument("desc", type=str, default='', help='description of the notebook')

    # Subparser for submitting a result
    submit_parser = subparsers.add_parser("submit_prediction", help="Submit a Kaggle competition result")
    submit_parser.add_argument("prediction_file", type=str, help="prediction file")
    submit_parser.add_argument("message", type=str, help='message on submission')

    # Subparser for viewing the leaderboard
    leaderboard_parser = subparsers.add_parser("leaderboard", help="View the leaderboard for a Kaggle competition")

    args = parser.parse_args()

    if args.command == "set_env":
        set_kaggle(args.kaggle_username, args.kaggle_api_token, args.competition_name)
    elif args.command == "make_dirs":
        init_package(args.target_dir)
    elif args.command == "download_data":
        download_data(args.competition_name, args.download_path)
    elif args.command == "push_notebook":
        publish_notebook_to_kaggle(args.notebook_path, args.title, args.desc, args.competition_name)
    elif args.command == "submit_prediction":
        submit_result(args.competition_name, args.prediciton_file, args.message)
    elif args.command == "leaderboard":
        view_leaderboard(args.competition)
