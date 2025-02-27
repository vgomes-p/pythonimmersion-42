#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 14:31:07 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 14:31:07 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class PyImmersion:
	@staticmethod
	def shrink(pos):
		print(pos[:8])

	@staticmethod
	def enlarge(pos):
		print(pos.ljust(8, 'z'))


if len(sys.argv) - 1 <= 0:
	print("none")
else:
	args = []

	for arg in sys.argv[1:]:
		arg = arg.replace('[', '').replace(']', '').replace("'", '')
		args.append(arg)
	
	for pos in args:
		if len(pos) >= 8:
			PyImmersion.shrink(pos)
		else:
			PyImmersion.enlarge(pos)