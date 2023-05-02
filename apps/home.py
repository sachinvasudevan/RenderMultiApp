# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:05:12 2023

@author: sachi
"""

import dash
from dash import html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

from app import app

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            #Header span the whole row
            #className: Often used with CSS to style elements with common properties.
            dbc.Col(html.H1("Welcome to the Turkey's Customer Shopping Data Dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This app shows shopping information from 10 different shopping malls in Istanbul, Turkey between 2021 and 2023. '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of two main pages: Price Analysis, which gives an overview of the overall shopping price trends based on Average Unit Price, Total price etc on Daily and Monthly basis, '
                                     'Other, which gives an overview of the purchase quantity')
                    , className="mb-5")
        ]),

        dbc.Row([
            # 2 columns of width 6 with a border
            dbc.Col(dbc.Card(children=[html.H3(children='Go to the original Gapminder dataset for more data',
                                               className="text-center"),
                                       dbc.Button("Shoppin Dataset",
                                                  href="https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/sachinvasudevan/RenderMultiApp.git",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

        ], className="mb-5"),
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url('Sales.jpeg')), 
            width={"size": 6, "offset": 4})
        ]),
        html.A("This is a great icon representing the customer shopping",
               href="https://pngtree.com/freepng/shopping_521474.html")

    ])

])

# needed only if running this as a single page app
#if __name__ == '__main__':
 #   app.run_server(port=8098,debug=True)