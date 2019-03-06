class StateNode:

    def __init__(self, data, heuristic_value, parent=None, children=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.heuristic_value = heuristic_value
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_data(self):
        return self.data