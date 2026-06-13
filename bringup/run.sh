export LLM_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
export OPENAI_API_KEY="sk-bfe930b8e3ed4120954390415ec19ca5"
export MODEL="qwen3.7-plus"

uv run python embodichain/lab/scripts/run_agent.py \
  --gym_config configs/gym/agent/pour_water_agent/fast_gym_config.json \
  --agent_config configs/gym/agent/pour_water_agent/agent_config.json \
  --task_name SinglePourWater \
  --filter_dataset_saving \
  --filter_visual_rand \
  --recovery \
  --interactive_error_injection
