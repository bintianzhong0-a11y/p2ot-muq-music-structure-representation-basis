"""Feature-processing utilities for music structure experiments."""

from __future__ import annotations

import numpy as np


def zscore_features(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    """Apply feature-wise z-score normalization."""
    x = np.asarray(x, dtype=float)
    mean = x.mean(axis=0, keepdims=True)
    std = x.std(axis=0, keepdims=True)
    return (x - mean) / np.maximum(std, eps)
