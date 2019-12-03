import plotly
import plotly.express as px
import json
from cleaning_data import data_clean

def mpg_plot():
    df = data_clean()
    fig = px.histogram(df,x='mpg',marginal="rug")
    fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def horse_plot():
    df = data_clean()
    fig = px.histogram(df,x='horsepower',marginal="rug")
    fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json