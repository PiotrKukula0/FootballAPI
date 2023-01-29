from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def matches():
    url = 'https://api.football-data.org/v2/matches'
    headers = {'X-Auth-Token': '87ec44505a664bd0bead914c6b6d62a0'}
    response = requests.get(url, headers=headers)

    data = response.json()
    return render_template("matches.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
