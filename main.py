import gym
from gym_fearbun.envs.raceboard import space_to_action
import time
import os

env = gym.make('gym_fearbun:raceboard-v0', map_name='map1.txt')

env.reset()
done = False
input()
while not done:
    action = space_to_action(env.action_space.sample())
    print(env.s)
    # action = (1, 1)

    s, r, done, _ = env.step(action)
    print(s, action)
    env.render()
    time.sleep(0.1)
    os.system('clear')