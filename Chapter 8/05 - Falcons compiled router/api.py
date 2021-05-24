import falcon
import json


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            "quote": "I've always been more interested in "
            "the future than in the past.",
            "author": "Grace Hopper",
        }

        resp.body = json.dumps(quote)


api = falcon.API()
api.add_route("/quote", QuoteResource())
