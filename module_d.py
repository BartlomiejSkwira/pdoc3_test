# FYI: This module and class intentionally has no docstrings.

module_variable = 1


class NoDocStrings:
    class_variable = 2

    def __init__(self):
        self.instance_variable = 3

    def foo(self):
        pass

    def _private_method(self):
        pass

    def __name_mangled_method(self):
        pass


def module_function():
    pass
