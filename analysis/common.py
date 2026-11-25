"""Shared paths and a small check helper: every number used in the deck is recomputed and compared."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
RESULTS = []


def load(name, **kw):
    return pd.read_csv(DATA / name, **kw)


def check(page, label, got, deck):
    """Record a recomputed value next to the value printed in the deck."""
    ok = str(got) == str(deck)
    RESULTS.append((page, label, got, deck, ok))
    print(f"[{'OK' if ok else 'DIFF'}] {page} · {label}: {got} (deck: {deck})")
    return got
