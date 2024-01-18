from dashseo import htmlify
import dash
from dash import Dash, html

def test_html_inserted_in_app_index():
    app = Dash()
    app.layout = html.Div([
        html.H1("hello, world")
    ])
    assert 'hello, world' not in dash.dash._app_entry
    htmlify(app)
    assert 'hello, world' in dash.dash._app_entry

if __name__ == '__main__':
    test_html_inserted_in_app_index()