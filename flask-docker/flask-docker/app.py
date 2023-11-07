from flask import Flask

app = Flask(__name__)

# take the user to the URL '/' i.e. homepage and display text
@app.route('/')
def index():
    return '<h1>Hello there, Jay</h2>'

if __name__ == "__main__":
    app.run(debug=True)