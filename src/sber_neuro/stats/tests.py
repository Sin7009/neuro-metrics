import numpy as np
from scipy import stats

def compare_groups(data_a, data_b, method='t-test'):
    """
    Compares two groups of data using statistical tests.

    Automatically checks for normality using the Shapiro-Wilk test.
    - If both groups are normally distributed, uses the independent T-test.
    - If either group is not normally distributed, uses the Mann-Whitney U test.

    Args:
        data_a (array-like): Data for group A.
        data_b (array-like): Data for group B.
        method (str): Default is 't-test'. This parameter is present for signature compatibility
                      but the actual test is determined by normality checks.

    Returns:
        dict: A dictionary containing:
            - 'p_value': float
            - 'significant': bool (True if p < 0.05)
            - 'message': str (Human-readable explanation)
    """
    # Convert to numpy arrays to handle lists/pandas series
    a = np.asarray(data_a)
    b = np.asarray(data_b)

    # Remove NaNs if any
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]

    # Check Normality
    # Shapiro-Wilk test: p < 0.05 implies NOT normal
    try:
        shapiro_a = stats.shapiro(a)
        shapiro_b = stats.shapiro(b)
        is_normal_a = shapiro_a.pvalue >= 0.05
        is_normal_b = shapiro_b.pvalue >= 0.05
    except ValueError:
        # Fallback if sample size is too small for shapiro or other issues
        # Usually requires N >= 3
        is_normal_a = False
        is_normal_b = False

    # Decide on test
    # If both are normal, use T-test
    if is_normal_a and is_normal_b:
        test_used = "T-test"
        stat_res = stats.ttest_ind(a, b)
        p_value = stat_res.pvalue
    else:
        test_used = "Mann-Whitney U test"
        stat_res = stats.mannwhitneyu(a, b)
        p_value = stat_res.pvalue

    significant = p_value < 0.05

    # Determine direction
    mean_a = np.mean(a)
    mean_b = np.mean(b)

    if significant:
        if mean_a > mean_b:
            direction = "Group A mean is higher."
        else:
            direction = "Group B mean is higher."
        msg_start = f"Significant difference found (p = {p_value:.4f})."
    else:
        direction = ""
        msg_start = f"No significant difference found (p = {p_value:.4f})."

    message = f"{msg_start} Used {test_used}. {direction}".strip()

    return {
        'p_value': float(p_value),
        'significant': bool(significant),
        'message': message
    }
