# P²OT Music Structure Representation

A small research repository for **music structure representation** using **MuQ audio embeddings** and **Prior-guided Partial Optimal Transport (P²OT)**.

This repository is prepared as a reproducible research artifact for a graduate-school research plan on music structure representation.

---

## 日本語概要

本研究では、音楽に含まれる反復、展開、雰囲気の変化、和声遷移などの時間的構造を、定量的に扱える表現として捉えることを目的とする。MuQ による音響特徴量と P²OT による最適輸送的割当を用いることで、楽曲構造を数値的・視覚的に扱え、かつ運用に音楽の専門知識を必要としない、拡張性をもった表現基盤の構築を試みる。

---

## Research Motivation / 研究動機

Music contains temporal structures such as repeated sections, development, atmosphere changes, and harmonic transitions. These structures are important for music analysis, creative support, recommendation, and music understanding, but they are often difficult to handle without expert-level music-theory knowledge.

This project explores a representation basis that converts audio-derived features into probabilistic and geometric trajectories. The aim is to make musical structure easier to analyze numerically and visually.

---

## 日本語概要

音楽には、反復、展開、雰囲気の変化、和声遷移など、時間とともに変化する多層的な構造が含まれている。しかし、これらの構造を分析するには、従来は音楽理論や楽曲形式に関する専門知識が必要となる場合が多く、制作者や鑑賞者が直感的に活用できる形で扱うことは容易ではない。

本研究の動機は、深層学習によって得られる音響特徴量と、確率的・幾何的な割当手法を組み合わせることで、音楽の時間的構造を数値的・視覚的に扱える表現基盤を構築することである。これにより、専門的な音楽理論に依存しすぎず、楽曲分析、創作支援、推薦、教育などへ拡張可能な音楽理解の基盤を目指す。


---

## Core Idea / 基本アイデア

The proposed pipeline is:

1. Extract frame-level audio embeddings using **MuQ**.
2. Convert embeddings into probabilistic structural assignments using **P²OT**.
3. Represent each song as a temporal probability path.
4. Compute local and global structural change scores.
5. Evaluate the representation on structure boundary detection and harmonic probing tasks.

Conceptually, this repository treats music structure as a trajectory in a probabilistic representation space.

---

## 日本語概要

本研究の処理の流れは、以下の 5 段階で構成される。

1. **MuQ** を用いて、楽曲音響からフレーム単位の音響埋め込み表現を抽出する。

2. 抽出した埋め込み表現を、**P²OT** による最適輸送的割当を用いて、確率的な構造表現へ変換する。

3. 各楽曲を、時間方向に変化する確率ベクトルの系列、すなわち **temporal probability path** として表現する。

4. 確率経路の時間変化や自己距離構造を用いて、局所的および大域的な楽曲構造変化スコアを計算する。

5. 得られた表現を、楽曲構造境界検出および和声的プロービング課題によって評価する。


---

## Keywords

- Music Structure Analysis
- Music Information Retrieval
- MuQ
- P²OT
- Optimal Transport
- Probabilistic Representation
- Harmonic Analysis
- Structure Boundary Detection
- POP909
- Harmonix

---

## Repository Structure

```text
p2ot-music-structure-representation/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── notebooks/
│   ├── README.md
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── p2ot.py
│   ├── features.py
│   ├── evaluation.py
│   └── visualization.py
├── reports/
│   ├── research_plan.pdf
│   ├── experiment_report_1.pdf
│   ├── experiment_report_2.pdf
│   ├── experiment_report_3.pdf
│   └── experiment_report_4.pdf
├── figures/
│   ├── README.md
│   └── .gitkeep
├── results/
│   ├── README.md
│   └── sample_outputs/
│       └── .gitkeep
├── data/
│   └── README.md
└── references/
    └── README.md
```

---

## Method Overview

### 1. Audio Feature Extraction

Audio is first converted into frame-level embeddings using MuQ. These embeddings are expected to capture musical information related to timbre, harmony, rhythm, and local texture.

### 2. P²OT-based Structural Assignment

P²OT is used to assign each temporal frame to a set of latent structural prototypes. Instead of forcing each frame into a single hard cluster, the method represents each frame as a probability vector.

Let the representation at time frame \(t\) be:

\[
\gamma_i^{(t)} \in \Delta^{K-1}
\]

where \(K\) is the number of structural prototypes and \(\Delta^{K-1}\) is the probability simplex.

### 3. Probability Path Representation

A song is represented as a trajectory:

\[
\Gamma_i = \left( \gamma_i^{(1)}, \gamma_i^{(2)}, \ldots, \gamma_i^{(T_i)} \right)
\]

This trajectory can be used to visualize musical development, repetition, and transition.

### 4. Local and Global Change Scores

The project uses probability-path changes and self-distance structures to estimate musical boundaries.

Example notation:

\[
\delta_i^{(t)}, \quad \nu_i^{(t)}, \quad \nu_{\mathcal A,i}^{(t)}, \quad S_{\lambda,i}^{(t)}
\]

where \(S_{\lambda,i}^{(t)}\) denotes a mixed structural change score.

---

## Preliminary Experiments

The following values are preliminary research results and should be interpreted as experimental evidence rather than final benchmark claims.

### Music Structure Boundary Detection

| Setting | Dataset | Metric | Result |
|---|---:|---:|---:|
| Point-level boundary detection | Harmonix | HR3F macro | approx. 0.408 |
| Band-based boundary detection | Harmonix | HR3F macro | approx. 0.662 ± 0.019 |
| Band-based boundary detection | Harmonix | HR3F micro | approx. 0.673 ± 0.018 |

### Harmonic Probing

| Setting | Dataset | Metric | Result |
|---|---:|---:|---:|
| Root-normalized chroma probe | POP909 | Macro-F1 | approx. 0.524 |
| P²OT representation with harmonic probe | POP909 | Macro-F1 | experimental |
| P²OT + HSMM-lite support | POP909 | Macro-F1 | experimental |

These experiments suggest that the proposed representation may capture both large-scale musical structure and local harmonic tendencies.

---

## Intended Use

This repository is intended for:

- graduate-school research-plan presentation,
- preliminary Music Information Retrieval experiments,
- music structure visualization,
- creative-support research,
- probabilistic representation analysis of music audio.

---

## What Is Not Included

This repository does **not** include copyrighted audio files or raw commercial music data.

Datasets such as Harmonix and POP909 should be obtained from their original sources according to their respective licenses and terms of use.

Large intermediate feature files are also excluded from the repository. Users should regenerate features locally or on Google Colab.

---

## Installation

```bash
pip install -r requirements.txt
```

The current repository is a research scaffold. Full experimental notebooks and additional scripts may be added progressively.

---

## Reproducibility Notes

To reproduce the experiments, prepare the following externally:

1. Audio dataset or permitted local audio files.
2. MuQ feature extraction environment.
3. P²OT assignment script.
4. Evaluation metadata for boundary detection or harmonic probing.

Recommended workflow:

```text
Audio files
  ↓
MuQ embeddings
  ↓
P²OT probability assignments
  ↓
Probability-path visualization
  ↓
Boundary / harmonic evaluation
```

---

## Reports

The `reports/` directory contains research-plan and experiment-report PDFs prepared for this project.

- `research_plan.pdf`
- `experiment_report_1.pdf`
- `experiment_report_2.pdf`
- `experiment_report_3.pdf`
- `experiment_report_4.pdf`

---

## License

This repository is released under the MIT License.

The license applies to the code and original text in this repository. External datasets, papers, models, and audio files are governed by their own licenses.

---

## Author

Akira Tanaka

GitHub: `bintianzhong0-a11y`
