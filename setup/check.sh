#!/bin/sh
# Pre-session check: are the tools installed, and which model tiers answer?
for c in llm pi python3 git; do
  if command -v "$c" >/dev/null 2>&1; then echo "found    $c"; else echo "MISSING  $c"; fi
done
try() {
  printf '%-11s ' "$1"
  out=$(llm -m "$1" "Reply with exactly: ok" < /dev/null 2>&1 | tail -1)
  case "$out" in
    *ok*|*OK*|*Ok*) echo "answers" ;;
    *) echo "no answer ($(printf '%s' "$out" | cut -c1-70))" ;;
  esac
}
try lab-gemma
try lab-flash
try qwen-local
echo "You need lab-gemma, or qwen-local with qwen-serve running. One is enough."
