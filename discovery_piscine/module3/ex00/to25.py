#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:07:14 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:07:14 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = int(input("Enter a number less than 25: "))

while num != 25:
	if num > 25:
		print("Error")
		break
	else:
		for need in range (num, 26):
			print(f"Inside the loop, my variable is {need}")
		break