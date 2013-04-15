import os
import sys

this_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(this_dir + "/../../"))

#class FileNotFound(Exception): pass

def asm_files():
  test_dirs = [this_dir + "/S"]
  for test_dir in test_dirs:
    for f in os.listdir(test_dir):
      if f.endswith(".s"):
        yield(os.path.join(test_dir, f))

def asm(name):
  f   = this_dir + "/S/" + name
  s   = f+".s"
  c_s = f+".c.s"
  if os.path.exists(s):
    return s
  if os.path.exists(c_s):
    return c_s
  raise FileNotFoundError("{} or {}".format(s, c_s))

test_files = asm_files()
