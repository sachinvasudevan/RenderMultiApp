# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:41:41 2023

@author: sachi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:00:41 2023

@author: sachi
"""

#import packages to create app
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

df= pd.read_csv("C:/Users/sachi/Documents/sem2/DataVisualization/Individual/ShoppingMultipage/shopping_data.csv")
mall_name= df['shopping_mall'].unique()
month_name= df['month'].unique()
gender= df['gender'].unique()
category_name= df['category'].unique()
payment_type= df['payment_method'].unique()
from app import app
#app = dash.Dash(__name__)

colors = {
    #background to rgb(233, 238, 245)
    'background': '#e9eef5',
    'text': '#1c1cbd'
}

layout=html.Div(style={'backgroundColor': colors['background']},children=[
    dbc.Container([
        dbc.Row([
            #Header span the whole row
            #className: Often used with CSS to style elements with common properties.
            dbc.Col(html.H1("Shopping Sales Price Analysis Dashboard",        
             style={
            'textAlign': 'center',
            'color': colors['text']}), 
            className="mb-5 mt-5")
        ]),
        html.Div([
            html.Div([
                html.Label('Select Shopping Mall:'),
                dcc.Dropdown(id='mall_dropdown',
                            options=[{'label': i, 'value': i}
                                    for i in mall_name],
                            value=mall_name,
                            multi=True
                )
            ],style={'width': '49%', 'display': 'inline-block'}),
            html.Div([
                html.Label('Gender'),
                dcc.Dropdown(id='gender_dropdown',
                            options=[{'label': i, 'value': i}
                                    for i in gender],
                            value=gender,
                            multi=True
                ),
                html.Label('Select Variable to display on the Graphs'),
                dcc.Dropdown(id='eur_y_dropdown',
                    options=[                    
                        {'label': 'Total Price', 'value': 'totalprice'},
                        {'label': 'Average Price', 'value': 'avg_price'},
                        {'label': 'Average Unit Price', 'value': 'avg_unitprice'}],
                    value='totalprice',
                )
            ],style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
        ]),
        html.Div([
            dcc.Graph(
                id='barchart'
            ),
            ],style={'width': '80%', 'margin-left': '10%','display': 'inline-block'}),
        html.Div([
            html.Div([
                dcc.Graph(
                        id='areachart'
                ),
            ],style={'width': '49%','display': 'inline-block'}),
            html.Div([
                dcc.Graph(
                    id='trendline'
                ),
            ],style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
            ]),
    ])
])

@app.callback(
    [Output(component_id='barchart', component_property='figure'),
    Output(component_id='areachart', component_property='figure'),
    Output(component_id='trendline', component_property='figure')],
    [Input(component_id='mall_dropdown', component_property='value'),
    Input(component_id='gender_dropdown', component_property='value'),
    Input(component_id='eur_y_dropdown', component_property='value')]
)
def update_graphs(selected_mall,gendervalue,eyvar):
    if not (selected_mall or gendervalue or eyvar):
        return dash.no_update
    barfig = px.bar(df, y=eyvar, x='category',animation_frame="invoice_date",
             # add text labels to bar
             text=eyvar, color='payment_method',
             hover_data=['totalprice'])

    areafig= px.area(df, x="invoice_date", y=eyvar, color="shopping_mall", line_group="category")

    linefig = px.box(data_frame=df, 
                x="shopping_mall",  y = df[eyvar] , color='payment_method',
                hover_data=['category','invoice_date'])
        
    return [barfig, areafig, linefig]

# needed only if running this as a single page app
#if __name__=='__main__':
    #app.run_server(debug=True, port=8000)
