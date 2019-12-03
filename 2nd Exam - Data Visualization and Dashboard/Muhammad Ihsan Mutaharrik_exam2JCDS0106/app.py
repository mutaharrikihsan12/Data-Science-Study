from flask import Flask,render_template
from cleaning_data import data_clean
from stats import horse_data,irit_data
from plots import horse_plot,mpg_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data_clean().head()
    return render_template('table_data.html' , data=data)

@app.route('/stats')
def stats():
    horsepower = horse_data()
    irit = irit_data()
    return render_template('stats.html' , data1=horsepower ,data2=irit)

@app.route('/plots')
def fig_plots():
    plot1 = mpg_plot()
    plot2 = horse_plot()
    return render_template('plots.html' , data=[plot1,plot2])

if __name__ == '__main__':
    app.run(debug=True, port=3333)