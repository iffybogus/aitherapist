from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Ifeatu\'s Flask!'

# if we invoke program with python
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

#app.run(host='0.0.0.0', port=5000)
