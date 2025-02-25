#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:06:24 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:06:24 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = int(input("type a number!\n: "))

if num > 0:
	print("This number is positive.")
elif num < 0:
	print("This number is negative.")
else:
	print("This number is both positive and negative")