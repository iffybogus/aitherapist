from flask import Flask, render_template, jsonify
from database import load_clients

app = Flask(__name__)

@app.route('/')
def index():
    clients = load_clients()
    return render_template("home.html", clients=clients, company_name="Technically Yours")

@app.route("/services")
def list_services():
  return jsonify(clients)
  
# if we invoke program with python
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

#app.run(host='0.0.0.0', port=5000)
