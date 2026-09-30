"""Compare results.csv with the known answers: python3 tools/score.py [results.csv]"""
import csv
import sys


def load(path):
    with open(path, newline="") as f:
        return {r["run_id"]: r for r in csv.DictReader(f)}


def same(field, a, b):
    a, b = (a or "").strip(), (b or "").strip()
    if field in ("lr", "best_val_acc"):
        try:
            tol = 0.0006 if field == "best_val_acc" else 1e-9
            return abs(float(a) - float(b)) <= tol
        except ValueError:
            return False
    return a.lower() == b.lower()


truth = load("tools/answers.csv")
got = load(sys.argv[1] if len(sys.argv) > 1 else "results.csv")
fields = ["model", "lr", "status", "best_val_acc"]
right = {f: 0 for f in fields}
rows_right = 0
truth = {run: t for run, t in truth.items() if run in got}   # score only the runs that were summarized
for run, t in truth.items():
    g = got[run]
    ok = [same(f, g.get(f), t[f]) for f in fields]
    for f, o in zip(fields, ok):
        right[f] += o
    rows_right += all(ok)
    if not all(ok):
        wrong = [f"{f}: got {g.get(f)!r}, expected {t[f]!r}" for f, o in zip(fields, ok) if not o]
        print(f"  {run}: " + "; ".join(wrong))
n = len(truth)
print(f"rows fully correct: {rows_right}/{n}")
print("per field: " + ", ".join(f"{f} {right[f]}/{n}" for f in fields))
