from pathlib import Path

from rlbot.utils.game_state_util import GameState, BoostState, BallState, CarState, Physics, Vector3, Rotator
from rlbot.matchconfig.match_config import MatchConfig, PlayerConfig, Team
from rlbottraining.rng import SeededRandomNumberGenerator
from rlbottraining.match_configs import make_empty_match_config
from rlbot.matchconfig.conversions import read_match_config_from_file
from rlbottraining.training_exercise import TrainingExercise, Playlist

def make_match_config_with_my_bot() -> MatchConfig:
    # Makes a config which only has our bot in it for now.
    # For more details: https://youtu.be/uGFmOZCpel8?t=375
    match_config = make_empty_match_config()
    match_config.player_configs = [
        PlayerConfig.bot_config(
            Path(__file__).absolute().parent.parent / 'src' / 'bot.cfg',
            Team.BLUE
        ),
    ]
    return match_config

def make_match_config_with_human() -> MatchConfig:
    # Makes a config with a single human.
    match_config = make_empty_match_config()
    match_config.player_configs = [
        PlayerConfig.bot_config(
            Path(__file__).absolute().parent.parent / 'src' / 'bot.cfg',
            Team.BLUE
        ),
    ]
    human = match_config.player_configs[0]
    human.bot = False
    human.rlbot_controlled = False
    human.human_index = 0
    return match_config

def make_match_config_with_cfg() -> MatchConfig:
    # Makes a config from the rlbot.cfg file for match customization.
    localPath = Path(__file__).absolute().parent.parent
    match_config = read_match_config_from_file(localPath / 'rlbot.cfg' )
    return match_config


def add_my_bot_to_playlist(exercises: Playlist) -> Playlist:
    """
    Updates the match config for each excercise to include
    the bot from this project
    """
    for exercise in exercises:
        exercise.match_config = make_match_config_with_my_bot()
    return exercises

def add_human_to_playlist(exercises: Playlist) -> Playlist:
    """
    Updates the match config for each excercise to include
    a human controller
    """
    for exercise in exercises:
        exercise.match_config = make_match_config_with_human()
    return exercises

def add_cfg_to_playlist(exercises: Playlist) -> Playlist:
    """
    Updates the match config for each excercise to include
    the desired configuration based on rlbot.cfg
    """
    for exercise in exercises:
        exercise.match_config = make_match_config_with_cfg()
    return exercises

def get_car_start_near_goal(rng: SeededRandomNumberGenerator) -> Vector3:
    return Vector3(rng.uniform(1000, 2000), 3000, 0)