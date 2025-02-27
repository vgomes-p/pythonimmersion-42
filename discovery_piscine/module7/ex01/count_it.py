#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/27 10:08:57 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/27 10:08:57 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

num_args = len(sys.argv) - 1

print(f'Number of parameters passed: {num_args}')
for pos in range (num_args):
	print(f'{sys.argv[pos + 1]}: {len(sys.argv[pos + 1])}')