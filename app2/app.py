from flask import Flask, render_template

app = Flask(__name__)

# Services list for demonstration
services = [
    {"name": "Inventory System", "status": "Online", "version": "v1.2.0"},
    {"name": "Payment Gateway", "status": "Online", "version": "v1.4.3"},
    {"name": "HR Portal", "status": "Maintenance", "version": "v0.9.5"},
]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", services=services)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
