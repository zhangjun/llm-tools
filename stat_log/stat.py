import sys
import json
import numpy as np

# cat moe_vllm_worker*err.log* | grep "time_cost:" 
# cat model_worker_default.log.2024-04-* | grep "2024-04-17" | grep "completion_tokens" | python ../fantasky_llm_logs/stat.py

cost_data = []
prompt_data = []
completion_data = []
total_data = []
count = 0
for line in sys.stdin:
  data = line.strip().split('. || time_cost:')
  try:
    cost = float(data[1].split(' s.')[0])
    # print(data[0])
    res = eval(data[0].split('response:')[1])
  except:
    continue

  prompt_tokens = res["usage"]["prompt_tokens"] 
  completion_tokens = res["usage"]["completion_tokens"]
  total_tokens = res["usage"]["total_tokens"]
  cost_data.append(cost)
  prompt_data.append(prompt_tokens)
  completion_data.append(completion_tokens)
  total_data.append(total_tokens)
  count += 1

print("total token: ", np.sum(total_data))
print("cost avg: ", np.mean(cost_data), ", p50: ", np.percentile(cost_data, 50), ", p90: ", np.percentile(cost_data, 90))
print("prompt: ", np.mean(prompt_data), np.std(prompt_data), ", p50: ", np.percentile(prompt_data, 50), ", p90: ", np.percentile(prompt_data, 90))
print("generation: ", np.mean(completion_data), np.std(completion_data), ", p50: ", np.percentile(completion_data, 50), ", p90: ", np.percentile(completion_data, 90))
print("total: ", np.mean(total_data), ", p50: ", np.percentile(total_data, 50), ", p90: ", np.percentile(total_data, 90))