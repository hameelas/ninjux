"""
	ninjux.problem
	~~~~~~~~~~~~

	Implements the problem related objects.

	:copyright: (c) 2013 by Hamed Saleh.
	:license: GPL, see LICENSE for more details.
"""

class Problem:
	def __init__(self, name, capsules):
		self.name = name
		self.capsules = capsules

	def __init__(self, address):
		self.capsules = []
		from_file(open (address + "config"))

	def from_file(self, config):
		""" 
		Parsing Problem infromation from a file in old `HelliJudge` style
		
		There are three types of testcase specification:
		
		1- TEST `time` `memory` `input` `score`
			This type specifies a single testcase which 
			`time` stands for its time limit,
			`memory` stands for its memory limit,
			`input` specifies the format of inputs,
			and solving that has `score` points.

		2- GROUP `count` `time` `memory` `score`
			Which specifies a group of `count` tests with similar properties,
			and solving each of them has `score`/`count` points.

		3- CAP `count` `score`
			The set of testcases in next `count` lines will be judged
			as a capsule of testcases and will have `score` points,
			only if all of them solve correctly.
			Note: lines after CAP, must NOT have score property at the end.

		Note: sum of scores for a problem should be 100.
		"""
		
		while True:
			command = config.strip().split()
			if not command: break

			if "TEST" == command[0]:
				self.capsules.append(Test(command[1:]).getcap())

			elif "GROUP" == command[0]:
				for num in range (int (command[1])):
					self.capsules.append(Test(command[2:]).getcap())

			elif "CAP" == command[0]:
				self.capsules.append(Capsule(command[1:], config))

			else: pass

		config.close()
	
class Capsule:


class Test:
	
