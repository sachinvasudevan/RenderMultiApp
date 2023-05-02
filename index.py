# -*- coding: utf-8 -*-
"""
Created on Tue May  2 00:21:26 2023

@author: sachi
"""

from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
# from app import server
from app import app
# import all pages in the app
from apps import other_analysis, price_analysis, home
server= app.server
# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Price", href="/price_analysis"),
        dbc.DropdownMenuItem("Other", href="/other_analysis"),
    ],
    nav = True,
    in_navbar = True,
    label = "View Pages",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/shop.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Customer Shopping Analysis Dashboard- Turkey", className="ml-2")),
                    ],
                    align="center",
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/other_analysis':
        return other_analysis.layout
    elif pathname == '/price_analysis':
        return price_analysis.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(port = 8079, debug=True)
