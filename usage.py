import lanrzip_material_components as lmc
from dash import Dash, callback, html, Input, Output, State

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
        # disabled=True
    ),
    lmc.MuiTextField(
        id='text-field',
        value='my-value',
        label='my-label'
    ),
    html.Div(id='test-output'),

])


@callback(
    Output('test-output', 'children'),
    Input('button', 'nClicks'),
    State('text-field', 'value')
)
def display_output2(nClicks, textValue):
    return f"Button clicked {nClicks} times, text field value: {textValue}"

@callback(Output('output', 'children'), Input('input', 'value'))
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
