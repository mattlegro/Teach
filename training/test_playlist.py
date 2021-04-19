from exercises import *
from graders import *
from training_util import *

def make_default_playlist():
    exercises = [
        DrivesToBallExercise('Get to ball')
    ]
    for exercise in exercises:
        exercise.match_config = make_match_config_with_cfg()

    return exercises
