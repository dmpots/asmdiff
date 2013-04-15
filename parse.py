import asm
import re

def parse(f):
  """Parse the contents of file f"""
  module = asm.Module(f)
  parse_asm(f, module)
  return module

def parse_asm(fname, module):
  """Parse an assembly file and populate module"""
  with open(fname) as f:
    for line in f:
      # start of a new function
      m_fun = re.match("(?P<fun>[0-9_a-z]+):", line, re.I)
      if m_fun:
        name = m_fun.group('fun')
        fun = asm.Function(name)
        module.functions.append(fun)
        next

      # instruction
      m_inst = re.match("\s+(?P<opcode>[a-z][a-z0-9.]+)\s+", line, re.I)
      if m_inst:
        fun.instructions.append(asm.Instruction(*lex_inst(line)))
        next

def lex_inst(inst):
  inst = inst.strip()
  ob = inst.find("[")
  cb = inst.find("]")
  if ob != -1 and cb != -1:
    inst = inst[:ob] + inst[ob:cb].replace(",", "|") + inst[cb:]

  (opcode, operands) = inst.split(maxsplit=1)
  operands = operands.split(",")
  opernads = [op.replace("|", ",") for op in operands]

  return (opcode, operands)

