from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('products.json', 'r', encoding='utf-8') as file:
        fridge_data = json.load(file)
    
    return render_template('vivod_H.html', fridge_data=fridge_data)

if __name__ == '__main__':
    app.run(debug=True)
