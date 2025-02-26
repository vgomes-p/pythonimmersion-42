#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_it.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 16:40:48 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/26 16:40:50 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args = sys.argv[1:2]

fargs = str(args).replace('[', '').replace(']', '').replace("'", "").lower()

print(f'The first parameter downcased is: {fargs}')