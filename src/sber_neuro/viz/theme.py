import plotly.io as pio
import plotly.graph_objects as go

def apply_sber_theme():
    """
    Registers and sets the 'sber_corporate' Plotly theme with Sberbank corporate colors.
    """

    # Color Palette
    colors = [
        "rgb(0, 112, 59)",   # Primary 1
        "rgb(66, 149, 56)",  # Primary 2
        "rgb(124, 193, 68)", # Primary 3
        "rgb(214, 223, 61)", # Secondary 1
        "rgb(216, 223, 126)" # Secondary 2
    ]

    background_color = "rgb(252, 252, 249)"
    grid_color = "rgb(220, 220, 220)" # Subtle gray
    font_family = "Arial"
    font_size = 14

    # Define the template
    sber_template = go.layout.Template(
        layout=go.Layout(
            # Backgrounds
            paper_bgcolor=background_color,
            plot_bgcolor=background_color,

            # Fonts
            font=dict(
                family=font_family,
                size=font_size
            ),

            # Colorway (for sequential colors in plots)
            colorway=colors,

            # Axes
            xaxis=dict(
                gridcolor=grid_color,
                zerolinecolor=grid_color,
            ),
            yaxis=dict(
                gridcolor=grid_color,
                zerolinecolor=grid_color,
            ),

            # Title
            title=dict(
                font=dict(
                    family=font_family,
                    size=font_size + 4 # Slightly larger for title
                )
            )
        )
    )

    # Register the template
    pio.templates["sber_corporate"] = sber_template

    # Set as default
    pio.templates.default = "sber_corporate"
