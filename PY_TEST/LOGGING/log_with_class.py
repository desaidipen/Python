import logging
# Logging Documentation: https://docs.python.org/3/library/logging.html?highlight=logger

logging.basicConfig(filename='test.log', level=logging.INFO, 
                    format='%(levelname)s : %(message)s')


class Employee:
  """A sample Employee class"""

  def __init__(self, first, last):
    self.first = first
    self.last = last

    logging.info("Crated Employee: {} - {}".format(self.fullname, self.email))

  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first.lower(), self.last.lower())

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)


emp1 = Employee("Dipen", "Desai")
emp2 = Employee("Dhara", "Desai")
emp3 = Employee("Riha", "Desai")