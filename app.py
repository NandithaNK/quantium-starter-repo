import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Initializing Dash application
app = dash.Dash(__name__)

# Reading data from CSV file
df = pd.read_csv("Quantium Task 2.csv")

# Extracting unique regions from the data and converting them to a list called regions.
regions = df['region'].unique().tolist()
# this is how all the regions are detected.
# Inserting "All" option at the top of the regions radio buttons
regions.insert(0, "All")

# Setting default region to "All"
default_region = regions[0]

# Creating initial line graph
fig = px.line(df, x="date", y="Sales", title=f"Sales Over Time - {default_region}")


# Defining Dash app layout
app.layout = html.Div([
    html.H1(children="Sales of Pink Morsel Over Time", style={"padding": "20px", "color": "White"}),
    html.Div("Choose the region you want the sales data of:", style={"background-color": "#2C5D63", "color": "White", "font-size": "20px", "padding": "20px"}),

    # Radio button component with inline CSS
    dcc.RadioItems(
        id="region-radio",
        options=[{"label": region, "value": region} for region in regions],
        value=default_region,
        labelStyle={"display": "block"},
        style={"font-size": "18px", "background-color": "#2C5D63", "color": "White", "padding": "20px"},
    ),

    # Graph component to display the sales data
    dcc.Graph(id="example-graph", figure=fig),
], style={"height": "100%", "width": "100%", "position": "absolute", "background-color": "#283739"})

# Define callback function to update the graph based on selected region
@app.callback(
    Output("example-graph", "figure"),
    [Input("region-radio", "value")],
)
def update_graph(selected_region):
    # Filter data based on selected region
    df_filtered = df if selected_region == "All" else df[df["region"] == selected_region]

    # Update graph title based on selected region
    title = "Sales Over Time - All Regions" if selected_region == "All" else f"Sales Over Time - {selected_region}"

    # Update graph figure with filtered data and updated title
    updated_fig = px.line(df_filtered, x="date", y="Sales", title=title)

    # Apply custom background color to the area around the line
    updated_fig.update_layout(paper_bgcolor="#A9C52F")

    # Maintain original background colors for the graph area
    updated_fig.update_layout(plot_bgcolor="#F7EEBB")

    return updated_fig

if __name__ == "__main__":
    app.run_server(debug=True)
