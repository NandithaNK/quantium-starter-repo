import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

#initializing Dash application
app = dash.Dash(__name__)

#reading data from csv
df = pd.read_csv("Quantium Task 2.csv")

#extracting all the unique regions from the data and converting them to a list called regions.
regions = df['region'].unique().tolist()
regions.insert(0, "All") #inserting the all option at the start and making that the default value
default_region = regions[0]

#creating the line graph
fig = px.line(df, x="date", y="Sales", title=f"Sales Over Time - {default_region}")

#making the dash layout
app.layout = html.Div([
    html.H1(children="Sales of Pink Morsel Over Time", style={"padding": "20px", "color": "White"}),
    html.Div("Choose the region you want the sales data of:", style={"background-color": "#2C5D63", "color": "White", "font-size": "20px", "padding": "20px"}),

    #creates radio button with inline css
    dcc.RadioItems(
        id="region-radio",
        options=[{"label": region, "value": region} for region in regions],
        value=default_region,
        labelStyle={"display": "block"},
        style={"font-size": "18px", "background-color": "#2C5D63", "color": "White", "padding": "20px"},
    ),

    #graph to display the sales
    dcc.Graph(id="example-graph", figure=fig),
], style={"height": "100%", "width": "100%", "position": "absolute", "background-color": "#283739"})

#define callback function to update the graph based on selected region
@app.callback(
    Output("example-graph", "figure"),
    [Input("region-radio", "value")],
)
def update_graph(selected_region):
    #filtering the data based on the selected region and updating the graph title too
    df_filtered = df if selected_region == "All" else df[df["region"] == selected_region]
    title = "Sales Over Time - All Regions" if selected_region == "All" else f"Sales Over Time - {selected_region}"
    updated_fig = px.line(df_filtered, x="date", y="Sales", title=title) #updating the graph

    #Applying the background colours
    updated_fig.update_layout(paper_bgcolor="#A9C52F")
    updated_fig.update_layout(plot_bgcolor="#F7EEBB")

    return updated_fig

if __name__ == "__main__":
    app.run_server(debug=True)
