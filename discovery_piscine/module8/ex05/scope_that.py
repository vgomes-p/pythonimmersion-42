#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 14:30:19 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 14:30:19 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PyImmersion:
	def __init__(self, var):
		self.var = var

	def add_one(self):
		self.var += 1
		return self.var
	
	def printer(self):
		var0 = self.add_one()
		print(var0)

var = 42
print(var)
var1 = PyImmersion(var)
var1.printer()