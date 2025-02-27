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
	@staticmethod
	def add_one(param):
		param += 1
		return param

var = 42
print(var)
PyImmersion.add_one(var)
print(var)
