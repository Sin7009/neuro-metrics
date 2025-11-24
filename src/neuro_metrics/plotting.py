"""
Professional visualization module with Sber corporate styling.

This module provides one-liner functions to create beautiful, publication-ready
charts with Sber's corporate color palette and styling.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional, Union, List, Tuple

try:
    from scipy import stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

from .colors import (
    SBER_GREEN, SBER_DARK_GRAY, SBER_LIGHT_GRAY, 
    get_palette, get_color
)


def _apply_sber_style(ax=None, title=None, xlabel=None, ylabel=None, 
                      grid=True, legend=True):
    """
    Apply Sber corporate styling to a matplotlib axes.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes, optional
        The axes to style. If None, uses current axes.
    title : str, optional
        Title for the plot.
    xlabel : str, optional
        Label for x-axis.
    ylabel : str, optional
        Label for y-axis.
    grid : bool, optional
        Whether to show grid. Default is True.
    legend : bool, optional
        Whether to show legend if applicable. Default is True.
    """
    if ax is None:
        ax = plt.gca()
    
    # Set title and labels with Sber styling
    if title:
        ax.set_title(title, fontsize=16, fontweight='bold', 
                    color=SBER_DARK_GRAY, pad=20)
    
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12, fontweight='600', 
                     color=SBER_DARK_GRAY)
    
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12, fontweight='600', 
                     color=SBER_DARK_GRAY)
    
    # Style the axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(SBER_LIGHT_GRAY)
    ax.spines['bottom'].set_color(SBER_LIGHT_GRAY)
    
    # Style ticks
    ax.tick_params(colors=SBER_DARK_GRAY, labelsize=10)
    
    # Grid styling
    if grid:
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, 
               color=SBER_LIGHT_GRAY)
        ax.set_axisbelow(True)
    
    # Legend styling
    if legend and ax.get_legend():
        legend = ax.legend(frameon=True, fancybox=True, shadow=False,
                          framealpha=0.9, edgecolor=SBER_LIGHT_GRAY)
        legend.get_frame().set_linewidth(0.5)


def plot_line(data: Union[pd.DataFrame, pd.Series, np.ndarray, list],
             x: Optional[Union[str, list, np.ndarray]] = None,
             y: Optional[Union[str, List[str]]] = None,
             title: Optional[str] = None,
             xlabel: Optional[str] = None,
             ylabel: Optional[str] = None,
             figsize: Tuple[int, int] = (10, 6),
             colors: Optional[List[str]] = None,
             legend: bool = True,
             save_path: Optional[str] = None):
    """
    Create a professional line plot with Sber styling.
    
    Parameters
    ----------
    data : DataFrame, Series, array, or list
        Data to plot. Can be a pandas DataFrame, Series, numpy array, or list.
    x : str, list, or array, optional
        X-axis data or column name if data is DataFrame.
    y : str or list of str, optional
        Y-axis data or column name(s) if data is DataFrame. 
        Can plot multiple lines if list is provided.
    title : str, optional
        Plot title.
    xlabel : str, optional
        X-axis label.
    ylabel : str, optional
        Y-axis label.
    figsize : tuple, optional
        Figure size (width, height). Default is (10, 6).
    colors : list of str, optional
        Custom colors. If None, uses Sber palette.
    legend : bool, optional
        Whether to show legend. Default is True.
    save_path : str, optional
        Path to save the figure. If None, displays the plot.
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure.
    
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 15, 25]})
    >>> plot_line(df, x='x', y='y', title='Sales Trend')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Handle different data types
    if isinstance(data, pd.DataFrame):
        if y is None:
            raise ValueError("y parameter required when data is DataFrame")
        
        if isinstance(y, str):
            y = [y]
        
        if colors is None:
            colors = get_palette('primary', len(y))
        
        for i, col in enumerate(y):
            if x is not None:
                ax.plot(data[x], data[col], label=col, 
                       color=colors[i % len(colors)], linewidth=2.5)
            else:
                ax.plot(data[col], label=col, 
                       color=colors[i % len(colors)], linewidth=2.5)
    
    elif isinstance(data, pd.Series):
        color = colors[0] if colors else SBER_GREEN
        if x is not None:
            ax.plot(x, data, color=color, linewidth=2.5, label=data.name)
        else:
            ax.plot(data, color=color, linewidth=2.5, label=data.name)
    
    else:  # numpy array or list
        color = colors[0] if colors else SBER_GREEN
        if x is not None:
            ax.plot(x, data, color=color, linewidth=2.5)
        else:
            ax.plot(data, color=color, linewidth=2.5)
    
    _apply_sber_style(ax, title, xlabel, ylabel, legend=legend)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    
    return fig


