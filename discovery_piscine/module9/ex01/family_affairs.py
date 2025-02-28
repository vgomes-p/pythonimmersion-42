#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 17:42:31 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 17:42:32 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



class PyImmersion:
	def is_red(name, dic):
			return dic[name] == "red"

	@staticmethod
	def find_the_redheads(family_members):
		redheads = list(filter(lambda name: PyImmersion.is_red(name, family_members), family_members))
		return redheads

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(PyImmersion.find_the_redheads(dupont_family))