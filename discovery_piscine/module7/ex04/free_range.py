#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 10:10:37 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 10:10:38 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) - 1 != 2:
	print("none")
else:
	num0 = sys.argv[1]
	num1 = sys.argv[2]
	if num0.isnumeric() and num1.isnumeric():
		num0, num1 = int(num0), int(num1)
		free_range = list(range(num0, num1 + 1))
		print(free_range)
	else:
		print("only two numeric parameters are acceptable")

# def intput():
# 	entry = input()
# 	if entry.isnumeric():
# 		print("oi")
# 	else:
# 		print("Only numeric entry are accepted")