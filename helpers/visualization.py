import dash
from dash import dcc, html
import plotly.graph_objects as go

def create_dash_app(flask_app):
    """Creates Dash app with properly aligned and styled pie charts."""
    dash_app = dash.Dash(
        __name__,
        server=flask_app,
        routes_pathname_prefix='/visualization/'
    )

    # Sample Data for Pie Charts
    labels = ["Process A", "Process B", "Process C"]
    values1 = [30, 50, 20]
    values2 = [25, 35, 40]
    values3 = [40, 30, 30]

    # Dash Layout with Flexbox for Horizontal Alignment
    dash_app.layout = html.Div([
        html.H3("System Process Analysis", style={'textAlign': 'center', 'color': 'black'}),

        html.Div([
            html.Div([
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Pie(
                            labels=labels, values=values1, hole=0.3,
                            pull=[0.02, 0.03, 0.04],
                            marker=dict(colors=['#FF9999', '#66B3FF', '#99FF99'])
                        )],
                        layout=go.Layout(title="CPU Usage")
                    )
                )
            ], style={
                'flex': '1', 'padding': '5px',
                'border': '1px solid black',  # Decreased border width
                'border-radius': '8px',
                'background-color': '#222',
                'margin': '5px', 'textAlign': 'center'
            }),

            html.Div([
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Pie(
                            labels=labels, values=values2, hole=0.3,
                            pull=[0.02, 0.03, 0.04],
                            marker=dict(colors=['#FFD700', '#C71585', '#20B2AA'])
                        )],
                        layout=go.Layout(title="Memory Usage")
                    )
                )
            ], style={
                'flex': '1', 'padding': '5px',
                'border': '1px solid black',  # Decreased border width
                'border-radius': '8px',
                'background-color': '#222',
                'margin': '5px', 'textAlign': 'center'
            }),

            html.Div([
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Pie(
                            labels=labels, values=values3, hole=0.3,
                            pull=[0.02, 0.03, 0.04],
                            marker=dict(colors=['#8A2BE2', '#FF4500', '#228B22'])
                        )],
                        layout=go.Layout(title="Disk Space Usage")
                    )
                )
            ], style={
                'flex': '1', 'padding': '5px',
                'border': '1px solid black',  # Decreased border width
                'border-radius': '8px',
                'background-color': '#222',
                'margin': '5px', 'textAlign': 'center'
            }),
        ], style={
            'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center',
            'padding': '10px'
        })
    ])

    return dash_app