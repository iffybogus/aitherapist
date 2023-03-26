from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICES = [
  {
    'id': 2,
    'product': "Sex Therapy",
    'location': "Enugu",
    'price': '$75'
  },
  {
    'id': 3,
    'product': "Speech Therapy",
    'location': "Dallas",
    'price': '$175'
  },
  {
    'id': 4,
    'product': "Drug Therapy",
    'location': "New York",
    'price': '$250'
  },
  {
    'id': 5,
    'product': "Gambling Therapy",
    'location': "Enugu",
    'price': '$75'
  } 
]

@app.route('/')
def index():
    return render_template("home.html", services = SERVICES, company_name="Technically Yours")

@app.route("/services")
def list_services():
  return jsonify(SERVICES)
  
# if we invoke program with python
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

#app.run(host='0.0.0.0', port=5000)
