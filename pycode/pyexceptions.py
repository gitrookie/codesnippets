import logging

class HPLIPException(Exception):
    def __init__(self, name="Printer not found"):
        self.name = name
    def __str__(self):
        return self.name


print_dict = {"hp": 1, "canon": 2}
def foo(comp):
    try:
        return print_dict[comp]
    except KeyError as e:
        logging.exception("logging exception") # HPLIPException from e


foo("lexmark")
