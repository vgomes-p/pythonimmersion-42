#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:07:27 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:07:27 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = int(input("Enter a number!\n: "))

for mult in range (0, 10):
	result = num * mult
	print (f"{num} x {mult} = {result}")