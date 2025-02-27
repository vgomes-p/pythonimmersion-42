#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 16:38:24 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/26 16:38:24 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args = sys.argv[1:2]

fargs = str(args).replace('[', '').replace(']', '').replace("'", "").upper()

if len(sys.argv) - 1 <= 0:
	print("none")
else:
	print(f'The first parameter upcased is: {fargs}')