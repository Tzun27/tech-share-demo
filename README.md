# sentiment-eval

Demo repo for the tech share. Clone: `git clone https://github.com/Tzun27/tech-share-demo.git`

A small research-code repo used as the running example in the tech share.

- `evaluate.py` scores a sentiment classifier's predictions (`data/predictions.csv`).
- `metrics.py` holds the metric functions; `test_metrics.py` tests them (`python3 test_metrics.py`).
- `logs/` holds training logs from 30 runs, written by three different versions of the training script.
- `summarize_logs.sh` turns those logs into `results.csv` with a language model.
- `notes/` holds rough weekly notes and a draft paragraph; `prompts/` holds the prompt for each chore.
- `setup/` holds the model entries for `llm` and `pi`, and a check script.
- `tools/` holds the log generator, the known answers, and a scorer for `results.csv`.

Start with `FOLLOW_ALONG.md`.

## Sources cited on the slides

Model charts (vendor-published):

- Qwen3.5-9B model card: https://huggingface.co/Qwen/Qwen3.5-9B
- Gemma 4 announcement: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- Gemini 3 Flash announcement: https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/
- Gemini 3.1 Pro announcement: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/

Tools:

- llm: https://github.com/simonw/llm
- pi: https://github.com/earendil-works/pi
- ccusage: https://github.com/ccusage/ccusage
- Marp: https://github.com/marp-team/marp-cli

Token-saving tools, measured by third parties:

- RTK, JetBrains: https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/
- RTK, Quesma: https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/
- RTK and Headroom, arXiv 2607.12161: https://arxiv.org/abs/2607.12161
- caveman, JetBrains: https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/
- graphify, KubeBlogs: https://www.kubeblogs.com/graphify-claims-71-5x-fewer-tokens-we-tested-it-on-real-production-work/
- GitHub star counts: GitHub API, 30 September 2026

Subscription-login tools and the provider's terms:

- 9Router: https://github.com/decolua/9router (its `src/shared/constants/providersDisplay.js` carries the ban warning)
- Anthropic, Claude Code legal and compliance: https://code.claude.com/docs/en/legal-and-compliance
