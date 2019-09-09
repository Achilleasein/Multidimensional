class segment_node:
    def __init__(self, left_child, right_child, parent, segment):
        self.left_child  = left_child
        self.right_child = right_child
        self.parent      = parent
        self.segment     = segment


N1 = segment_node(None , None , None , 'A')
