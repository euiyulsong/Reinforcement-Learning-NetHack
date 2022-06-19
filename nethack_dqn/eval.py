from dqn_model import DuelDQNModel, DQNAgent, TargetNet
from replay_buffer import ReplayBuffer, fill, evfill
from common_utils import *
from nethack_wrapper import make_env
from args import get_args

import torch
import torch.nn as nn
from tqdm import trange
from tensorboardX import SummaryWriter

import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from test_submission import evaluate


def eva():
    with torch.no_grad():
        writer = SummaryWriter('logs/result')

        args = get_args()
        print(vars(args))

        env = make_env()
        print(env.action_space)
        observation_shape = env.observation_space.shape
        print('obs shape', observation_shape)
        n_actions = env.action_space.n
        net = DuelDQNModel(observation_shape, n_actions).to(args.device)
        net.load_state_dict(torch.load('/home/jaelee/nethack/nethack_raph/neurips2021-nethack-raph/nethack_dqn/model'))
        target_net = TargetNet(net)
        exp_replay = ReplayBuffer(args.buffer_size)

        agent = DQNAgent(net, args.init_eps, args.device)
        

        # optimizer = torch.optim.Adam(net.parameters(), lr=args.lr)

        state = env.reset()
        state = fill(exp_replay, agent, env, state, n_steps=args.init_buff_size)

        tot_step = 512
        reward = 0
        print('total evalutation step:', tot_step)
        for step in range(0, tot_step):
            

            agent.epsilon = args.eval_eps
            

            # play
            state, mean_reward = evfill(agent, env, state, n_steps=10000000000)
            
            print("step:", step, "reward:", mean_reward)
            reward += mean_reward
            
            writer.add_scalar('reward', mean_reward, step)
            
        print('mean_reward: ', reward / (tot_step+1))

           


if __name__ == '__main__':
    eva()