def plot_bar(data: Union[pd.DataFrame, pd.Series, dict, list],
            x: Optional[Union[str, list]] = None,
            y: Optional[Union[str, List[str]]] = None,
            title: Optional[str] = None,
            xlabel: Optional[str] = None,
            ylabel: Optional[str] = None,
            figsize: Tuple[int, int] = (10, 6),
            colors: Optional[List[str]] = None,
            horizontal: bool = False,
            legend: bool = True,
            save_path: Optional[str] = None):
    """
    Create a professional bar chart with Sber styling.
    
    Parameters
    ----------
    data : DataFrame, Series, dict, or list
        Data to plot.
    x : str or list, optional
        X-axis data or column name.
    y : str or list of str, optional
        Y-axis data or column name(s). Can plot grouped bars if list.
    title : str, optional
        Plot title.
    xlabel : str, optional
        X-axis label.
    ylabel : str, optional
        Y-axis label.
    figsize : tuple, optional
        Figure size. Default is (10, 6).
    colors : list of str, optional
        Custom colors. If None, uses Sber palette.
    horizontal : bool, optional
        Create horizontal bar chart. Default is False.
    legend : bool, optional
        Whether to show legend. Default is True.
    save_path : str, optional
        Path to save the figure.
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure.
    
    Examples
    --------
    >>> data = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 15]}
    >>> plot_bar(data, x='Category', y='Values', title='Sales by Category')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Handle different data types
    if isinstance(data, pd.DataFrame):
        if y is None:
            raise ValueError("y parameter required when data is DataFrame")
        
        if isinstance(y, str):
            y = [y]
        
        if colors is None:
            colors = get_palette('primary', len(y))
        
        if x is not None:
            x_data = data[x]
        else:
            x_data = data.index
        
        width = 0.8 / len(y)
        positions = np.arange(len(x_data))
        
        for i, col in enumerate(y):
            offset = width * (i - len(y)/2 + 0.5)
            if horizontal:
                ax.barh(positions + offset, data[col], width, 
                       label=col, color=colors[i % len(colors)])
            else:
                ax.bar(positions + offset, data[col], width, 
                      label=col, color=colors[i % len(colors)])
        
        if horizontal:
            ax.set_yticks(positions)
            ax.set_yticklabels(x_data)
        else:
            ax.set_xticks(positions)
            ax.set_xticklabels(x_data, rotation=45 if len(x_data) > 5 else 0)
    
    elif isinstance(data, pd.Series):
        color = colors[0] if colors else SBER_GREEN
        if horizontal:
            ax.barh(range(len(data)), data.values, color=color)
            ax.set_yticks(range(len(data)))
            ax.set_yticklabels(data.index)
        else:
            ax.bar(range(len(data)), data.values, color=color)
            ax.set_xticks(range(len(data)))
            ax.set_xticklabels(data.index, 
                             rotation=45 if len(data) > 5 else 0)
    
    elif isinstance(data, dict):
        color = colors[0] if colors else SBER_GREEN
        keys = list(data.keys()) if x is None else x
        values = list(data.values()) if y is None else [data[k] for k in y]
        
        if horizontal:
            ax.barh(range(len(keys)), values, color=color)
            ax.set_yticks(range(len(keys)))
            ax.set_yticklabels(keys)
        else:
            ax.bar(range(len(keys)), values, color=color)
            ax.set_xticks(range(len(keys)))
            ax.set_xticklabels(keys, rotation=45 if len(keys) > 5 else 0)
    
    else:  # list
        color = colors[0] if colors else SBER_GREEN
        if horizontal:
            ax.barh(range(len(data)), data, color=color)
        else:
            ax.bar(range(len(data)), data, color=color)
    
    _apply_sber_style(ax, title, xlabel, ylabel, legend=legend)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    
    return fig


def plot_scatter(data: Union[pd.DataFrame, dict] = None,
                x: Optional[Union[str, list, np.ndarray]] = None,
                y: Optional[Union[str, list, np.ndarray]] = None,
                hue: Optional[str] = None,
                size: Optional[Union[str, float]] = None,
                title: Optional[str] = None,
                xlabel: Optional[str] = None,
                ylabel: Optional[str] = None,
                figsize: Tuple[int, int] = (10, 6),
                colors: Optional[List[str]] = None,
                alpha: float = 0.7,
                save_path: Optional[str] = None):
    """
    Create a professional scatter plot with Sber styling.
    
    Parameters
    ----------
    data : DataFrame or dict, optional
        Data to plot.
    x : str, list, or array
        X-axis data or column name.
    y : str, list, or array
        Y-axis data or column name.
    hue : str, optional
        Column name for color grouping (only for DataFrame).
    size : str or float, optional
        Column name for size variation or fixed size.
    title : str, optional
        Plot title.
    xlabel : str, optional
        X-axis label.
    ylabel : str, optional
        Y-axis label.
    figsize : tuple, optional
        Figure size. Default is (10, 6).
    colors : list of str, optional
        Custom colors. If None, uses Sber palette.
    alpha : float, optional
        Point transparency. Default is 0.7.
    save_path : str, optional
        Path to save the figure.
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure.
    
    Examples
    --------
    >>> df = pd.DataFrame({'x': [1,2,3,4], 'y': [2,4,3,5]})
    >>> plot_scatter(df, x='x', y='y', title='Correlation Plot')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if colors is None:
        colors = get_palette('primary')
    
    if isinstance(data, pd.DataFrame):
        x_data = data[x] if isinstance(x, str) else x
        y_data = data[y] if isinstance(y, str) else y
        
        if hue is not None:
            groups = data[hue].unique()
            for i, group in enumerate(groups):
                mask = data[hue] == group
                s = size if isinstance(size, (int, float)) else 100
                ax.scatter(data[x][mask], data[y][mask], 
                          label=group, color=colors[i % len(colors)],
                          s=s, alpha=alpha)
        else:
            s = size if isinstance(size, (int, float)) else 100
            ax.scatter(x_data, y_data, color=colors[0], s=s, alpha=alpha)
    else:
        s = size if isinstance(size, (int, float)) else 100
        ax.scatter(x, y, color=colors[0], s=s, alpha=alpha)
    
    _apply_sber_style(ax, title, xlabel, ylabel, legend=(hue is not None))
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    
    return fig


