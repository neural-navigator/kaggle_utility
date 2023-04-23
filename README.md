# kaggle_util

`kaggle_util` is a Python package that provides a set of utility functions for working with Kaggle datasets and competitions.

## Installation

To install `kaggle_util`, run the following command:

```
pip install kaggle_util
```

## Usage

### Setting Up

Before you can use the Kaggle API, you need to setup. To setup, you need to create an API token on the Kaggle website. 

Once you have downloaded the token, you can authenticate by running the following command in your teminal

```
kaggle_util set_env <path-to-kaggle.json> <competition_name>

Like:

kaggle_util set_env "/home/<username>/Downloads/kaggle.json" "cafa-5-protein-function-prediction"
```

### Creating required directories for a data science project

You can create a good directory structure by using kaggle_util's `make_dirs` utility

```
 kaggle_util make_dirs <target_dir>
```
It will create following directory structure

```
├── configs
├── dataset
│   ├── interim
│   ├── processed
│   ├── raw
│   │   ├── cafa-5-protein-function-prediction.zip
│   │   ├── IA.txt
│   │   ├── submission.tsv
│   │   ├── Test (Targets)
│   │   │   ├── testsuperset.fasta
│   │   │   └── testsuperset-taxon-list.tsv
│   │   └── Train
│   │       ├── go-basic.obo
│   │       ├── train_sequences.fasta
│   │       ├── train_taxonomy.tsv
│   │       └── train_terms.tsv
│   └── submissions
├── docs
├── models
├── notebooks
├── src
│   ├── __init__.py
│   └── main.py
└── tests
```

### Downloading Datasets

You can download datasets from Kaggle using the `download_data` function:

```
kaggle_util download_data <competition_name> <target_dir>
```

### Uploading Notebook

You can upload notebook to Kaggle using the `push_notebook` function:

```
kaggle_util push_notebook <notebook path> <notebook_name>  <competition_name> <kernel_type>

Like:
kaggle_util push_notebook "<basedir>/new.ipynb" "test2notebook"  "cafa-5-protein-function-prediction" "notebook"
```

### Submitting Results

You can submit your results to a Kaggle competition using the `submit_result` function:

```
kaggle_util submit_prediction <competition_name> <submission_file> <message>

Like:
kaggle_util submit_prediction "cafa-5-protein-function-prediction" "<base_path>/submission.tsv" "nothing"
```

### Viewing Leaderboard

You can view the leaderboard of a Kaggle competition using the `leaderboard` function:

```
kaggle_util leaderboard <competition_name>

Like:
kaggle_util leaderboard cafa-5-protein-function-prediction
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.