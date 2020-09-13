from arm.logicnode.arm_nodes import *

class IsTrueNode(ArmLogicTreeNode):
    """Is true node"""
    bl_idname = 'LNIsTrueNode'
    bl_label = 'Is True'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketBool', 'Value')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(IsTrueNode, category=PKG_AS_CATEGORY)
