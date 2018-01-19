# fact.py
# Modules concerned with facts.
# encoding: utf-8
# version: python 3.5.4


def read_facts(fact_path):
	"""
	Read facts from path.

	Args:
		fact_path - file path of facts
	Returns:
		facts - list of facts
	"""

	with open(fact_path, 'r') as f:
		facts = f.read().splitlines()

	return facts


if __name__ == '__main__':
	fact_path = 'facts.txt'
	facts = read_facts(fact_path)
	print(facts)