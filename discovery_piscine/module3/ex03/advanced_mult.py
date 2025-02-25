#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:07:46 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:07:46 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

init = 0

while init != 11:
	mult = 0
	results = []
	while mult < 11:
		result = init * mult
		results.append(str(result))
		mult += 1
	formated_result = " ".join(results)
	print(f"Table of {init}: {formated_result}")
	init += 1