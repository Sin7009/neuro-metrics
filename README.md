# sber-neuro-metrics

## Mission
Standardizing neuro-data analysis and visualization across the laboratory.

## Key Features

*   **One-line Sber-branded plots (Standard Compliance)**
    Enforces corporate identity guidelines automatically, ensuring consistent visual communication.

*   **Automated statistical decision making (Error reduction)**
    Dynamically selects appropriate statistical tests (T-test vs. Mann-Whitney) based on data distribution checks.

*   **Unified data loading (Time saving)**
    Streamlines access to experimental data structures and common file formats.

## Quick Start

### Installation

Install the project using `uv`:

```bash
uv pip install sber-neuro-metrics
```

### Usage

```python
from sber_neuro.viz.theme import apply_sber_theme
import plotly.express as px
import pandas as pd

apply_sber_theme()
data = pd.read_csv("experiment_data.csv")
px.line(data, title="Neural Response").show()
```
