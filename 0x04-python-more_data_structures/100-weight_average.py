#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    scores, weights = zip(*my_list)
    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weights)

    if total_weight == 0:
        return (0)
    return (total_score / total_weight)
