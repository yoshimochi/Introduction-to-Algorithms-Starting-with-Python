def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        # 最もコストが小さい頂点を探す
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i
        # 最もコストが小さい頂点を取り出す
        u = q.pop(q.index(r))
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新
                dist[i[0]] = dist[u] + i[1]

    return dist

# 辺のリスト（終点とコストのリスト）
edges = [
    [[1, 4], [2, 3]], # 頂点Aから辺のリスト
    [[2, 1], [3, 1], [4, 5]], # 頂点Bから辺のリスト
    [[5, 2]], # 頂点Cから辺のリスト
    [[4, 3]], # 頂点Dから辺のリスト
    [[6, 2]], # 頂点Eから辺のリスト
    [[4, 1], [6, 4]], # 頂点Fから辺のリスト
    [] # 頂点Gから辺のリスト
]

print(dijkstra(edges, 7))