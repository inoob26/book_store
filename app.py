from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '6\xabQ\x1f\xe8\xf3;\\,sW\x08\xb6\xff\xaecGO9\xadN[\xa7\xbf'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)