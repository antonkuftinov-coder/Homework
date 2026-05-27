
from flask import Flask, render_template, jsonify, request, redirect
app = Flask(__name__)

state = {
    "hand": "empty"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/status')
def status():
   
    return jsonify(state)


@app.route('/toggle', methods=['POST'])
def toggle():
   
    if state["hand"] == "empty":
        state["hand"] = "holding"
    else:
        state["hand"] = "empty"
    return jsonify(state)


@app.route('/on')
def set_on():
    state["hand"] = "holding"
    return redirect('/')


@app.route('/off')
def set_off():
    state["hand"] = "empty"
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
