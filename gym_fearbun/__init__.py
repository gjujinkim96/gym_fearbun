from gym.envs.registration import register

register(
    id='raceboard-v0',
    entry_point='gym_fearbun.envs:RaceboardEnv',
    map='map_1'
)