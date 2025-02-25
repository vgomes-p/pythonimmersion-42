#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    round_up.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:08:43 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:08:44 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = float(input("Give me a number: "))

rnum = int(num) + (1 if num > int(num) else 0)

print(rnum)