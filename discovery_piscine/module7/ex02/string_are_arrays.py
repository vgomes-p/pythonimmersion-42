#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 10:09:31 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 10:09:31 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args = sys.argv[1]
cnt = args.count("z")

if len(sys.argv) - 1 <= 0:
	print('none')
else:
	print("z" * cnt)