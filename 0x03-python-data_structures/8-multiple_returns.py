#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns length of a string the first character."""
    if sentence == '':
        return 0, None
    return len(sentence), sentence[0]
