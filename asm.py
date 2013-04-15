
class Module:
  def __init__(self, name):
    self.name = name
    self.functions = []

class Function:
  def __init__(self, name):
    self.name = name
    self.instructions = []
  
class Instruction:
  def __init__(self, opcode, operands):
    self.opcode = opcode
    self.operands = operands

