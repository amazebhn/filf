import time
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def redir():
    return redirect(url_for('get_current_time'))

@app.route('/time')
def get_current_time():
    return jsonify({'time': time.time()})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)