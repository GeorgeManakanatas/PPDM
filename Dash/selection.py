# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Data mining method'),
    dcc.Dropdown(
        options=[
            {'label': 'Apriori', 'value': 'Apriori'}
        ],
        value=''
    ),

    html.Label('Minimum support value'),
    dcc.Slider(
        min=0,
        max=99,
        marks={i: str(i) for i in range(1, 100)},
        value=30,
    ),

    html.Label('Minimum confidence value'),
    dcc.Slider(
        min=0,
        max=99,
        marks={i: str(i) for i in range(1, 100)},
        value=90,
    ),

    html.Label('Anonymisation method'),
    dcc.Dropdown(
        options=[
            {'label': 'k-anonymity', 'value': 'k-anonymity'}
        ],
        value=''
    ),

    html.Label('Masking method'),
    dcc.RadioItems(
        options=[
            {'label': 'Encrypt', 'value': 'encrypt'},
            {'label': 'Replace', 'value': 'replace'}
        ],
        value='replace'
    ),

    html.Label('Save to file'),
    dcc.Checklist(
        options=[
            {'label': 'Save intermediate steps', 'value': True}
        ],
        value=[False]
    ),

    html.Label('Columns to mask'),
    dcc.Checklist(
        options=[
            {'label': '1', 'value': '1'},
            {'label': '2', 'value': '2'},
            {'label': '3', 'value': '3'},
            {'label': '4', 'value': '4'},
            {'label': '5', 'value': '5'}
        ],
        value=[]
    ),

    html.Label('Columns to anonymise'),
    dcc.Checklist(
        options=[
            {'label': '1', 'value': '1'},
            {'label': '2', 'value': '2'},
            {'label': '3', 'value': '3'},
            {'label': '4', 'value': '4'},
            {'label': '5', 'value': '5'}
        ],
        value=[]
    ),

    html.Label('Data file path'),
    dcc.Input(value='data/input/', type='text'),

    html.Label('Data file name'),
    dcc.Input(value='adult_dataset.txt', type='text'),

    html.Label('Temp folder location'),
    dcc.Input(id='Temp folder', value='temp/', type='text'),

    html.Label('Masked file name'),
    dcc.Input(value='masked_file.csv', type='text'),

    html.Label('Anonymised file name'),
    dcc.Input(value='anonym_file.csv', type='text'),

    html.Label('Data output path'),
    dcc.Input(value='data/output/', type='text'),

#    html.Label('Data output file name'),
#    dcc.Input(value='data/input/', type='text'),

    html.Label('K-min selection'),
    dcc.Slider(
        min=0,
        max=19,
        marks={i: str(i) for i in range(1, 20)},
        value=5,
    ),

    html.Button('Start', id='button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')

], style={'columnCount': 3})


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('Temp folder', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=False)
