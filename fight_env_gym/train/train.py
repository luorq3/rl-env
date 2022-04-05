import fight_env_gym

from stable_baselines3 import A2C


if __name__ == "__main__":
    env = fight_env_gym.make("Fight-rgb-v0")

    model = A2C("CnnPolicy", env, tensorboard_log='tb_log', create_eval_env=False, verbose=2)
    model.learn(total_timesteps=10000)

    obs = env.reset()
    for i in range(1000):
        action, _state = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
            obs = env.reset()


