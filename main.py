from flask import Flask, request

app = Flask(__name__)

@app.route("/auth/register", methods=["POST"])
def registerUser():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    return f"u: {username}, p: {password}"


if __name__ == "__main__":
    app.run()