#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 14:30:45 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 14:30:45 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class PyImmersion:
	@staticmethod
	def greetings(entry=None):
		if entry is None or entry == "":
			print(f"Hello, noble stranger.")
		elif isinstance(entry, int) or (isinstance(entry, str) and entry.isdigit()):
			print(f"It was not a name")
		else:
			print(f"Hello, {entry}.")

PyImmersion.greetings('Alexandra')
PyImmersion.greetings('Wil')
PyImmersion.greetings()
PyImmersion.greetings(42)