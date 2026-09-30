from metrics import accuracy, f1, macro_f1, per_class, precision, recall


def test_accuracy():
    assert accuracy(["a", "b", "a"], ["a", "b", "b"]) == 2 / 3


def test_precision_recall_basic():
    assert precision(3, 1) == 0.75
    assert recall(3, 3) == 0.5


def test_f1_basic():
    assert abs(f1(0.5, 0.5) - 0.5) < 1e-9


def test_label_never_predicted():
    # "c" appears in the gold labels but the model never predicts it.
    # Its precision, recall and F1 should all be 0.0, not a crash.
    y_true = ["a", "b", "c", "a"]
    y_pred = ["a", "b", "a", "a"]
    assert per_class(y_true, y_pred)["c"] == (0.0, 0.0, 0.0)


def test_macro_f1_with_missing_label():
    y_true = ["a", "b", "c", "a"]
    y_pred = ["a", "b", "a", "a"]
    # a: p=2/3, r=1, f1=0.8 ; b: 1.0 ; c: 0.0
    assert abs(macro_f1(y_true, y_pred) - (0.8 + 1.0 + 0.0) / 3) < 1e-9


if __name__ == "__main__":
    failed = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            try:
                fn()
                print("PASS", name)
            except Exception as e:
                failed += 1
                print("FAIL", name, type(e).__name__, e)
    raise SystemExit(1 if failed else 0)
