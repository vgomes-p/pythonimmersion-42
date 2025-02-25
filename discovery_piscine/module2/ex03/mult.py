#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:06:56 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:06:56 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

mult = int(num1) * int(num2)
result = f"{num1} x {num2} = {mult}"

if mult > 0:
	print(f"{result}\nThe result is positive.")
elif mult < 0:
	print(f"{result}\nThe result is Negative.")
else:
	print(f"{result}\nThe result is both positive and negative")