"""
Resources used to write this code:
A Minimal Application n.d., Pallets, accessed 30 May 2026,
<https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application>
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
