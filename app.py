# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    resilience,
    equity,
    recover,
    transform,
    comingsoon
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    url_base_pathname='/resilience-equity/',
)
server = app.server

app.title = 'Embedding equity into resilience'

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/resilience-equity/resilience":
        return resilience.create_layout(app)
    elif pathname == "/resilience-equity/equity":
        return equity.create_layout(app)
    elif pathname == "/resilience-equity/recover":
        return recover.create_layout(app)
    elif pathname == "/resilience-equity/transform":
        return transform.create_layout(app)
    elif pathname == "/resilience-equity/soon":
        return comingsoon.create_layout(app)
    elif pathname == "/resilience-equity/all":
        return (
            overview.create_layout(app),
            resilience.create_layout(app),
            equity.create_layout(app),
            recover.create_layout(app),
            transform.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(port=9006)
