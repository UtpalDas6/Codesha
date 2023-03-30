import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def weather():
    city = request.form['city']
    api_key= "74ce3f1c73a3380ce3c1c7fb242baea8"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    #print(response)
    if response['cod'] != '404':
        weather = {
            'city': city.title(),
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        return render_template('index.html', weather=weather)
    else:
        return render_template('index.html', error='City not found :(')

if __name__ == '__main__':
    app.run(debug=True)
