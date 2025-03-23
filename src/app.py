from flask import Flask, render_template, request
import os
from weather import get_weather

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    city = request.form['city']
    unit = request.form['unit']
    units = "metric" if unit == "Celsius" else "imperial"
    unit_symbol = "°C" if unit == "Celsius" else "°F"
    
    weather_data = get_weather(city, units)
    
    if weather_data:
        return render_template('result.html', city=city, weather_data=weather_data, unit_symbol=unit_symbol)
    else:
        return render_template('result.html', city=city, weather_data=None)

if __name__ == '__main__':
    app.run(debug=True)