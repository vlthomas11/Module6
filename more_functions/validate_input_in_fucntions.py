def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again'):
    """Takes parameters name and score, determines if score is valid and returns name and score or error message"""
    if type(test_score) != int:
        return invalid_message
    elif test_score >= 0 and test_score < 100:
        return test_name + " : " + str(test_score)
    else:
        return invalid_message

