"""Classification metrics for the sentiment experiments."""


def counts(y_true, y_pred, label):
    """Return (tp, fp, fn) for one label."""
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == label and p == label)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t != label and p == label)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == label and p != label)
    return tp, fp, fn


def precision(tp, fp):
    return tp / (tp + fp)


def recall(tp, fn):
    return tp / (tp + fn)


def f1(p, r):
    return 2 * p * r / (p + r)


def per_class(y_true, y_pred):
    """Return {label: (precision, recall, f1)} for every label in y_true."""
    out = {}
    for label in sorted(set(y_true)):
        tp, fp, fn = counts(y_true, y_pred, label)
        p = precision(tp, fp)
        r = recall(tp, fn)
        out[label] = (p, r, f1(p, r))
    return out


def macro_f1(y_true, y_pred):
    scores = per_class(y_true, y_pred)
    return sum(f for _, _, f in scores.values()) / len(scores)


def accuracy(y_true, y_pred):
    return sum(1 for t, p in zip(y_true, y_pred) if t == p) / len(y_true)
