#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:08:35 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:08:35 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = float(input("Give me a number: "))

if num == int(num):
	print("This is an integer")
else:
	print("This is a decimal.")
