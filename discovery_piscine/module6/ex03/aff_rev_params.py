#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 16:42:56 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/26 16:42:56 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

rev_args = sys.argv[1:][::-1]
num_args = len(sys.argv) - 1

if int(num_args) <= 0:
	print('none')
else:
	print(f'Your parameter reversed are:')
	print("\n".join(rev_args).replace('[', '').replace(']', '').replace("'", '').replace('"', ''))