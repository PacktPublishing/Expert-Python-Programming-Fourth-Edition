from http import HTTPStatus

from flask import Flask, request, Response
from flask_injector import FlaskInjector
from prometheus_client import Summary, Gauge, Info, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from interfaces import ViewsStorageBackend
import di


app = Flask(__name__)

PIXEL = (
    b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00"
    b"\x00\x00\xff\xff\xff!\xf9\x04\x01\x00"
    b"\x00\x00\x00,\x00\x00\x00\x00\x01\x00"
    b"\x01\x00\x00\x02\x01D\x00;"
)

REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing requests")
AVERAGE_TOP_HITS = Gauge("average_top_hits", "Average number of top-10 page counts ")
TOP_PAGE = Info("top_page", "Most popular referrer")


@app.route("/track")
@REQUEST_TIME.time()
def track(storage: ViewsStorageBackend):
    try:
        referer = request.headers["Referer"]
    except KeyError:
        return Response(status=HTTPStatus.BAD_REQUEST)

    storage.increment(referer)

    return Response(
        PIXEL,
        headers={
            "Content-Type": "image/gif",
            "Expires": "Mon, 01 Jan 1990 00:00:00 GMT",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
        },
    )


@app.route("/stats")
@REQUEST_TIME.time()
def stats(storage: ViewsStorageBackend):
    counts: dict[str, int] = storage.most_common(10)

    AVERAGE_TOP_HITS.set(sum(counts.values()) / len(counts) if counts else 0)
    TOP_PAGE.info({"top": max(counts, default="n/a", key=lambda x: counts[x])})

    return counts


@app.route("/test")
@REQUEST_TIME.time()
def test():
    return """
    <html>
    <head></head>
    <body><img src="/track"></body>
    </html>
    """


FlaskInjector(app=app, modules=[di.RedisModule()])
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
