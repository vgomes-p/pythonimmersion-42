#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 10:08:37 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 10:08:37 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) - 1 <= 0:
	print("none")
else:
	param = str(sys.argv[1]).replace('[', '').replace(']', '').replace("'", '')
	user_entry = str(input("What was the parameter? "))
	if param == user_entry:
		print("Good job!")
	else:
		print("Nope, sorry...")