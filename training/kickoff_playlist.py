from exercises import *
from graders import *
from training_util import *

from rlbottraining.common_exercises.kickoff_exercise import *

def make_default_playlist():
    exercises = [
        # KickoffExercise('Both Corners', blue_spawns=[Spawns.CORNER_R, Spawns.CORNER_L], orange_spawns = []),
        #KickoffExercise('Right Corner 50/50', blue_spawns=[Spawns.CORNER_R], orange_spawns = [Spawns.CORNER_R]),
        KickoffExercise('Right Corner', blue_spawns=[Spawns.CORNER_R], orange_spawns = []),
        KickoffExercise('Left Corner', blue_spawns=[Spawns.CORNER_L], orange_spawns = []),
        KickoffExercise('Back Right', blue_spawns=[Spawns.BACK_R], orange_spawns = []),
        KickoffExercise('Back Left', blue_spawns=[Spawns.BACK_L], orange_spawns = []),
        KickoffExercise('Straight', blue_spawns=[Spawns.STRAIGHT], orange_spawns = []),
    ]
    for exercise in exercises:
        exercise.match_config = make_match_config_with_cfg()

    return exercises
