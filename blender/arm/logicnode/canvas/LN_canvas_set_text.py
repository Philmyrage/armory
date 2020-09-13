from arm.logicnode.arm_nodes import *

class CanvasSetTextNode(ArmLogicTreeNode):
    """Set canvas text"""
    bl_idname = 'LNCanvasSetTextNode'
    bl_label = 'Canvas Set Text'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Element')
        self.add_input('NodeSocketString', 'Text')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(CanvasSetTextNode, category=PKG_AS_CATEGORY)
