import kaggle


def view_leaderboard(competition):
    """
    View the leaderboard of a Kaggle competition using the Kaggle API.

    Args:
        competition (str): The slug of the Kaggle competition.

    Returns:
        None
    """
    res = {}
    try:
        # Retrieve the leaderboard data from Kaggle
        res['leaderboard_data'] = kaggle.api.competition_leaderboard(competition=competition)
        for i, row in enumerate(res['leaderboard_data']):
            if row['teamName'] == 'private':
                res['private_score'] = float(row['score'])
            elif row['teamName'] == 'public':
                res['public_score'] = float(row['score'])
            elif row['teamName'] == 'your_team_name':
                res['your_score'] = float(row['score'])
                res['your_position'] = i + 1
    except kaggle.api.KaggleApiError as e:
        print(f"Error retrieving leaderboard data: {str(e)}")
    return res
