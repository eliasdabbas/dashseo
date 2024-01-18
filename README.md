# Dash SEO

A set of tools to make Dash apps SEO-friendly.

### Why?

Dash is renderd as a single page app, as a set of React components. The HTML representation is not available like a traditional page, and app content an be difficult to read by search engines. 

The solution is to convert the app's HTML components in the `layout` attribute to an HTML string, and include it in the app's source.

## Features

* Create the full HTML string of the app, to be easily read by crawlers and search engines.
* Does not convert `dcc` components (charts, dropdowns, date pickers, etc.) saving on performance because these components can be heavy without much content, especially charts.
* Title tag, and meta tags are already supported by Dash, and you can set these using default Dash.

## Example

`$ pip install dashseo`


```python
from dashseo import htmlify
from dash import Dash, html

app = Dash()
app.layout = html.Div([
    html.H1("Hello, world!")
])

# You only need to add this:
htmlify(app)

app.run()

```
## What just happened?

The `div` containing "Loading..." get an additional div, which is the full HTML of the app's `layout`. For the above app, it ends up like this:

```html:highlight={5-7}
<div id="react-entry-point">
    <div class="_dash-loading">
        Loading...
    </div>
    <div>
        <h1>hello, world</h1>
    </div>
</div>

```

## Limitations

The current solution works only for simple apps (not using pages).