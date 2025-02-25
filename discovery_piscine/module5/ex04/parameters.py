#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameters.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:10:00 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:10:00 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

num_args = len(sys.argv) - 1
args = sys.argv[1:]

argstr = str(args).replace('[', '').replace(']', '')

print(f'''Number of parameters: {num_args}
Your arguments were: {argstr}''')