import sys
import os
sys.path.extend(['.', '..'])

from pycparser import parse_file
from minic.c_ast_to_minic import transform
from transform_func import *
from func_utils import function_wrapper

if __name__ == "__main__":
  directory_path = "./inputs/checkin4_inputs"
  directory = os.fsencode(directory_path)
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not filename.endswith("_out.c"):
      output_c = function_wrapper(os.path.join(directory_path, filename))
      mast = transform(parse_file(output_c))
      ftranslator = FunctionalTranslator(mast)
      print("File: {} \nInput:".format(filename))
      with open(os.path.join(directory_path, filename), 'r') as fin:
        print(fin.read())
      print("Output:\n{}\n----------".format(ftranslator))