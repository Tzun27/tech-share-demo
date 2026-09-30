#!/bin/sh
# Turn training logs into one CSV row each with a language model.
# Usage: ./summarize_logs.sh <llm model id> [how many logs]     e.g. ./summarize_logs.sh lab-gemma 10
# Extra llm options go in LLM_OPTS, e.g. LLM_OPTS='-o reasoning_effort minimal' ./summarize_logs.sh lab-flash
MODEL=${1:?usage: ./summarize_logs.sh <llm model id> [how many logs]}
COUNT=${2:-1000}
PROMPT=$(cat prompts/logs.txt)

echo "run_id,model,lr,status,best_val_acc" > results.csv
ls logs/*.log | head -n "$COUNT" | while read -r f; do
  id=$(basename "$f" .log)
  line=$(llm -m "$MODEL" $LLM_OPTS -s "$PROMPT" < "$f" | grep -v '^```' | grep . | tail -1)
  echo "$id,$line" >> results.csv
  echo "$id,$line"
done
