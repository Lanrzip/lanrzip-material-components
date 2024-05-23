import lanrzip_material_components as lmc
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    lmc.LanrzipMaterialComponents(
        id='input',
        value='my-value',
        label='my-label'
    ),
    html.Div(id='output'),
    lmc.MuiButton(
        id='button',
        children='Click me',
        variant='contained',
    ),
    html.Div(id='output2'),

])


@callback(Output('output2', 'children'), Input('button', 'nClicks'))
def display_output2(nClicks):
    return 'You have entered {}'.format(nClicks)

@callback(Output('output', 'children'), Input('input', 'value'))
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
