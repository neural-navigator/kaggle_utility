import argparse


def main():
    parser = argparse.ArgumentParser(description="Kaggle Command Line Interface")
    # Create subparsers for each function
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for initializing a kaggleUtil object
    init_parser = subparsers.add_parser("set_env", help="setup the environment for KaggleUtil")
    init_parser.add_argument("conf_json", type=str, help="path of the configuration json with username and api key "
                                                         "downloaded from kaggle")
    init_parser.add_argument("competition_name", type=str, help="name of the competition")

    # Subparser for initialize the directories
    pkg_parser = subparsers.add_parser("make_dirs", help="create required directories for datascience project")
    pkg_parser.add_argument("target_dir", type=str, default='.', help='directory in which the packaging will be done')

    # download the dataset
    download_parser = subparsers.add_parser("download_data", help="download the dataset")
    download_parser.add_argument("competition_name", type=str, help="name of the competition")
    download_parser.add_argument("download_path", type=str, help="path where the data will be stored")

    # Subparser for pushing a notebook
    push_parser = subparsers.add_parser("push_notebook", help="Push a Jupyter notebook to Kaggle")
    push_parser.add_argument("notebook_path", type=str, help="Path to the Jupyter notebook")
    push_parser.add_argument("title", type=str, default='', help="title of the notebook")
    push_parser.add_argument("competition_name", type=str, help="name of the competition")
    push_parser.add_argument("kernel_type", type=str, default='notebook', help='description of the notebook')

    # Subparser for submitting a result
    submit_parser = subparsers.add_parser("submit_prediction", help="Submit a Kaggle competition result")
    submit_parser.add_argument("prediction_file", type=str, help="prediction file")

    # Subparser for viewing the leaderboard
    leaderboard_parser = subparsers.add_parser("leaderboard", help="View the leaderboard for a Kaggle competition")
    leaderboard_parser.add_argument("competition_name", type=str, help="competition name")

    args = parser.parse_args()

    if args.command == "set_env":
        from init_kaggle import KaggleUser, set_kaggle
        set_kaggle(args.conf_json, args.competition_name)
    elif args.command == "make_dirs":
        from package_initializer import init_package
        init_package(args.target_dir)
    elif args.command == "download_data":
        from download_dataset import download_data
        download_data(args.competition_name, args.download_path)
    elif args.command == "push_notebook":
        from publish_notebook import publish_notebook
        publish_notebook(args.notebook_path, args.title, args.competition_name, args.kernel_type)
    elif args.command == "submit_prediction":
        from submit_result import submit_result
        submit_result(args.competition_name, args.prediciton_file)
    elif args.command == "leaderboard":
        from view_leaderboard import get_leaderboard
        get_leaderboard(args.competition_name)

