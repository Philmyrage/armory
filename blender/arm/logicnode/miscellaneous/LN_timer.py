from arm.logicnode.arm_nodes import *

class TimerNode(ArmLogicTreeNode):
    """Timer node"""
    bl_idname = 'LNTimerNode'
    bl_label = 'Timer'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'Start')
        self.add_input('ArmNodeSocketAction', 'Pause')
        self.add_input('ArmNodeSocketAction', 'Stop')
        self.add_input('NodeSocketFloat', 'Duration', default_value=1.0)
        self.add_input('NodeSocketInt', 'Repeat', default_value=1)

        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('ArmNodeSocketAction', 'Done')
        self.add_output('NodeSocketBool', 'Running')
        self.add_output('NodeSocketInt', 'Time Passed')
        self.add_output('NodeSocketInt', 'Time Left')
        self.add_output('NodeSocketFloat', 'Progress')
        self.add_output('NodeSocketFloat', 'Repetitions')

add_node(TimerNode, category=PKG_AS_CATEGORY)
