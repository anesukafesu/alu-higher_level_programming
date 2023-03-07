#!/usr/bin/python3


def multiple_returns(sentence):
    sentence_length = len(sentence)

    if sentence_length == 0:
        return (0, None)
    else:
        return (sentence_length, sentence[0])
