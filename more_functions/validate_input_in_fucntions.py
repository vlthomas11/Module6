def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again'):
    """Takes parameters"""
    while True:
        if test_score >= 0:
            return test_name + " : " + str(test_score)
        else:
            print(invalid_message)
            return False

