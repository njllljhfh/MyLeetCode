# -*- coding:utf-8 -*-
from collections import deque


class Vertex(object):
    """顶点类"""

    def __init__(self, val: int):
        self.val = val


def vals_to_vets(vals: list[int]) -> list["Vertex"]:
    """输入值列表 vals ，返回顶点列表 vets"""
    return [Vertex(val) for val in vals]


class GraphAdjList(object):
    """基于邻接表实现的无向图类"""

    def __init__(self, edges: list[list[Vertex]]):
        """构造方法"""
        self.adj_list = dict[Vertex, list[Vertex]]()

        # 添加所有顶点和边
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        """获取顶点数量"""
        return len(self.adj_list)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 添加边 vet1 - vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """删除边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 删除边 vet1 - vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self, vet: Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            return

        # 在邻接表中添加一个新链表
        self.adj_list[vet] = []

    def remove_vertex(self, vet: Vertex):
        """删除顶点"""
        if vet not in self.adj_list:
            raise ValueError()

        # 在邻接表中删除顶点 vet 对应的链表
        self.adj_list.pop(vet)

        # 遍历其他顶点的链表，删除所有包含 vet 的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def view(self):
        for vertex in self.adj_list:
            ls = [str(item.val) for item in self.adj_list[vertex]]
            print(f'{vertex.val}: {", ".join(ls)}')


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """广度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []

    # 哈希集合，用于记录已被访问过的顶点
    visited = set[Vertex]([start_vet])

    # 队列用于实现 BFS
    que = deque[Vertex]([start_vet])

    # 以顶点 vet 为起点，循环直至访问完所有顶点
    while len(que) > 0:
        vet = que.popleft()  # 队首顶点出队
        res.append(vet)  # 记录访问顶点

        # 遍历该顶点的所有邻接顶点
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue  # 跳过已被访问的顶点
            que.append(adj_vet)  # 只入队未访问的顶点
            visited.add(adj_vet)  # 标记该顶点已被访问

    # 返回顶点遍历序列
    return res


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    """深度优先遍历辅助函数"""
    res.append(vet)  # 记录访问顶点
    visited.add(vet)  # 标记该顶点已被访问

    # 遍历该顶点的所有邻接顶点
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue  # 跳过已被访问的顶点

        # 递归访问邻接顶点
        dfs(graph, visited, res, adjVet)


def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """深度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []
    # 哈希集合，用于记录已被访问过的顶点
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res


if __name__ == "__main__":
    # 初始化无向图
    print(f'初始化无向图')
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
        [v[3], v[4]],
    ]
    graph = GraphAdjList(edges)
    del edges
    graph.view()
    print('- ' * 20)

    print(f'广度优先遍历:从节点 1 开始遍历')
    res = graph_bfs(graph, v[0])
    print(f'遍历结果: {", ".join([str(item.val) for item in res])}')
    print('- ' * 20)

    print(f'深度优先遍历:从节点 1 开始遍历')
    res = graph_dfs(graph, v[0])
    print(f'遍历结果: {", ".join([str(item.val) for item in res])}')
    print('- ' * 40)

    # 添加边
    print(f'添加边 [1, 2]')
    graph.add_edge(v[0], v[2])
    graph.view()
    print('- ' * 20)

    # 删除边
    print(f'删除边 [1, 3]')
    graph.remove_edge(v[0], v[1])
    graph.view()
    print('- ' * 20)

    # 添加顶点
    print(f'添加顶点 6')
    v5 = Vertex(6)
    graph.add_vertex(v5)
    graph.view()
    print('- ' * 20)

    # 删除顶点 3, 索引为 1
    print(f'删除顶点 3')
    graph.remove_vertex(v[1])
    graph.view()
    print('- ' * 20)
