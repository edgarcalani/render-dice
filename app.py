'''
Author: Edgar Calani 9sep2024
App web lanza dado Python Flask Html Javascript VSCode
Python 3.10.11 .venv
'''

from flask import Flask, render_template
import dice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    result = dice.roll_dice()
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