def plot_heatmap(data: Union[pd.DataFrame, np.ndarray],
                title: Optional[str] = None,
                xlabel: Optional[str] = None,
                ylabel: Optional[str] = None,
                figsize: Tuple[int, int] = (10, 8),
                cmap: str = 'Greens',
                annot: bool = True,
                fmt: str = '.2f',
                cbar_label: Optional[str] = None,
                save_path: Optional[str] = None):
    """
    Create a professional heatmap with Sber styling.
    
    Parameters
    ----------
    data : DataFrame or array
        Data to plot as heatmap.
    title : str, optional
        Plot title.
    xlabel : str, optional
        X-axis label.
    ylabel : str, optional
        Y-axis label.
    figsize : tuple, optional
        Figure size. Default is (10, 8).
    cmap : str, optional
        Colormap name. Default is 'Greens' (Sber style).
    annot : bool, optional
        Annotate cells with values. Default is True.
    fmt : str, optional
        String formatting for annotations. Default is '.2f'.
    cbar_label : str, optional
        Label for colorbar.
    save_path : str, optional
        Path to save the figure.
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure.
    
    Examples
    --------
    >>> corr_matrix = df.corr()
    >>> plot_heatmap(corr_matrix, title='Correlation Matrix')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create heatmap with seaborn
    sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap, 
                cbar_kws={'label': cbar_label} if cbar_label else {},
                linewidths=0.5, linecolor=SBER_LIGHT_GRAY, ax=ax)
    
    # Apply Sber styling
    if title:
        ax.set_title(title, fontsize=16, fontweight='bold', 
                    color=SBER_DARK_GRAY, pad=20)
    
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12, fontweight='600', 
                     color=SBER_DARK_GRAY)
    
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12, fontweight='600', 
                     color=SBER_DARK_GRAY)
    
    ax.tick_params(colors=SBER_DARK_GRAY, labelsize=10)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    
    return fig


def plot_pie(data: Union[pd.Series, dict, list],
            labels: Optional[list] = None,
            title: Optional[str] = None,
            figsize: Tuple[int, int] = (10, 8),
            colors: Optional[List[str]] = None,
            autopct: str = '%1.1f%%',
            explode: Optional[list] = None,
            save_path: Optional[str] = None):
    """
    Create a professional pie chart with Sber styling.
    
    Parameters
    ----------
    data : Series, dict, or list
        Data to plot. Values should sum to represent proportions.
    labels : list, optional
        Labels for each slice. If data is Series or dict, uses keys.
    title : str, optional
        Plot title.
    figsize : tuple, optional
        Figure size. Default is (10, 8).
    colors : list of str, optional
        Custom colors. If None, uses Sber palette.
    autopct : str, optional
        Format string for percentage labels. Default is '%1.1f%%'.
    explode : list, optional
        Fraction to offset each slice.
    save_path : str, optional
        Path to save the figure.
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure.
    
    Examples
    --------
    >>> data = {'A': 30, 'B': 25, 'C': 45}
    >>> plot_pie(data, title='Market Share')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if colors is None:
        colors = get_palette('primary')
    
    # Handle different data types
    if isinstance(data, pd.Series):
        values = data.values
        labels = labels if labels else data.index.tolist()
    elif isinstance(data, dict):
        labels = labels if labels else list(data.keys())
        values = list(data.values())
    else:
        values = data
        labels = labels if labels else [f'Category {i+1}' for i in range(len(data))]
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(values, labels=labels, colors=colors,
                                       autopct=autopct, explode=explode,
                                       startangle=90, textprops={'color': SBER_DARK_GRAY})
    
    # Style the percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    # Style labels
    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight('600')
    
    if title:
        ax.set_title(title, fontsize=16, fontweight='bold', 
                    color=SBER_DARK_GRAY, pad=20)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    
    return fig


