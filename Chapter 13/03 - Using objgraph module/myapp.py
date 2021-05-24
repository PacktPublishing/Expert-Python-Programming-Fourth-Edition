from collections import Counter
import objgraph


def graph_references(*objects):
    objgraph.show_refs(
        objects,
        filename="show_refs.png",
        refcounts=True,
        # additional filtering for the sake of brevity
        too_many=5,
        filter=lambda x: not isinstance(x, dict),
    )
    objgraph.show_backrefs(objects, filename="show_backrefs.png", refcounts=True)


if __name__ == "__main__":
    quote = """
    People who think they know everything are a
    great annoyance to those of us who do.
    """
    words = quote.lower().strip().split()
    counts = Counter(words)
    graph_references(words, quote, counts)
