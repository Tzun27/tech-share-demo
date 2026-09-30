# sentiment-eval

A small research-code repo used as the running example in the tech share.

- `evaluate.py` scores a sentiment classifier's predictions (`data/predictions.csv`).
- `metrics.py` holds the metric functions; `test_metrics.py` tests them (`python3 test_metrics.py`).
- `logs/` holds training logs from 30 runs, written by three different versions of the training script.
- `summarize_logs.sh` turns those logs into `results.csv` with a language model.
- `notes/` holds rough weekly notes and a draft paragraph; `prompts/` holds the prompt for each chore.
- `setup/` holds the model entries for `llm` and `pi`, and a check script.
- `tools/` holds the log generator, the known answers, and a scorer for `results.csv`.

Start with `FOLLOW_ALONG.md`.
