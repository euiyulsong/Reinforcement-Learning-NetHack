CUDA_VISIBLE_DEVICES=1 nohup python main.py \
--policy "DDPG" \
--seed 0 \
--env "NetHackChallenge-v0" > main_ddpg.log &
