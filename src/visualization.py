"""Visualization utilities for probability-path analysis."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def plot_probability_path(gamma: np.ndarray, title: str = "Probability Path"):
    """Plot a probability path as a heatmap."""
    gamma = np.asarray(gamma, dtype=float)
    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(gamma.T, aspect="auto", origin="lower")
    ax.set_xlabel("Frame")
    ax.set_ylabel("Prototype")
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label="Probability")
    return fig, ax
