#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Dough
import Toppings
import Oven
import Packinging
from typing import List

from Packinging import Packinging


class PizzaFacade(Dough, Toppings, Oven, Packinging):
	def order_pizza(self):
		pass

	def __init__(self):
		self.___dough : Dough = None
		self.___toppings : Toppings = None
		self.___oven : Oven = None
		self.___packaging : Packinging = None

