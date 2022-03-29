import time

import gym

import fight_env_gym
import numpy as np
import pygame
from PIL import Image
# from fight_env_gym import FightEnvRGB


# Action={0:NOOP, 1:UP, 2:DOWN, 3:LEFT, 4:RIGHT, 5:FIRE}
def play_with_render(env: gym.Env):
    clock = pygame.time.Clock()
    score = 0

    obs = env.reset()
    while True:
        env.render()

        # Getting action
        action = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    action = 1
                elif event.key == pygame.K_DOWN:
                    action = 2
                elif event.key == pygame.K_LEFT:
                    action = 3
                elif event.key == pygame.K_RIGHT:
                    action = 4
                elif event.key == pygame.K_a or event.key == pygame.K_SPACE:
                    action = 5

        # Processing
        obs, reward, done, info = env.step(action)

        score += reward
        print(f"Obs shape: {obs.shape}")
        print(f"Score: {score}\n")

        clock.tick(30)

        if done:
            env.render()
            time.sleep(0.6)
            break


if __name__ == "__main__":
    fight_env = fight_env_gym.make("Fight-rgb-v0")

    print(f"Action space: {fight_env.action_space}")
    print(f"Observation space: {fight_env.observation_space}")

    play_with_render(env=fight_env)

    fight_env.close()
