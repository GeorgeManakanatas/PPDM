# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

app.layout = html.Div(id='Main', children=[
    html.H1(children='Parameter definition'),
    html.Div(id='mining', children=[
        html.H2(children='Data mining'),
        html.Label('Data mining method'),
        dcc.Dropdown(
            options=[
                {'label': 'Apriori', 'value': 'Apriori'}
            ],
            value=''
        ),
        html.Div([
            html.Label('Minimum support value'),
            dcc.Slider(
                min=0,
                max=99,
                marks={i: str(i) for i in range(1, 100)},
                value=30,
            ),
        ], style={'padding': '10px 0px', 'width': '100%', 'display': 'inline-block'}),

        html.Div([
            html.Label('Minimum confidence value'),
            dcc.Slider(
                min=0,
                max=99,
                marks={i: str(i) for i in range(1, 100)},
                value=90,
            ),
        ]),

    ]),

    html.Div(id='files', children=[
        html.H2(children='File / Output options'),
        html.Label('Data file path'),
        dcc.Input(id='data_folder', value='data/input/', type='text'),

        html.Label('Data file name'),
        dcc.Input(id='data_file', value='adult_dataset.txt', type='text'),

        html.Label('Temp folder location'),
        dcc.Input(id='temp_folder', value='temp/', type='text'),

        html.Label('Masked file name'),
        dcc.Input(id='masked_file', value='masked_file.csv', type='text'),

        html.Label('Anonymised file name'),
        dcc.Input(id='anon_file', value='anonym_file.csv', type='text'),

        html.Label('Data output path'),
        dcc.Input(id='data_output', value='data/output/', type='text'),

        html.Label('Save to file'),
        dcc.Checklist(
            options=[
                {'label': 'Save intermediate steps', 'value': True}
            ],
            value=[False]
        ),

    ]),

    html.Div(id='anonymisation', children=[
        html.H2(children='Anonymisation'),
        html.Label('Anonymisation method'),
        dcc.Dropdown(
            options=[
                {'label': 'k-anonymity', 'value': 'k-anonymity'}
            ],
            value=''
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
        html.Label('K-min selection'),
        dcc.Slider(
            min=0,
            max=19,
            marks={i: str(i) for i in range(1, 20)},
            value=5,
        ),
    ]),

    html.Div(id='masking', children=[
        html.H2(children='Masking'),
        html.Label('Masking method'),
        dcc.Dropdown(
            options=[
                {'label': 'Encrypt', 'value': 'encrypt'},
                {'label': 'Replace', 'value': 'replace'}
            ],
            value=''
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
    ]),

    html.Div(id='execution', children=[
        html.H2(children='Execution'),
        html.Button('Start', id='button'),
        html.Div(id='output-container-button',
                 children='Enter a value and press submit')
    ]),

], style={'width': '100%', 'display': 'inline-block'})


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('data_folder', 'value')])
def update_output(n_clicks, value):
    return ' The data folder is "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=False)
