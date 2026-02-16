from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running on Azure 🚀"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/api/data")
def data():
    return {"message": "Hello from Flask API", "data": [1, 2, 3]}

if __name__ == "__main__":
    app.run()