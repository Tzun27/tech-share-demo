"""Score a predictions file: python3 evaluate.py [data/predictions.csv]"""
import csv
import sys

from metrics import accuracy, macro_f1, per_class


def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return [r["gold"] for r in rows], [r["pred"] for r in rows]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/predictions.csv"
    y_true, y_pred = load(path)
    print(f"{len(y_true)} examples from {path}")
    print(f"accuracy  {accuracy(y_true, y_pred):.3f}")
    for label, (p, r, f) in per_class(y_true, y_pred).items():
        print(f"{label:9s} precision {p:.3f}  recall {r:.3f}  f1 {f:.3f}")
    print(f"macro-F1  {macro_f1(y_true, y_pred):.3f}")


if __name__ == "__main__":
    main()
