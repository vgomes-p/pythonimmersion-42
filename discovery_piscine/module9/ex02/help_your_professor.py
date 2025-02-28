#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 17:43:04 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 17:43:05 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PyImmersion:
	@staticmethod
	def average(classgrades):
		all_grade = 0
		for name, grade in classgrades.items():
			all_grade = all_grade + int(grade)
		if not classgrades:
			return 0
		else:
			return all_grade / len(classgrades)


class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

print(f"Average for class 3B: {PyImmersion.average(class_3B)}")
print(f"Average for class 3C: {PyImmersion.average(class_3C)}")