from flask import Flask
from sanity import app

app = Flask(__name__)

client = SanityClient("<your_project_id>", "<your_dataset>", "<your_token>")


@app.route('/members')
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
