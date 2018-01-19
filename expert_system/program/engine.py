# engine.py
# Modules concerned with engines.
# encoding: utf-8
# version: python 3.5.4


class Engine:
	"""
	Engine class.
	"""

	def __init__(self, rules, facts):
		"""
		Construct inference engine.

		Args:
			rules - rule library
			facts - fact library
		Returns:
			engine - inference engine
		"""

		self.rule_library = rules
		self.fact_library = facts
		self.condition_stack = []

	def infer(self, target):
		"""
		Inferring backward by the engine given rules and facts.

		Args:
			target - target of inference
		Returns:
			result - inference result. if result is True, target 
		can be inferred from the facts; if result is False, target
		can not be inferred from the facts
		"""

		# if target in fact library, matched
		if target in self.fact_library:
			return True

		# if target not in fact library, check every rule whether
		# target can be inferred from it
		for rule in self.rule_library:
			# target can be inferred from some rule
			if self.can_be_inferred_from_rule(target, rule):
				return True

		# target can't be inferred from any rule
		return False

	def can_be_inferred_from_rule(self, target, rule):
		"""
		Whether target can be inferred from rule.

		Args:
			target
			rule
		Returns:
			True if target can be inferred from rule, False if
		target can't be inferred from rule.
		"""

		# if target does not match consequent of rule, can't be
		# inferred from it
		if target != rule.consequent:
			return False

		# if target matches consequent, check whether every antecedent
		# can be inferred
		for ant in rule.antecedent:
			# if any antecedent can't be inferred, target can't be inferred
			if not self.infer(ant):
				return False

		# every antecedent can be inferred
		return True

