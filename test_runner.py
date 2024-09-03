import armsim
#run instruction tests
import instruction_tests
import sys
from io import StringIO,BytesIO
  
'''
Full program tests in /tests directory
exit code in x0 for all test cases should be 7
'''
with open('tests/arithmetic_test.s','r') as f:
	armsim.parse(f.readlines())
armsim.run()
assert armsim.reg['x0'] == 7, "arithmetic_test returned incorrect value of {}".format(armsim.reg['x0'])
armsim.reset()
with open('tests/branch_test.s','r') as f:
	armsim.parse(f.readlines())
armsim.run()
assert armsim.reg['x0'] == 7, "arithmetic_test returned incorrect value of {}".format(armsim.reg['x0'])
armsim.reset()

with open('tests/brk_test.s','r') as f:
	armsim.parse(f.readlines())
armsim.run()
assert armsim.reg['x0'] == 7, "brk_test returned incorrect value of {}".format(armsim.reg['x0'])
armsim.reset()

print("All tests passed")  
