#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 10:09:56 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 10:09:56 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args = sys.argv[1:]
cnt_args = len(sys.argv) - 1

if cnt_args <= 0:
	print("none")
else:
	for word in args:
		if not word.endswith("ism"):
			word += "ism"
			print(word)
		elif word.endswith("ism"):
			pass
