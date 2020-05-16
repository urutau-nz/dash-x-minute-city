import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))



def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.A(
                                        html.Button("Overview", id="learn-more-button"),
                                        href="./overview",
                                    ),
                                    html.A(
                                        html.Button("Measuring Equity", id="learn-more-button"),
                                        href="./equity",
                                    ),
                                    html.A(
                                        html.Button("Recover", id="learn-more-button"),
                                        href="./recover",
                                    ),
                                    html.A(
                                        html.Button("Transformation", id="learn-more-button"),
                                        href="./transform",
                                    ),
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row buttons",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Resilience as access to essentials"),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P(
                                        ["\
                                    In ",
                                    html.A("Logan & Guikema (2020)", href="https://onlinelibrary.wiley.com/doi/full/10.1111/risa.13492",
                                        # style={'color':'white'}
                                        ),
                                    " we made the case for ''access to essential services'' being considered as a \
                                    pillar of community resilience.\
                                    This is a natural outcome based on the works of many in the planning and resilience communities."
                                    ],
                                    ),
                                    html.H6(
                                        ["Everyday services"], className="subtitle padded"
                                    ),
                                    html.P(
                                        ["\
                                    What am i referring to?"
                                    ],
                                    ),
                                    html.H6(
                                        ["Community capacity"], className="subtitle padded"
                                    ),
                                    html.P(
                                        ["\
                                    For example, Talen () points out that access to services is of utmost importance to planners.\
                                    We know that communities without access to everyday services will simply collapse.\
                                    Further, we know that access, especially equitable access, is critical for community cohesion and social capital.\
                                    These are characteristics integral to community resilience indicators such as those proposed by Cutter.."
                                    ],
                                    ),
                                    html.H6(
                                        ["Infrastructure functionality"], className="subtitle padded"
                                    ),
                                    html.P(
                                        ["\
                                    Thinking about resilience in this manner, neatly ties in the works of the engineering resilience communities,\
                                    who have focused primarily on infrastructure functionality.\
                                    This infrastructure has been the focus because of its traditional critical importance in supporting\
                                    everyday services.\
                                    However, if we focus on the outcomes that matter for communities, we can explore interventions that can\
                                    improve the resilience of communities, such as decentralization or infrastructure independence (e.g., solar panels or generators)."
                                    ],
                                    ),
                                    html.H6(
                                        ["Spatial dimension"], className="subtitle padded"
                                    ),
                                    html.P(
                                        ["\
                                    Finally, this conceptualization is spatially explicit, so resilience-enhancing decisions can be integrated into\
                                    planning."
                                    ],
                                    ),
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Performance", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=df_graph["Date"],
                                                    y=df_graph["Calibre Index Fund"],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Calibre Index Fund",
                                                ),
                                                go.Scatter(
                                                    x=df_graph["Date"],
                                                    y=df_graph[
                                                        "MSCI EAFE Index Fund (ETF)"
                                                    ],
                                                    line={"color": "#b5b5b5"},
                                                    mode="lines",
                                                    name="MSCI EAFE Index Fund (ETF)",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=700,
                                                height=200,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 30,
                                                    "l": 30,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        "2007-12-31",
                                                        "2018-03-06",
                                                    ],
                                                    "rangeselector": {
                                                        "buttons": [
                                                            {
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 5,
                                                                "label": "5Y",
                                                                "step": "year",
                                                            },
                                                            {
                                                                "count": 10,
                                                                "label": "10Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "label": "All",
                                                                "step": "all",
                                                            },
                                                        ]
                                                    },
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        18.6880162434,
                                                        278.431996757,
                                                    ],
                                                    "showline": True,
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "After-tax returns--updated quarterly as of 12/31/2017"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            html.Table(
                                                make_dash_table(df_after_tax),
                                                className="tiny-header",
                                            )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Recent investment returns"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(
                                        make_dash_table(df_recent_returns),
                                        className="tiny-header",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
