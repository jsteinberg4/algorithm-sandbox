import enum
from collections import namedtuple, deque
from pprint import pprint
from typing import List

from graph import Graph

Edge = namedtuple("Edge", ["dest"])


class DirectedGraph(Graph):
    class SearchType(enum.Enum):
        BFS = "breadth-first-search"
        DFS = "depth-first-search"

    def __init__(self, *args, **kwargs):
        super(DirectedGraph, self).__init__(*args, **kwargs)
        self._adjacency_list = dict()  # Dict[NodeId, List[Edge]]
        self._search_map = {
            DirectedGraph.SearchType.BFS: self._bfs,
            DirectedGraph.SearchType.DFS: self._dfs,
        }

    def search(
        self, s, t, *args, search_type: SearchType = SearchType.BFS, **kwargs
    ) -> List:
        return self._search_map.get(search_type)(s, t, *args, **kwargs)

    def _bfs(self, s, t, *args, **kwargs) -> List:
        # No path exists if the nodes don't exist
        if s not in self._adjacency_list or t not in self._adjacency_list:
            return []

        queue = deque([s])
        node_to_predecessor = {s: -1}
        exists: bool = False
        while len(queue) > 0:
            next_node = queue.pop()

            for edge_to in self._adjacency_list.get(next_node):
                edge_to: Edge
                if edge_to.dest not in node_to_predecessor:
                    node_to_predecessor[edge_to.dest] = next_node
                    queue.appendleft(edge_to.dest)

                if edge_to.dest == t:
                    queue.clear()
                    exists = True

        path = deque()
        if exists:
            vertex = t
            while vertex != s:
                path.appendleft(vertex)
                vertex = node_to_predecessor[vertex]
            path.appendleft(vertex)

        return list(path)

    def _dfs(self, s, t, *args, **kwargs) -> List:
        # No path exists if either S or T do not exist
        if s not in self._adjacency_list or t not in self._adjacency_list:
            return []

        stack = deque()
        node_to_predecessor = {s: -1}
        exists = False

        while len(stack) > 0:
            next_node = stack.pop()

            for edge_to in self._adjacency_list.get(next_node):
                dest = edge_to.dest
                if dest not in node_to_predecessor:
                    stack.append(dest)
                    node_to_predecessor[dest] = next_node

                if dest == t:
                    stack.clear()
                    exists = True

        path = deque()
        if exists:
            vertex = t
            while vertex != -1:
                path.appendleft(vertex)
                vertex = node_to_predecessor.get(vertex, -1)
        return list(path)



    @property
    def nodes(self):
        """Getter method for nodes in the graph.
        Implemented as a generator for practice. Also beneficial if
        # nodes grows extremely large.
        """
        return (node for node in self._adjacency_list.keys())

    @property
    def edges(self):
        """Getter method for edges pairs (src, destination).
        Implemented as a generator for practice. Also beneficial for a
        connected graph with many nodes.
        """
        for node in self.nodes:
            for adjacent_node in self._adjacency_list[node]:
                yield node, adjacent_node.dest


if __name__ == "__main__":
    adj_list = {
        1: [Edge(2), Edge(3)],
        2: [Edge(1), Edge(3), Edge(4), Edge(5)],
        3: [Edge(1), Edge(2), Edge(5), Edge(7)],
        4: [Edge(2), Edge(5)],
        5: [Edge(2), Edge(3), Edge(4), Edge(6)],
        6: [Edge(5)],
        7: [Edge(3), Edge(8)],
        8: [Edge(3), Edge(7)],
    }

    graph = DirectedGraph()
    setattr(graph, "_adjacency_list", adj_list)
    bfs_path = graph.search(1, 4, search_type=DirectedGraph.SearchType.BFS)
    # FIXME :: no dfs path found?
    dfs_path = graph.search(1, 4, search_type=DirectedGraph.SearchType.DFS)

    print(bfs_path)
    print(dfs_path)