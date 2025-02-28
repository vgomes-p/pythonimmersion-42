#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 17:43:40 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 17:43:41 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PyImmersion:
	@staticmethod
	def famous_births(famous_list):
		sorted_famous = sorted(famous_list.items(), key=lambda item: int(item[1]["date_of_birth"]))
		for nick, info in sorted_famous:
			name = info["name"]
			year = info["date_of_birth"]
			print(f"{name} is a great scientist born in {year}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}


PyImmersion.famous_births(women_scientists)