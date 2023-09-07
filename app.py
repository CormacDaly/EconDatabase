from flask import Flask, render_template
from dotenv import load_dotenv
import json
import os
import time    

app = Flask(__name__)

@app.route('/')
def index():
    name = "Cormac"
    return render_template('index.html',name=name)


@app.route('/grid_test')
def grid_test():
    return render_template('grid_test.html')


@app.route('/gdp_test')
def gdp_test():
    with open('fred_data.json', 'r') as f:
        fred_data = json.load(f)
        gdp = fred_data["GDP"][-10:]
        for entry in gdp:
            print(entry)
    return render_template('gdp_test.html', gdp=gdp)


@app.route('/chartjs_test')
def chartjs_test():
    return render_template('chartjs_test.html')
        

import os

if __name__ == '__main__':
    template_files = [os.path.join('templates', f) for f in os.listdir('templates') if f.endswith('.html')]
    app.run(debug=True, extra_files=template_files)

