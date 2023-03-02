import socket

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index_ip():
    if request.method == "POST":
        url_1 = request.form['url']
        clear_url = url_1[8:-1]
        ip = socket.gethostbyname(clear_url)
        return render_template('show_ip.html', ip=ip)
    return render_template('index.html')


@app.route('/show_ip')
def show_ip():
    return render_template('show_ip.html')


if __name__ == "__main__":
    app.run(debug=True)
