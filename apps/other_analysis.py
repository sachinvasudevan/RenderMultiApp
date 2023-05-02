import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

df= pd.read_csv("C:/Users/sachi/Documents/sem2/DataVisualization/Individual/ShoppingMultipage/shopping_data.csv")
mall_name= df['shopping_mall'].unique()
payment = ["Credit Card", "Cash", "Debit Card"]
from app import app
#app = dash.Dash(__name__)

layout = html.Div([
    dbc.Container([
        dbc.Row([
            #Header span the whole row
            #className: Often used with CSS to style elements with common properties.
            dbc.Col(html.H1("Shopping Quantity and Payment Method Analysis", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/sales.jpg')
                ], width=4
            ),
            dbc.Col(
                [
                    dcc.RadioItems(df.month.unique(), id='mnth-choice', value='Jan', inline=True)
                ], width=6,
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(id='bar-fig',
                              figure=px.bar(df, x='payment_method', y='avg_quantity',color="gender",
                                            color_discrete_sequence=["red", "green"]))
                ], width=12
            )
        ])
    ]
)
])

@app.callback(
    Output('bar-fig', 'figure'),
    Input('mnth-choice', 'value')
)
def update_graph(value):
    dff = df[df.month==value]
    fig = px.bar(dff, x='payment_method', y='avg_quantity',color='gender',color_discrete_sequence=["red", "green"])
    fig.update_layout(plot_bgcolor='rgb(233, 238, 245)',
        paper_bgcolor='rgb(233, 238, 245)')
    return fig

#if __name__ == '__main__':
   # app.run_server(debug=True)