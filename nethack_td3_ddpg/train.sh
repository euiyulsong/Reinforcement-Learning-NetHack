CUDA_VISIBLE_DEVICES=1 nohup python main.py \
--policy "TD3" \
--seed 0 \
--env "NetHackChallenge-v0" > main_td3.log &
