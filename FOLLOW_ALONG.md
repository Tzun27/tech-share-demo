# Follow-along commands

Run everything from the repo root. Each chore ends with a way to check the result.

## Before the session

```sh
# 0. Get the repo
git clone https://github.com/Tzun27/tech-share-demo.git && cd tech-share-demo

# 1. Tools (macOS; on Linux: `uv tool install llm` and `npm install -g @earendil-works/pi-coding-agent`, Node 22.19+;
#    Windows: use WSL and follow the Linux lines). Node.js is also needed for npx (ccusage, Marp): `brew install node`
brew install llm pi-coding-agent

# 2. Model entries for llm and pi (-n keeps any file you already have)
cp -n setup/extra-openai-models.yaml "$(dirname "$(llm logs path)")/"
mkdir -p ~/.pi/agent && cp -n setup/models.json ~/.pi/agent/

# 3. Your lab key (paste it when asked)
llm keys set lab

# 4. Check
./setup/check.sh
```

Local track only (Apple Silicon Mac, 16 GB or more). Allow about 35 minutes, mostly a 5.6 GB download. Run this from inside the cloned repo, after step 0:

```sh
brew install mlx-lm
cat setup/qwen.zsh >> ~/.zshrc && source ~/.zshrc
qwen "hello"          # first run downloads the model
qwen-serve            # keep this running in a second terminal during the session
```

## Pick your tier

```sh
# Lab track (free Gemma on the lab server)
export M=lab-gemma PM=lab/gemma4:31b-IT-NVFP4

# Local track (qwen-serve running in another terminal)
export M=qwen-local PM=mlx/mlx-community/Qwen3.5-9B-MLX-4bit
```

## Chore 1: the evaluation script crashes

```sh
python3 evaluate.py                                                    # see the crash
python3 evaluate.py 2>&1 | llm -m $M -s "$(cat prompts/explain.txt)"   # what went wrong?
pi -p --model "$PM" "$(cat prompts/fix.txt)"                           # let an agent fix it (about a minute)
```

Check, then commit:

```sh
python3 test_metrics.py && python3 evaluate.py
git diff | llm -m $M -s "$(cat prompts/commit.txt)"
```

## Chore 2: thirty logs into one table

```sh
./summarize_logs.sh $M 10        # first 10 logs; leave out the number for all 30
# Gemini users: same, with reasoning turned off
# LLM_OPTS='-o reasoning_effort minimal' ./summarize_logs.sh lab-flash 10
python3 tools/score.py           # compare with the known answers
```

## Chore 3: writing

```sh
llm -m $M -s "$(cat prompts/report.txt)" < notes/weekly_notes.md
llm -m $M -s "$(cat prompts/proofread.txt)" < notes/draft_paragraph.txt > polished.txt
git diff --no-index --word-diff notes/draft_paragraph.txt polished.txt   # what did it change?
```

## Chore 4: slides

```sh
llm -m $M -s "$(cat prompts/slides.txt)" < notes/weekly_notes.md | grep -v '^```' > slides.md
npx -y @marp-team/marp-cli slides.md -o slides.html
open slides.html                 # xdg-open on Linux
```

## Chore 5: docs

```sh
llm -m $M -s "$(cat prompts/docs.txt)" < metrics.py
```

## Reset

```sh
git checkout -- . && rm -f results.csv polished.txt slides.md slides.html
```

## House rules

- The lab's Gemma is shared and slow (about 7 tokens per second). Keep inputs small; do not paste whole repos into it.
- `lab-flash` (Gemini) is fast but draws on your $10 monthly budget. For simple tasks add `-o reasoning_effort minimal`.
- `pi` runs shell commands as you, without asking. Use it in this repo only.
- Check every result. The checks above exist because the models do make mistakes.
