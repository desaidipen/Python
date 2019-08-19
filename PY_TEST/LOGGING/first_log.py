import logging
# Logging Documentation: https://docs.python.org/3/library/logging.html?highlight=logger

logging.basicConfig(filename="test.log", level=logging.DEBUG, 
                    format='%(asctime)s: %(levelname)s: %(message)s')

def add(x, y):
  """Add Function"""
  return x + y

def substract(x, y):
  """Substract Function"""
  return x - y

def multiply(x, y):
  """Multiply Function"""
  return x * y

def divide(x, y):
  """Divide Function"""
  return x / y

n1 = 200
n2 = 10

add_result = add(n1, n2)
logging.debug("Add: {} + {} = {}".format(n1, n2, add_result))

sub_result = substract(n1, n2)
logging.debug("Sub: {} - {} = {}".format(n1, n2, sub_result))

mul_result = multiply(n1, n2)
logging.debug("Mul: {} * {} = {}".format(n1, n2, mul_result))

div_result = divide(n1, n2)
logging.debug("Div: {} / {} = {}".format(n1, n2, div_result))