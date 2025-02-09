import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("covid-dashboard/country_wise_latest.csv")
df.fillna(0, inplace=True)
df["Active Cases"] = df["Confirmed"] - df["Deaths"] - df["Recovered"]

# Initialize Dash app
app = dash.Dash(__name__)

# Create visualizations
fig_map = px.scatter_geo(
    df, locations="Country/Region", locationmode="country names",
    size="Confirmed", color="Deaths", hover_name="Country/Region",
    title="COVID-19 Cases by Country", template="plotly_dark"
)

fig_bar = px.bar(
    df.nlargest(10, "Confirmed"), x="Confirmed", y="Country/Region",
    orientation="h", title="Top 10 Countries with Most Cases", template="plotly_dark"
)

fig_pie = px.pie(
    df, values="Confirmed", names="WHO Region",
    title="COVID-19 Cases by WHO Region", template="plotly_dark"
)

# App Layout
app.layout = html.Div([
    html.H1("COVID-19 Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Div(f"Total Confirmed: {df['Confirmed'].sum():,}", style={"color": "white", "fontSize": "20px"}),
        html.Div(f"Total Deaths: {df['Deaths'].sum():,}", style={"color": "red", "fontSize": "20px"}),
        html.Div(f"Total Recovered: {df['Recovered'].sum():,}", style={"color": "green", "fontSize": "20px"}),
        html.Div(f"Total Active Cases: {df['Active Cases'].sum():,}", style={"color": "orange", "fontSize": "20px"}),
    ], style={"display": "flex", "justifyContent": "space-around", "backgroundColor": "#222", "padding": "10px"}),

    dcc.Graph(figure=fig_map),
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_pie),
], style={"backgroundColor": "#111", "color": "white", "padding": "20px"})

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
