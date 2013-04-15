import unittest
import os

from . import paths
import asmdiff.parse as parse

class TestAsmParse(unittest.TestCase):
  # automatically generate tests to parse all the files
  for test in paths.test_files:
    method_name = os.path.basename(test).replace(".","_")
    code = """
def test_parse_{}(self):
  parse.parse("{}")
""".format(method_name, test)
    exec(code)

  def assertInstructions(self, fun, insts):
    self.assertEqual(len(fun.instructions), len(insts))
    for (i, (opcode, operands)) in enumerate(insts):
      self.assertEqual(fun.instructions[i].opcode, opcode)
      self.assertEqual(len(fun.instructions[i].operands), len(operands))
      for (j, operand) in enumerate(operands):
        self.assertEqual(fun.instructions[i].operands[j], operand)

  def test_empty(self):
    module = parse.parse(paths.asm("empty"))
    self.assertEqual(len(module.functions), 1)
    f = module.functions[0]
    self.assertEqual(f.name, "_empty")
    self.assertInstructions(f, [("bx", ["lr"])])

  def test_two(self):
    module = parse.parse(paths.asm("two"))
    self.assertEqual(len(module.functions), 2)
    f1 = module.functions[0]
    f2 = module.functions[1]
    self.assertEqual(f1.name, "_one")
    self.assertInstructions(f1, [("bx", ["lr"])])
    self.assertEqual(f2.name, "_two")
    self.assertInstructions(f2, [("bx", ["lr"])])

