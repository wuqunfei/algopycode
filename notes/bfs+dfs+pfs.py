import collections
from queue import PriorityQueue


class Node:
    def __init__(self, val):
        self.val = val
        self.left: Node = None
        self.right: Node = None


class Search:

    def __init__(self):
        self.visited = set()
        self.queue = collections.deque()

    def depth_first_search(self, node: Node):
        if node in self.visited:
            return
        self.visited.add(node)
        # find the children node and go next
        for leaf in self.children():
            if leaf not in self.visited:
                self.depth_first_search(node)

    def breath_first_search(self, node: Node):
        self.queue.append(node)
        while self.queue:
            leaf = self.queue.popleft()
            nodes = self.children(node)
            self.queue.append(nodes)

    def priority_search(self, node: PriorityQueue):
        while node:
            node.get(block=False, timeout=2)

    def children(self, node: Node):
        return [node.left, node.right]
