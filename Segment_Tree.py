class segment_node:
    def __init__(self, left_child, right_child, parent, segment, value):
        self.left_child  = left_child
        self.right_child = right_child
        self.parent      = parent
        self.segment     = segment
        self.value       = value

    def calculate_value (self, value):
        try:
            value = int(right_child.value)
        except:
            pass
        try:
            value = int(left_child.value)
        except:
            pass
        try:
            value = int(right_child.value) + int(left_child.value)
        except:
            pass

N1 = segment_node(None , None , None , 'A', 0)


 