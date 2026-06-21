"""Evaluation utilities for preliminary experiments."""

from __future__ import annotations

import numpy as np


def peak_indices(score: np.ndarray, threshold: float) -> np.ndarray:
    """Return indices whose score is greater than or equal to a threshold."""
    score = np.asarray(score, dtype=float)
    return np.where(score >= threshold)[0]
