from typing import Optional, Tuple

import gym
import numpy as np
import pygame
from gym.core import ObsType, ActType
from fight_env_gym.envs.renderer import FightRenderer
from fight_env_gym.envs.game_logic import GameLogic


class FightEnvRGB(gym.Env):

    metadata = {"render.modes": ["human", "rgb_array"]}

    def __init__(self,
                 screen_size: Tuple[int, int] = (700, 512)):
        super(FightEnvRGB, self).__init__()
        self.action_space = gym.spaces.Discrete(6)
        self.observation_space = gym.spaces.Box(0, 255, [*screen_size, 3])

        self._screen_size = screen_size
        self._game = None
        self._renderer = FightRenderer(screen_size=self._screen_size)

    def _get_observation(self):
        self._renderer.draw_surface()
        return pygame.surfarray.array3d(self._renderer.surface)

    def reset(self, *, seed: Optional[int] = None, return_info: bool = False, options: Optional[dict] = None):
        self._game = GameLogic(screen_size=self._screen_size)
        self._renderer.game = self._game
        return self._get_observation()

    def step(self, action: ActType) -> Tuple[ObsType, float, bool, dict]:
        alive = self._game.update_state(action)
        obs = self._get_observation()

        reward = 1

        done = not alive
        # info = {"score": self._game.score}
        info = None

        return obs, reward, done, info

    def render(self, mode="human") -> Optional[np.ndarray]:
        if mode not in FightEnvRGB.metadata['render.modes']:
            raise ValueError("Invalid render mode!")

        self._renderer.draw_surface()

        if mode == 'rgb_array':
            return pygame.surfarray.array3d(self._renderer.surface)
        else:
            if self._renderer.display is None:
                self._renderer.make_display()
            self._renderer.update_display()

    def close(self):
        if self._renderer is not None:
            pygame.display.quit()
            self._renderer = None

        super().close()
        