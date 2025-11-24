#!/usr/bin/env python3
"""
Comprehensive examples demonstrating neuro-metrics capabilities.

This script shows real-world usage scenarios with Sber corporate styling.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import neuro_metrics as nm
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 70)
print("NEURO-METRICS LIBRARY DEMO")
print("Professional Visualization with Sber Corporate Styling")
print("=" * 70)
print()

# ============================================================================
# Example 1: Business Performance Dashboard
# ============================================================================
print("📊 Example 1: Business Performance Analysis")
print("-" * 70)

# Create business data
business_data = pd.DataFrame({
    'quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'revenue': [1200, 1450, 1380, 1650],
    'profit': [240, 290, 276, 330],
    'costs': [960, 1160, 1104, 1320]
})

print("Creating multi-line business performance chart...")
nm.plot_line(
    business_data, 
    x='quarter', 
    y=['revenue', 'profit', 'costs'],
    title='Quarterly Business Performance 2024',
    xlabel='Quarter',
    ylabel='Amount (Million RUB)',
    figsize=(12, 6),
    save_path='/tmp/example_business.png'
)
print("✓ Saved to /tmp/example_business.png")
print()

# ============================================================================
# Example 2: Product Comparison
# ============================================================================
print("📊 Example 2: Product Sales Comparison")
print("-" * 70)

products = {
    'SberPay': 3500,
    'SberBank Online': 8200,
    'SberSpasibo': 2100,
    'SberMarket': 1800,
    'SberPrime': 4200
}

print("Creating horizontal bar chart for product comparison...")
nm.plot_bar(
    products,
    title='Product Active Users (thousands)',
    xlabel='Users',
    horizontal=True,
    figsize=(10, 6),
    save_path='/tmp/example_products.png'
)
print("✓ Saved to /tmp/example_products.png")
print()

# ============================================================================
# Example 3: Customer Segmentation
# ============================================================================
print("📊 Example 3: Customer Segmentation Analysis")
print("-" * 70)

# Generate customer data
n_customers = 300
segments = np.random.choice(['Premium', 'Standard', 'Basic'], n_customers, p=[0.2, 0.5, 0.3])
customer_data = pd.DataFrame({
    'age': np.random.randint(18, 75, n_customers),
    'income': np.random.lognormal(11.5, 0.5, n_customers),
    'segment': segments
})

print("Creating scatter plot with customer segmentation...")
nm.plot_scatter(
    customer_data,
    x='age',
    y='income',
    hue='segment',
    title='Customer Segmentation by Age and Income',
    xlabel='Age (years)',
    ylabel='Annual Income (thousand RUB)',
    figsize=(12, 8),
    alpha=0.6,
    save_path='/tmp/example_segments.png'
)
print("✓ Saved to /tmp/example_segments.png")
print()

# ============================================================================
# Example 4: Market Share Analysis
# ============================================================================
print("📊 Example 4: Market Share Distribution")
print("-" * 70)

market_share = {
    'Sberbank': 35.2,
    'VTB': 18.5,
    'Gazprombank': 12.3,
    'Alfa-Bank': 9.8,
    'Others': 24.2
}

print("Creating pie chart for market share...")
nm.plot_pie(
    market_share,
    title='Russian Banking Market Share 2024',
    explode=[0.1, 0, 0, 0, 0],  # Highlight Sberbank
    figsize=(10, 10),
    save_path='/tmp/example_market.png'
)
print("✓ Saved to /tmp/example_market.png")
print()

# ============================================================================
# Example 5: Risk Correlation Matrix
# ============================================================================
print("📊 Example 5: Financial Risk Correlation Analysis")
print("-" * 70)

# Generate correlation data for financial metrics
metrics = ['Credit Risk', 'Market Risk', 'Operational Risk', 
           'Liquidity Risk', 'Reputational Risk']
n = len(metrics)
corr_data = np.random.rand(n, n)
# Make it symmetric
corr_data = (corr_data + corr_data.T) / 2
# Set diagonal to 1
np.fill_diagonal(corr_data, 1)

corr_df = pd.DataFrame(corr_data, columns=metrics, index=metrics)

print("Creating heatmap for risk correlations...")
nm.plot_heatmap(
    corr_df,
    title='Risk Factor Correlation Matrix',
    figsize=(10, 8),
    annot=True,
    fmt='.2f',
    cmap='RdYlGn',
    save_path='/tmp/example_risks.png'
)
print("✓ Saved to /tmp/example_risks.png")
print()

# ============================================================================
# Example 6: Transaction Volume Distribution
# ============================================================================
print("📊 Example 6: Transaction Volume Distribution")
print("-" * 70)

# Generate transaction data (log-normal distribution)
transactions = np.random.lognormal(7, 1.5, 5000)

print("Creating histogram with KDE for transaction volumes...")
nm.plot_histogram(
    transactions,
    bins=50,
    title='Daily Transaction Volume Distribution',
    xlabel='Transaction Amount (RUB)',
    ylabel='Number of Transactions',
    kde=True,
    figsize=(12, 6),
    save_path='/tmp/example_transactions.png'
)
print("✓ Saved to /tmp/example_transactions.png")
print()

# ============================================================================
# Example 7: Regional Performance
# ============================================================================
print("📊 Example 7: Regional Branch Performance")
print("-" * 70)

regions_df = pd.DataFrame({
    'region': ['Moscow', 'St. Petersburg', 'Kazan', 'Novosibirsk', 
               'Yekaterinburg', 'Nizhny Novgorod', 'Samara', 'Omsk'],
    'q1': [850, 620, 380, 340, 390, 310, 280, 240],
    'q2': [920, 680, 410, 370, 420, 340, 310, 260],
    'q3': [880, 650, 395, 355, 405, 325, 295, 255],
    'q4': [1050, 750, 450, 410, 470, 380, 350, 290]
})

print("Creating grouped bar chart for regional quarterly performance...")
nm.plot_bar(
    regions_df,
    x='region',
    y=['q1', 'q2', 'q3', 'q4'],
    title='Regional Branch Revenue by Quarter (Million RUB)',
    xlabel='Region',
    ylabel='Revenue',
    figsize=(14, 7),
    save_path='/tmp/example_regions.png'
)
print("✓ Saved to /tmp/example_regions.png")
print()

# ============================================================================
# Summary
# ============================================================================
print("=" * 70)
print("✓ All examples completed successfully!")
print("=" * 70)
print()
print("Generated visualizations:")
print("  1. /tmp/example_business.png      - Business performance line chart")
print("  2. /tmp/example_products.png      - Product comparison bar chart")
print("  3. /tmp/example_segments.png      - Customer segmentation scatter plot")
print("  4. /tmp/example_market.png        - Market share pie chart")
print("  5. /tmp/example_risks.png         - Risk correlation heatmap")
print("  6. /tmp/example_transactions.png  - Transaction volume histogram")
print("  7. /tmp/example_regions.png       - Regional performance grouped bars")
print()
print("All charts use Sber corporate colors and professional styling! 🎨")
print()
