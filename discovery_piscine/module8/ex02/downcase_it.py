#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_it.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 14:30:37 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 14:30:37 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class PyImmersion:
	@staticmethod
	def downcase_it():
		args = sys.argv[1:]
		fargs = str(args).replace('[', '').replace(']', '').replace("'", "").lower()

		if len(sys.argv) - 1 <= 0:
			print("none")
		else:
			print(f'The parameters downcased are: {fargs}')

PyImmersion.downcase_it()