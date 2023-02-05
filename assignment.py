import random
import pytest
from Fun import sum,sun

def test_sum():
  assert sum(5,7) == 10

def test_sun():
  assert sun(5,4) == 1