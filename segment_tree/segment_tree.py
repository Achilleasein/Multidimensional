import math

class segment_node:
    def __init__(self, left_child=None, right_child=None, parent=None, segment=None, value=0):
        self.left_child  = left_child
        self.right_child = right_child
        self.parent      = parent
        self.segment     = segment
        self.value       = value

    def calculateValue (self, value):
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

    def getSum(self, left, right):
        return 0


class segment_tree:
	def __init__(self, head_node=None, tree_size=0):
	    self.head_node = head_node
	    self.tree_size = tree_size
	
	def returnSize(self):
	    return self.return_size
        
        def returnHead(self):
            return self.head_node

