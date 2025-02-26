#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_first_param.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 16:26:52 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/26 16:26:56 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args = sys.argv[1:2]

fargs = str(args).replace('[', '').replace(']', '').replace("'", "")


print(f'The first parameter is: {fargs}')