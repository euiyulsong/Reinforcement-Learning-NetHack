![Nethack Banner](https://aicrowd-production.s3.eu-central-1.amazonaws.com/misc/neurips-2021-nethack-challenge-media/nethack_final_link+preview_starter_kit.jpg)

# **[NeurIPS 2021 - The NetHack Challenge](https://www.aicrowd.com/challenges/neurips-2021-the-nethack-challenge)** - WCBC Solution

## System Environment
```bash
pip install -r requirements.txt
```

## DQN
```bash
cd nethack_dqn 
./run.sh # for training
python3 eval.py # for evaluation
```
## Shallow Embedding
```bash
cd nethack_shallow_embedding/nethack_baselines/torchbeast/
python polyhydra.py # for training
cd ../../ # go to nethack_shallow_embedding
python test_submission.py # for evaluation
```
## Transformer and SWA
```bash
cd nethack_shallow_embedding/nethack_baselines/torchbeast/
python polyhydra.py # for training
cd ../../ # go to nethack_shallow_embedding
python test_submission.py # for evaluation
```
## TD3
```bash
./nethack_td3_ddpg/train.sh # for training
./nethack_td3_ddpg/eval.sh # for evaluation
```

# DDPG
```bash
./nethack_td3_ddpg/train_ddpg.sh # for training
./nethack_td3_ddpg/eval_ddpg.sh # for evaluation
```

# MC Dropout and Deep Ensemble
We DID experiemented on them, but we were not able to refactor our code. However, we will send our code ASAP if you request us our code.
