"""
Sber Corporate Color Palette

This module defines the official Sber corporate colors and provides
utility functions for working with the color palette.
"""

# Primary Sber Colors
SBER_GREEN = '#21A038'  # Main Sber brand color
SBER_DARK_GREEN = '#168A2C'  # Darker shade
SBER_LIGHT_GREEN = '#3BB54A'  # Lighter shade

# Secondary Colors
SBER_ORANGE = '#FF6B00'
SBER_BLUE = '#0E67D7'
SBER_PURPLE = '#7B4EA5'
SBER_RED = '#E31E24'
SBER_YELLOW = '#FFB800'

# Neutral Colors
SBER_DARK_GRAY = '#333333'
SBER_GRAY = '#707070'
SBER_LIGHT_GRAY = '#B8B8B8'
SBER_LIGHTER_GRAY = '#E6E6E6'
SBER_WHITE = '#FFFFFF'
SBER_BLACK = '#000000'

# Predefined color palettes for different chart types
PALETTE_PRIMARY = [
    SBER_GREEN,
    SBER_BLUE,
    SBER_ORANGE,
    SBER_PURPLE,
    SBER_YELLOW,
    SBER_RED,
]

PALETTE_SEQUENTIAL_GREEN = [
    '#E8F5E9',
    '#A5D6A7',
    '#66BB6A',
    '#43A047',
    '#2E7D32',
    '#1B5E20',
]

PALETTE_DIVERGING = [
    '#E31E24',
    '#FF6B00',
    '#FFB800',
    '#E6E6E6',
    '#3BB54A',
    '#21A038',
    '#168A2C',
]

PALETTE_CATEGORICAL = PALETTE_PRIMARY

# Gradient palettes
GRADIENT_GREEN = ['#E8F5E9', '#21A038', '#168A2C']
GRADIENT_BLUE = ['#E3F2FD', '#0E67D7', '#0D47A1']
GRADIENT_WARM = ['#FFE0B2', '#FF6B00', '#E31E24']


def get_palette(name='primary', n_colors=None):
    """
    Get a color palette by name.
    
    Parameters
    ----------
    name : str, optional
        Name of the palette. Options: 'primary', 'sequential', 'diverging',
        'categorical', 'gradient_green', 'gradient_blue', 'gradient_warm'.
        Default is 'primary'.
    n_colors : int, optional
        Number of colors to return. If None, returns all colors in the palette.
        If specified, interpolates or cycles through the palette.
    
    Returns
    -------
    list
        List of color hex codes.
    """
    palettes = {
        'primary': PALETTE_PRIMARY,
        'sequential': PALETTE_SEQUENTIAL_GREEN,
        'diverging': PALETTE_DIVERGING,
        'categorical': PALETTE_CATEGORICAL,
        'gradient_green': GRADIENT_GREEN,
        'gradient_blue': GRADIENT_BLUE,
        'gradient_warm': GRADIENT_WARM,
    }
    
    palette = palettes.get(name, PALETTE_PRIMARY)
    
    if n_colors is None:
        return palette
    
    if n_colors <= len(palette):
        return palette[:n_colors]
    else:
        # Cycle through palette if more colors needed
        return [palette[i % len(palette)] for i in range(n_colors)]


def get_color(index=0):
    """
    Get a single color from the primary palette by index.
    
    Parameters
    ----------
    index : int, optional
        Index of the color in the primary palette. Default is 0 (Sber green).
    
    Returns
    -------
    str
        Color hex code.
    """
    return PALETTE_PRIMARY[index % len(PALETTE_PRIMARY)]
