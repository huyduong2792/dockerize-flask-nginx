# Importing Flask Python micro web framework
from flask import Flask, render_template
app = Flask(__name__)
# this is a Flask application route
@app.route("/")
# this is a FLask application function
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)