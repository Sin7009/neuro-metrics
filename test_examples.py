#!/usr/bin/env python3
"""
Example usage of neuro-metrics library.

This script demonstrates all the main plotting functions with Sber styling.
"""

import sys
import os
import numpy as np
import pandas as pd

# Add the src directory to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import neuro_metrics as nm

def test_colors():
    """Test that colors are properly defined."""
    print("Testing color palette...")
    assert nm.SBER_GREEN == '#21A038'
    assert nm.SBER_BLUE == '#0E67D7'
    palette = nm.get_palette('primary')
    assert len(palette) == 6
    print(f"✓ Colors loaded: {palette}")
    print()

def test_line_plot():
    """Test line plot creation."""
    print("Testing line plot...")
    # Create sample data
    df = pd.DataFrame({
        'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'sales': [100, 120, 115, 140, 150, 145],
        'costs': [80, 85, 90, 95, 100, 98]
    })
    
    # Test with DataFrame and multiple y columns
    fig = nm.plot_line(df, x='month', y=['sales', 'costs'], 
                       title='Monthly Sales and Costs',
                       xlabel='Month', ylabel='Amount ($1000)',
                       save_path='/tmp/test_line.png')
    print("✓ Line plot created and saved to /tmp/test_line.png")
    print()

def test_bar_plot():
    """Test bar plot creation."""
    print("Testing bar plot...")
    # Test with dictionary
    data = {'Product A': 30, 'Product B': 45, 'Product C': 25, 'Product D': 50}
    fig = nm.plot_bar(data, title='Product Sales Distribution',
                      xlabel='Product', ylabel='Sales',
                      save_path='/tmp/test_bar.png')
    print("✓ Bar plot created and saved to /tmp/test_bar.png")
    print()

def test_scatter_plot():
    """Test scatter plot creation."""
    print("Testing scatter plot...")
    # Create sample data
    np.random.seed(42)
    df = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    fig = nm.plot_scatter(df, x='x', y='y', hue='category',
                          title='Scatter Plot with Categories',
                          xlabel='X Variable', ylabel='Y Variable',
                          save_path='/tmp/test_scatter.png')
    print("✓ Scatter plot created and saved to /tmp/test_scatter.png")
    print()

def test_heatmap():
    """Test heatmap creation."""
    print("Testing heatmap...")
    # Create correlation matrix
    np.random.seed(42)
    data = np.random.randn(10, 10)
    df = pd.DataFrame(data, 
                     columns=[f'Var{i+1}' for i in range(10)],
                     index=[f'Var{i+1}' for i in range(10)])
    corr = df.corr()
    
    fig = nm.plot_heatmap(corr, title='Correlation Matrix',
                          cmap='Greens', annot=False,
                          save_path='/tmp/test_heatmap.png')
    print("✓ Heatmap created and saved to /tmp/test_heatmap.png")
    print()

def test_pie_chart():
    """Test pie chart creation."""
    print("Testing pie chart...")
    data = {'Segment A': 30, 'Segment B': 25, 'Segment C': 20, 'Segment D': 25}
    fig = nm.plot_pie(data, title='Market Share Distribution',
                      save_path='/tmp/test_pie.png')
    print("✓ Pie chart created and saved to /tmp/test_pie.png")
    print()

def test_histogram():
    """Test histogram creation."""
    print("Testing histogram...")
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)
    
    fig = nm.plot_histogram(data, bins=30, 
                            title='Score Distribution',
                            xlabel='Score', ylabel='Frequency',
                            kde=True,
                            save_path='/tmp/test_histogram.png')
    print("✓ Histogram created and saved to /tmp/test_histogram.png")
    print()

def main():
    """Run all tests."""
    print("=" * 60)
    print("Testing neuro-metrics library")
    print("=" * 60)
    print()
    
    try:
        test_colors()
        test_line_plot()
        test_bar_plot()
        test_scatter_plot()
        test_heatmap()
        test_pie_chart()
        test_histogram()
        
        print("=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        print()
        print("Generated plots saved to /tmp/:")
        for f in os.listdir('/tmp'):
            if f.startswith('test_') and f.endswith('.png'):
                print(f"  - {f}")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
