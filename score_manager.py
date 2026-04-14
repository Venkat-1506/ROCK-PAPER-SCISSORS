import os

FILE_NAME = "rps_score.txt"

def save_score(winner):
    with open(FILE_NAME, "a") as file:
        file.write(winner + "\n")

def get_scores():
    scores = {"Player": 0, "Computer": 0, "Draw": 0}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                result = line.strip()
                if result in scores:
                    scores[result] += 1

    return scores