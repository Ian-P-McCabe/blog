import plotly.graph_objects as go
import numpy as np

def generate_lab_3d_all_colors(df, figure_title, output_filename=None):
    # Parse the L*a*b values from the string format
    df[['L', 'a', 'b']] = df['L*a*b Value'].str.split(', ', expand=True).astype(float)

    # Create the 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=df['a'],        # a* axis (green-red)
        y=df['L'],        # L* axis (lightness)
        z=df['b'],        # b* axis (blue-yellow)
        mode='markers+text',
        text=df['Color Name'],
        hovertemplate=
            '<b>%{text}</b><br>' +
            'L*: %{y:.1f}<br>' +
            'a*: %{x:.1f}<br>' +
            'b*: %{z:.1f}<br>',
        marker=dict(
            size=7,
            color=['#' + hex.strip() for hex in df['Hex']],  # Use actual hex colors
            opacity=1.0
        ),
        textposition='top center',
        textfont=dict(
            size=8
        )
    )])

    # Update the layout
    fig.update_layout(
        template="plotly",
        title=figure_title,
        scene=dict(
            # TODO Adjust before publish
            aspectratio=dict(x=1, y=1, z=1),
            xaxis_title='a* (green to red)',
            yaxis_title='L* (black to white)',
            zaxis_title='b* (blue to yellow)',
            # Set appropriate ranges for each axis
            # Originally -128, 128
            xaxis=dict(range=[-128, 128]),
            # Originally [0, 100]
            yaxis=dict(range=[0, 100]),
            zaxis=dict(range=[-128, 128])
        ),
        showlegend=True,
        margin=dict(l=1, r=1, t=1, b=1)
    )

    # Add better camera angle
    fig.update_layout(scene_camera=dict(
        up=dict(x=0, y=1, z=0),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.5, y=1.5, z=1.5)
    ))

    # Show the plot
    fig.show()

    # Optionally save to HTML file
    if output_filename is not None:
        fig.write_html(output_filename + ".html")