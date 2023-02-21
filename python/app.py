from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hail, Brother! Get the Flamer... the heavy Flamer"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
