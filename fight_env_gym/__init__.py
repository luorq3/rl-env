import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Exporting envs:
from fight_env_gym.envs.fight_env_rgb import FightEnvRGB

from gym import make

from gym.envs.registration import register

register(
    id="Fight-rgb-v0",
    entry_point="fight_env_gym:FightEnvRGB"
)

__all__ = [
    make.__name__,
    FightEnvRGB.__name__
]
