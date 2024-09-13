from flask import Flask, render_template, request
from core import getAirQuality, getLocation
import os
from dotenv import load_dotenv

app = Flask(__name__, template_folder='templates', static_url_path='/static')

load_dotenv()

API_KEY = os.getenv('API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize the variables with None or a default value
    city = None
    location = None
    air_quality = None

    if request.method == 'POST':
        city = request.form.get('search_bar')  # Safely get the form data
        if city:
            location = getLocation(city)
            air_quality = getAirQuality(city)
    
    # Pass 'city', 'location', and 'air_quality' to the template
    return render_template('index.html', city=city, location=location, air_quality=air_quality)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
