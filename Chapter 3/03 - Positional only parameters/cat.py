def cat(a: str, b: str, delim: str):
    return delim.join([a, b])


if __name__ == "__main__":
    cat("John", "Doe", " ")
    cat(a="John", b="Doe", delim=" ")
    cat("John", "Doe", delim=" ")
