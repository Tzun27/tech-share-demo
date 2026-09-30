"""Generate the 30 training logs and tools/answers.csv. Deterministic: python3 tools/make_logs.py"""
import csv
import json
import os
import random

random.seed(7)
MODELS = ["bert-base-uncased", "roberta-base", "distilbert-base-uncased", "deberta-v3-small"]
LRS = [1e-5, 2e-5, 3e-5, 5e-5]
os.makedirs("logs", exist_ok=True)
answers = []

for i in range(1, 31):
    run = f"run_{i:03d}"
    model = random.choice(MODELS)
    lr = random.choice(LRS)
    bs = random.choice([16, 32])
    seed = random.randint(1, 5)
    epochs = random.randint(6, 10)
    style = "ABC"[i % 3]
    fate = random.choices(["ok", "oom", "nan"], weights=[8, 1, 1])[0]
    stop_at = epochs if fate == "ok" else random.randint(2, epochs - 1)

    acc, loss, accs, lines = random.uniform(0.62, 0.70), random.uniform(0.95, 1.1), [], []
    if style == "A":
        lines += [f"[train.py v1] starting {run}", f"model={model} lr={lr:g} bs={bs} seed={seed} epochs={epochs}",
                  "loading dataset sst-3 ... 8544 train / 1101 val"]
    elif style == "B":
        lines += [f"=== Training run {run} ===",
                  "config: " + json.dumps({"model": model, "learning_rate": lr, "batch_size": bs, "seed": seed, "num_epochs": epochs}),
                  "Loaded 8544 training and 1101 validation examples"]
    else:
        lines += [f"# {run}", f"model: {model}", f"lr: {lr:g}", f"batch_size: {bs}", f"seed: {seed}", f"max_epochs: {epochs}", "data: sst-3"]

    for ep in range(1, stop_at + 1):
        acc = min(0.93, acc + random.uniform(-0.012, 0.045))
        loss = max(0.12, loss - random.uniform(0.02, 0.13))
        accs.append(round(acc, 3))
        if style == "A":
            lines.append(f"epoch {ep}/{epochs} train_loss={loss:.3f} val_acc={acc:.3f}")
        elif style == "B":
            lines.append(f"[Epoch {ep:02d}] loss: {loss:.2f} | val accuracy: {acc * 100:.1f}%")
        else:
            lines.append(f"ep={ep} loss={loss:.3f} acc_val={acc:.3f} time={random.randint(88, 140)}s")
        if random.random() < 0.25:
            lines.append("UserWarning: lr scheduler step called before optimizer step")

    best = max(accs)
    if fate == "oom":
        lines += ["Traceback (most recent call last):", '  File "train.py", line 212, in train_epoch',
                  "RuntimeError: CUDA out of memory. Tried to allocate 1.17 GiB (GPU 0; 23.69 GiB total capacity)"]
    elif fate == "nan":
        lines += [f"epoch {stop_at + 1}: loss is nan, aborting run" if style != "B" else f"[Epoch {stop_at + 1:02d}] loss: nan -- stopping, loss diverged"]
    elif style == "A":
        lines += [f"Training finished. best val_acc={best:.3f} (epoch {accs.index(best) + 1})", "saved checkpoint to ckpt/best.pt"]
    elif style == "B":
        lines += [f"Done. Best validation accuracy {best * 100:.1f}% at epoch {accs.index(best) + 1}"]
    else:
        lines += ["finished"]          # style C never prints a summary: the best epoch has to be found

    with open(f"logs/{run}.log", "w") as f:
        f.write("\n".join(lines) + "\n")
    answers.append([run, model, f"{lr:g}", fate, f"{best:.3f}"])

with open("tools/answers.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["run_id", "model", "lr", "status", "best_val_acc"])
    w.writerows(answers)
print(f"wrote {len(answers)} logs")