def plot_histogram(data: Union[pd.Series, np.ndarray, list],
                  bins: int = 30,
                  title: Optional[str] = None,
                  xlabel: Optional[str] = None,
                  ylabel: Optional[str] = 'Frequency',
                  figsize: Tuple[int, int] = (10, 6),
                  color: Optional[str] = None,
                  kde: bool = True,
                  save_path: Optional[str] = None):
    """
    Create a professional histogram with optional KDE with Sber styling.
    
    Parameters
    ----------
    data : Series, array, or list
        Data to plot.
    bins : int, optional
        Number of bins. Default is 30.
    title : str, optional
        Plot title.
    xlabel : str, optional
        X-axis label.
    ylabel : str, optional
        Y-axis label. Default is 'Frequency'.
    figsize : tuple, optional
        Figure size. Default is (10, 6).
    color : str, optional
        Bar color. If None, uses Sber green.
    kde : bool, optional
        Overlay kernel density estimate. Default is True.
    save_path : str, optional
        Path to save the figure.
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure.
    
    Examples
    --------
    >>> data = np.random.normal(100, 15, 1000)
    >>> plot_histogram(data, title='Score Distribution')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if color is None:
        color = SBER_GREEN
    
    # Convert to numpy array if needed
    if isinstance(data, pd.Series):
        data_array = data.values
    else:
        data_array = np.array(data)
    
    # Create histogram
    n, bins_arr, patches = ax.hist(data_array, bins=bins, color=color, 
                                     alpha=0.7, edgecolor=SBER_DARK_GRAY)
    
    # Add KDE if requested
    if kde:
        if not HAS_SCIPY:
            raise ImportError(
                "scipy is required for KDE plotting. "
                "Install it with: pip install scipy"
            )
        density = stats.gaussian_kde(data_array)
        xs = np.linspace(data_array.min(), data_array.max(), 200)
        # Scale KDE to match histogram
        density_values = density(xs) * len(data_array) * (bins_arr[1] - bins_arr[0])
        ax.plot(xs, density_values, color=SBER_DARK_GRAY, linewidth=2.5, 
               label='KDE')
        ax.legend()
    
    _apply_sber_style(ax, title, xlabel, ylabel, legend=kde)
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
    
    return fig
