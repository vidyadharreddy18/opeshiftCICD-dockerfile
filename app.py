import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello there!!! You are awesome"
    
@app.route('/about')
def about():
    return 'Test for the openShift CICD'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
