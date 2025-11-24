"""
Neuro-Metrics: Professional visualization library with Sber corporate styling.

This library provides one-liner functions to create beautiful, publication-ready
charts with Sber's corporate color palette and styling.

Quick Start
-----------
>>> import neuro_metrics as nm
>>> import pandas as pd

# Create a line plot
>>> df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 15, 25]})
>>> nm.plot_line(df, x='x', y='y', title='Sales Trend')

# Create a bar chart
>>> data = {'A': 30, 'B': 25, 'C': 45}
>>> nm.plot_bar(data, title='Distribution')

# Create a scatter plot
>>> nm.plot_scatter(df, x='x', y='y', title='Correlation')
"""

__version__ = "0.1.0"

# Import main plotting functions
from .plotting import (
    plot_line,
    plot_bar,
    plot_scatter,
    plot_heatmap,
    plot_pie,
    plot_histogram,
)

# Import color utilities
from .colors import (
    SBER_GREEN,
    SBER_BLUE,
    SBER_ORANGE,
    SBER_PURPLE,
    SBER_RED,
    SBER_YELLOW,
    get_palette,
    get_color,
)

__all__ = [
    # Plotting functions
    'plot_line',
    'plot_bar',
    'plot_scatter',
    'plot_heatmap',
    'plot_pie',
    'plot_histogram',
    # Color utilities
    'SBER_GREEN',
    'SBER_BLUE',
    'SBER_ORANGE',
    'SBER_PURPLE',
    'SBER_RED',
    'SBER_YELLOW',
    'get_palette',
    'get_color',
]
