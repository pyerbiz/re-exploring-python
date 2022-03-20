import dash_core_components as dcc
import dash_html_components as html

# Connect to main app.py file
from app import app

# Connect to your app pages
from apps import global_sales, vgames
from dash.dependencies import Input, Output

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                dcc.Link("Video Games|", href="/apps/vgames"),
                dcc.Link("Other Products", href="/apps/global_sales"),
            ],
            className="row",
        ),
        html.Div(id="page-content", children=[]),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """_summary_

    Args:
        pathname (_type_): _description_

    Returns:
        _type_: _description_
    """
    if pathname == "/apps/vgames":
        return vgames.layout
    if pathname == "/apps/global_sales":
        return global_sales.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == "__main__":
    app.run_server(debug=False)
