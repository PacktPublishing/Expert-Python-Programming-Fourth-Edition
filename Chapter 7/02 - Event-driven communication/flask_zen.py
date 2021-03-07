import this

from flask import Flask

app = Flask(__name__)

rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
)


def simple_html(body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Book Example</title>
      </head>
      <body>
        {body}
      </body>
    </html>
    """


@app.route("/")
def hello():
    return simple_html("<a href=/zen>Python Zen</a>")


@app.route("/zen")
def zen():
    return simple_html("<br>".join(this.s.translate(rot13).split("\n")))


if __name__ == "__main__":
    app.run()
