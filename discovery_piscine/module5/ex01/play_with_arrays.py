#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:09:25 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:09:25 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = original_array.copy()

for pos in range(len(new_array)):
	new_array[pos] += 2

print(f'''Original array: {original_array}
New array: {new_array}''')