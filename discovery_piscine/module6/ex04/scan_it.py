#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 17:03:08 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/26 17:03:08 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

num_args = len(sys.argv) - 1

if int(num_args) != 2:
	print('none')
else:
	first_param = sys.argv[1]
	second_param = sys.argv[2]
	num_rep = second_param.count(first_param)

	ffirst_param = str(first_param).replace('[', '').replace(']', '').replace("'", '').replace('"', '')
	fsecond_param = str(second_param).replace('[', '').replace(']', '').replace("'", '').replace('"', '')
	print(f"'{ffirst_param}' repeats {num_rep} times in '{fsecond_param}' string")