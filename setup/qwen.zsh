# --- Qwen3.5-9B local via mlx-lm -------------------------------------------
# Loads on demand, exits when done. No daemon, no idle cost.
export QWEN_MODEL="mlx-community/Qwen3.5-9B-MLX-4bit"
export HF_HUB_DISABLE_PROGRESS_BARS=1   # silence cache-check noise

# Default: non-thinking. Args or piped stdin. `qwen "why is the sky blue"`
qwen() {
  mlx_lm.generate --model "$QWEN_MODEL" \
    --temp 0.7 --top-p 0.8 --top-k 20 --max-tokens 2048 \
    --chat-template-config '{"enable_thinking":false}' \
    --verbose False --prompt "${*:--}"
}

# Thinking mode for hard problems. Big budget — it needs >1k tokens to be useful.
qwen-think() {
  mlx_lm.generate --model "$QWEN_MODEL" \
    --temp 1.0 --top-p 0.95 --top-k 20 --max-tokens 16384 \
    --verbose False --prompt "${*:--}"
}

# OpenAI-compatible API on :8080 while it runs. Ctrl-C to reclaim the RAM.
qwen-serve() {
  mlx_lm.server --model "$QWEN_MODEL" --port 8080 \
    --temp 0.7 --top-p 0.8 --top-k 20 --max-tokens 8192 \
    --chat-template-args '{"enable_thinking":false}'
}
# ---------------------------------------------------------------------------
