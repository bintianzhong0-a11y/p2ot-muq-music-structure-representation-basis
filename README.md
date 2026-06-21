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

## Method Overview / 手法概要

This project represents each song as a temporal trajectory of probabilistic structural assignments.  
本研究では、各楽曲を「時間方向に変化する確率的な構造表現」として扱う。

---

### 1. Audio Embedding Extraction / 音響埋め込み抽出

Frame-level audio embeddings are extracted from music audio using **MuQ**.  
まず、楽曲音響から **MuQ** を用いてフレーム単位の音響埋め込み表現を抽出する。これにより、音色、和声、リズム、雰囲気などを含む高次元の音響特徴を得る。

For a song, the extracted frame-level embeddings are represented as:

$$
X_i =
\left(
x_i^{(1)},
x_i^{(2)},
\ldots,
x_i^{(T_i)}
\right)
$$

$$
x_i^{(t)} \in \mathbb{R}^{d}
$$

Here, `i` denotes the song index, `t` denotes the frame index, `T_i` is the number of frames, and `d` is the embedding dimension.  
ここで、`x_i^(t)` は楽曲 `i` の時刻 `t` における MuQ 埋め込み表現を表す。

---

### 2. Probabilistic Structural Assignment / 確率的構造割当

The extracted embeddings are converted into probabilistic structural assignments using **P²OT**.  
次に、抽出された埋め込み表現を **P²OT** による最適輸送的割当により、複数の構造要素への確率的割当へ変換する。各時刻を単一ラベルに固定するのではなく、soft assignment として表すことで、音楽構造の曖昧性や連続的変化を扱う。

The probabilistic assignment at each time frame is denoted as:

$$
\gamma_i^{(t)}
=\left(
\gamma_{i,1}^{(t)},
\gamma_{i,2}^{(t)},
\ldots,
\gamma_{i,K}^{(t)}
\right)
$$

$$
\gamma_i^{(t)} \in \Delta^{K-1}
$$

$$
\sum_{k=1}^{K}
\gamma_{i,k}^{(t)}
=1
$$

$$
\gamma_{i,k}^{(t)}
\geq
0
$$

Here, `K` is the number of structural prototypes, and `Delta^(K-1)` denotes the probability simplex.  
ここで、`gamma_i,k^(t)` は、楽曲 `i` の時刻 `t` が構造プロトタイプ `k` にどの程度対応するかを表す確率である。

A simplified P²OT-based assignment objective can be written as:

$$
\Gamma_i=\arg\min_{\Gamma \geq 0}
\left[\left\langle
C_i,\Gamma
\right\rangle
+
\varepsilon
\sum_{t,k}
\Gamma_{t,k}
\left(
\log \Gamma_{t,k}

-
1
\right)
+
\lambda R(\Gamma)
\right]
$$

subject to:

$$
\sum_{k=1}^{K}
\Gamma_{t,k}
=1
$$

Here, `C_i` is the cost matrix between embeddings and structural prototypes, `epsilon` controls the smoothness of assignment, and `R(Gamma)` represents prior or temporal regularization.  
ここで、`C_i` は埋め込みと構造プロトタイプ間のコスト行列、`epsilon` は割当の滑らかさを制御するエントロピー正則化係数、`R(Gamma)` は事前情報や時間方向の安定性を反映する正則化項である。

---

### 3. Temporal Probability Path / 時間的確率経路

Each song is represented as a temporal probability path.  
各楽曲は、時刻ごとの確率ベクトルの系列として表現される。この確率経路により、楽曲内で構造的な状態がどのように変化しているかを数値的・視覚的に追跡できる。

The temporal probability path of song `i` is defined as:

$$
\Gamma_i=
\left[
\gamma_i^{(1)},
\gamma_i^{(2)},
\ldots,
\gamma_i^{(T_i)}
\right]^{\top}
$$

$$
\Gamma_i
\in
\mathbb{R}^{T_i \times K}
$$

This path describes how the structural state of a song changes over time.  
この `Gamma_i` により、楽曲全体を「確率ベクトルが時間方向に変化する軌跡」として扱うことができる。

---

### 4. Structural Change Scoring / 構造変化スコア計算

Local and global structural change scores are computed from the probability path and self-distance structure.  
確率経路の時間変化や自己距離構造を用いて、局所的な変化点や大域的な構造遷移を検出するためのスコアを計算する。これにより、反復、展開、境界、雰囲気の変化などを定量的に扱う。

A local change score is computed by comparing adjacent probability vectors:

$$
\delta_i^{(t)}=
D
\left(
\gamma_i^{(t)},
\gamma_i^{(t-1)}
\right)
$$

Here, `D` is a distance function such as Jensen-Shannon distance or cosine distance.  
ここで、`delta_i^(t)` は隣接する時刻間の局所的な変化量を表す。

To capture broader temporal changes, a window-based neighborhood change score is defined as:

$$
\nu_i^{(t)}=
D
\left(
\frac{1}{w}
\sum_{r=t-w}^{t-1}
\gamma_i^{(r)},
\frac{1}{w}
\sum_{r=t}^{t+w-1}
\gamma_i^{(r)}
\right)
$$

Here, `w` is the window size.  
ここで、`nu_i^(t)` は時刻 `t` の前後の時間窓を比較することで、より広い範囲での構造変化を表す。

The self-distance structure of the probability path is defined as:

$$
\mathcal{A}_i(t,s)=
D
\left(
\gamma_i^{(t)},
\gamma_i^{(s)}
\right)
$$

This matrix captures repetition and global structural relationships inside a song.  
この自己距離行列により、楽曲内の反復や大域的な構造関係を捉える。

A self-distance-based change score is defined as:

$$
\nu_{\mathcal{A},i}^{(t)}=
D
\left(
\mathcal{A}_i(t-w:t-1, :),
\mathcal{A}_i(t:t+w-1, :)
\right)
$$

Finally, the mixed structural change score is computed as:

$$
S_{\lambda,i}^{(t)}=
(1-\lambda)
\nu_i^{(t)}
+
\lambda
\nu_{\mathcal{A},i}^{(t)}
$$

Here, `lambda` controls the balance between local probability-path change and global self-distance-structure change.  
この `S_lambda,i^(t)` を用いることで、局所的な変化と大域的な構造変化の両方を考慮した境界候補を得る。

---

### 5. Evaluation / 評価

The learned representation is evaluated on music structure boundary detection and harmonic probing tasks.  
得られた表現は、楽曲構造境界検出および和声的プロービング課題によって評価する。これにより、提案表現が大域的な楽曲構造だけでなく、局所的な和声傾向の理解にも有効であるかを検証する。

For structure boundary detection, predicted boundary candidates are obtained from peaks of the structural change score:

$$
\hat{B}_i=
\left\{
t
\mid
S_{\lambda,i}^{(t)}
\text{ is a local peak}
\right\}
$$

The predicted boundaries are compared with annotated boundaries using tolerance-based precision, recall, and F-measure.  
予測された境界候補は、アノテーションされた境界と比較し、許容範囲つきの precision、recall、F-measure によって評価する。

For harmonic probing, the probability path is used as an input representation for predicting harmonic labels:

$$
\hat{y}_i^{(t)}=
f_{\mathrm{probe}}
\left(
\gamma_i^{(t)}
\right)
$$

Here, `f_probe` is a lightweight probe model such as logistic regression or MLP.  
ここで、`f_probe` はロジスティック回帰や MLP などの軽量なプローブモデルであり、`Gamma_i` が和声的情報をどの程度保持しているかを検証するために用いる。

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
