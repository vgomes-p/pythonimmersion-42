#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:08:25 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:08:26 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the first number: "))

print(f'''Thank you!
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} / {num2} = {num1 / num2}
{num1} * {num2} = {num1 * num2}''')