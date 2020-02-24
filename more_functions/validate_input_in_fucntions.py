def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again'):
    """Takes parameters"""
    while True:
        if test_score >= 0 and test_score < 100:
            return test_name + " : " + str(test_score)
        else:
            return invalid_message

