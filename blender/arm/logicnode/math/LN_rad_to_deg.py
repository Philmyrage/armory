from arm.logicnode.arm_nodes import *

class RadToDegNode(ArmLogicTreeNode):
    """Radians to degrees node"""
    bl_idname = 'LNRadToDegNode'
    bl_label = 'Rad to Deg'

    def init(self, context):
        self.add_input('NodeSocketFloat', 'Radians')
        self.add_output('NodeSocketFloat', 'Degrees')

add_node(RadToDegNode, category=PKG_AS_CATEGORY, section='angle')
