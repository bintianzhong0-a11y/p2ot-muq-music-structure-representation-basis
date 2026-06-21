"""P²OT-related utilities.

This file is a lightweight scaffold. Add the main P²OT implementation here.
"""

from __future__ import annotations

import numpy as np


def row_normalize(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Normalize rows of an array so that each row sums to one."""
    x = np.asarray(x, dtype=float)
    denom = x.sum(axis=1, keepdims=True)
    return x / np.maximum(denom, eps)


def probability_path_distance(gamma: np.ndarray) -> np.ndarray:
    """Compute frame-to-frame L2 changes for a probability path.

    Parameters
    ----------
    gamma:
        Array of shape ``(T, K)`` representing frame-wise probability vectors.

    Returns
    -------
    np.ndarray
        Array of length ``T - 1`` containing local changes.
    """
    gamma = row_normalize(gamma)
    return np.linalg.norm(np.diff(gamma, axis=0), axis=1)
