#!/bin/sh
# Turn every training log into one CSV row with a language model.
# Usage: ./summarize_logs.sh <llm model id>      e.g. ./summarize_logs.sh qwen-local
MODEL=${1:?usage: ./summarize_logs.sh <llm model id>}
PROMPT='You read one training log. Output exactly one CSV line and nothing else, with four fields: model,lr,status,best_val_acc
- model: the model name
- lr: the learning rate
- status: ok if training finished, oom if it ran out of memory, nan if the loss became nan
- best_val_acc: the highest validation accuracy of any epoch, as a fraction with three decimals, for example 0.884'

echo "run_id,model,lr,status,best_val_acc" > results.csv
for f in logs/*.log; do
  id=$(basename "$f" .log)
  line=$(llm -m "$MODEL" -s "$PROMPT" < "$f" | grep -v '^```' | grep . | tail -1)
  echo "$id,$line" >> results.csv
  echo "$id,$line"
done
