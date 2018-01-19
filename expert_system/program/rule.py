# rule.py
# Modules concerned with rules.
# encoding: utf-8
# version: python 3.5.4

import re

re_a_rule = re.compile(r'(\{.*?\})')
re_if_part = re.compile(r'^\{IF:\s+(\[.*?\])')
re_then_part = re.compile(r'THEN:\s+\'(.*?)\'')
re_descrp_part = re.compile(r'DESCRIPTION:\s+\'(.*?)\'')


class Rule:
	"""
	Rule class.
	"""

	def __init__(self, ant, con, desc=None):
		"""
		Rule object.

		Args:
			ant - antecedent
			con - consequent
			desc - description
		Returns:
			rule - rule object
		"""

		self.antecedent = ant
		self.consequent = con
		self.description = desc

	def __str__(self):
		"""
		Display rule.
		"""

		s = ''
		if self.description:
			s += 'Description: {}\n'.format(self.description)
		s += 'IF\t\t'
		for ant in self.antecedent:
			s += '{}\n'.format(ant)
			if ant != self.antecedent[-1]:
				s += '\tand\t'
		s += 'THEN\t{}\n'.format(self.consequent)

		return s
		


def read_rules(rule_path):
	"""
	Read rules from path.

	rule_path: path of rules
	"""

	# load rules of text format
	rules_str = load_rules_str(rule_path)

	# generate rules from text
	rules = list(map(generate_a_rule, rules_str))

	return rules


def  load_rules_str(rule_path):
	"""
	Load rules in text format.
	
	Args:
		rule_path - file path of rules
	Returns:
		rules_str - list of string rules
	"""

	# load rules text
	with open(rule_path, 'r') as f:
		rules = ''.join(f.read().splitlines())

	# seperate rules
	rules_str = re_a_rule.findall(rules)

	return rules_str


def generate_a_rule(rule_str):
	"""
	Generate a rule from string.

	Args:
		rule_str - string rule
	Returns:
		rule - rule object
	"""

	# if, then, and description part of rule
	if_part_str = re_if_part.findall(rule_str)[0]
	exec('if_part = ' + if_part_str, globals(), globals())
	then_part = re_then_part.findall(rule_str)[0]
	descrp_part = re_descrp_part.findall(rule_str)[0]

	return Rule(if_part, then_part, descrp_part)


if __name__ == '__main__':
	# test read rules 
	rule_path = 'rules.txt'
	rules = read_rules(rule_path)
	print(rules[3])