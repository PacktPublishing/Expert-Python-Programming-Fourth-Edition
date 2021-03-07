from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def echo():
    print(request.headers)
    return (
        f"METHOD: {request.method}\n"
        f"HEADERS:\n{request.headers}"
        f"BODY:\n{request.data.decode()}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
