from pathlib import Path

import dash
import dash_html_components as html
import flask

HERE = Path(__file__).parent

app = dash.Dash()

app.layout = html.A(html.Button("report"), href="/get_report", target="_blank")


@app.server.route("/get_report")
def get_report():
    return flask.send_from_directory(HERE, "report.html")


if __name__ == "__main__":
    app.run_server(debug=True)
