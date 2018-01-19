# infer.py
# Perform inference from rules and facts, get results inferred.
# encoding: utf-8
# version: python 3.5.4

from rule import read_rules
from fact import read_facts
from engine import Engine


rule_path = 'rules.txt'  # file path for rules
fact_path = 'facts.txt'  # file path for rules


# read rules and facts
print("Reading rules and facts...")
rules = read_rules(rule_path)
print('--RULES--')
[print(r) for r in rules]

facts = read_facts(fact_path)
print('--Facts--')
[print(f) for f in facts]
print()


# construct engine from rules and facts
print("Constructing engine...")
engine = Engine(rules, facts)
print()


# backward inference by engine
print("Inferring...")
targets = ['the animal is bird',
		   'the animal is cat',
		   'the animal is fish',
		   'the animal is snake']

# infer backward
# if result is True, target can be inferred from the facts;
# if result is False, target can not be inferred from the facts
for target in targets:
	result = engine.infer(target)
	print(target + ' ->', result)

print('\nDone.')