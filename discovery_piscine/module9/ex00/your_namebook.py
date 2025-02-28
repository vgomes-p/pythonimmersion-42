#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/28 09:29:04 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/28 09:29:04 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PyImmersion:
	@staticmethod
	def array_of_names(namelist):
		array = []
		for name, lastname in namelist.items():
			full_name = [name, lastname]
			full_name = " ".join(full_name).title()
			array.append(full_name)
		return array


persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(PyImmersion.array_of_names(persons))