from abc import ABC, abstractmethod
from typing import List


class Graph(ABC):
    """
    Represents a graph as a collection of nodes and edges.
    """

    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__()

    @property
    @abstractmethod
    def nodes(self):
        pass

    @property
    @abstractmethod
    def edges(self):
        pass

    @abstractmethod
    def search(self, s, t, /, *args, **kwargs) -> List:
        """Search the tree from node S to node T. Return a path, if one exists.
        """
        pass


