import networkx as nx

def build_graph():
    G = nx.DiGraph()
    
    # Додавання ребер згідно із заданими пропускними здатностями
    edges = [
        ("T1", "S1", 25), ("T1", "S2", 20), ("T1", "S3", 15),
        ("T2", "S3", 15), ("T2", "S4", 30), ("T2", "S2", 10),
        ("S1", "M1", 15), ("S1", "M2", 10), ("S1", "M3", 20),
        ("S2", "M4", 15), ("S2", "M5", 10), ("S2", "M6", 25),
        ("S3", "M7", 20), ("S3", "M8", 15), ("S3", "M9", 10),
        ("S4", "M10", 20), ("S4", "M11", 10), ("S4", "M12", 15),
        ("S4", "M13", 5), ("S4", "M14", 10)
    ]
    
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    
    return G

def compute_max_flow(G, source, sink):
    return nx.maximum_flow(G, source, sink)

# Побудова графа
graph = build_graph()

# Додаємо супер-джерело (S) і супер-сток (T)
graph.add_edge("S", "T1", capacity=float("inf"))
graph.add_edge("S", "T2", capacity=float("inf"))
graph.add_edge("M1", "T", capacity=float("inf"))
graph.add_edge("M2", "T", capacity=float("inf"))
graph.add_edge("M3", "T", capacity=float("inf"))
graph.add_edge("M4", "T", capacity=float("inf"))
graph.add_edge("M5", "T", capacity=float("inf"))
graph.add_edge("M6", "T", capacity=float("inf"))
graph.add_edge("M7", "T", capacity=float("inf"))
graph.add_edge("M8", "T", capacity=float("inf"))
graph.add_edge("M9", "T", capacity=float("inf"))
graph.add_edge("M10", "T", capacity=float("inf"))
graph.add_edge("M11", "T", capacity=float("inf"))
graph.add_edge("M12", "T", capacity=float("inf"))
graph.add_edge("M13", "T", capacity=float("inf"))
graph.add_edge("M14", "T", capacity=float("inf"))

# Обчислення максимального потоку
max_flow, flow_dict = compute_max_flow(graph, "S", "T")

# Виведення результату
print("Максимальний потік:", max_flow)
print("Розподіл потоку:")
for u, flows in flow_dict.items():
    for v, flow in flows.items():
        if flow > 0:
            print(f"{u} -> {v}: {flow}")


