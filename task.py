#######################################################################
# Copyright (C) 2017 Shangtong Zhang(zhangshangtong.cpp@gmail.com)    #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################
import gym
import sys
import numpy as np
import cv2

class BasicTask:
    def transfer_state(self, state):
        return state

    def reset(self):
        return self.transfer_state(self.env.reset())

    def step(self, action):
        next_state, reward, done, info = self.env.step(action)
        next_state = self.transfer_state(next_state)
        return next_state, np.sign(reward), done, info

class MountainCar(BasicTask):
    name = 'MountainCar-v0'
    success_threshold = -110

    def __init__(self):
        self.env = gym.make(self.name)
        self.env._max_episode_steps = sys.maxsize

class CartPole(BasicTask):
    name = 'CartPole-v0'
    success_threshold = 195

    def __init__(self):
        self.env = gym.make(self.name)

class LunarLander(BasicTask):
    name = 'LunarLander-v2'
    success_threshold = 200

    def __init__(self):
        self.env = gym.make(self.name)

class PixelAtari(BasicTask):
    width = 84
    height = 84
    success_threshold = 1000

    def __init__(self, name):
        self.env = gym.make(name)

    def transfer_state(self, state):
        img = (state[:, :, 0] * 0.299 + state[:, :, 1] * 0.587 + state[:, :, 2] * 0.114) / 255.0
        img = cv2.resize(img, (self.width, self.height))
        return np.reshape(img, (1, self.width, self.height))