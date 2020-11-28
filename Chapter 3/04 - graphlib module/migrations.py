from graphlib import TopologicalSorter

table_references = {
    "customers": set(),
    "accounts": {"customers"},
    "products": set(),
    "orders": {"accounts", "customers"},
    "order_products": {"orders", "products"},
}

if __name__ == "__main__":
    sorter = TopologicalSorter(table_references)
    print(list(sorter.static_order()))
