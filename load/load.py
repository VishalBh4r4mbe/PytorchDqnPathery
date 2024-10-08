from common import common

import torch

def main(model_path):
  env = common.getEnv()
  device = common.getDevice()
  print(f'Using device {device}')

  policy_net = torch.jit.load(model_path)
  policy_net.eval()
  print(f'Policy net: {policy_net}')

  observation, info = env.reset()
  observationTensor = common.observationToTensor(env, observation, device)
  print(env.render())
  print(f'Initial info: {info}')

  done = False

  while not done:
    action = common.select_action(env, observationTensor, policy_net, device, eps_threshold=None, deterministic=True)

    observation, reward, terminated, truncated, info = env.step(action.item())
    observationTensor = common.observationToTensor(env, observation, device)
    print(env.render())
    print(f'info: {info}')

    done = terminated

if __name__ == "__main__":
  main()