import gym
from gym_fearbun.envs.raceboard import space_to_action
import time
import os

env = gym.make('gym_fearbun:raceboard-v0', map_name='map1.txt')

env.reset()
done = False
while not done:
    action = env.action_space.sample()
    print(env.s)
    s, r, done, _ = env.step(action)
    print(s, space_to_action(action))
    env.render()
    time.sleep(0.1)
    os.system('clear')