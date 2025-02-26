#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:09:48 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:09:49 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = original_array.copy()

for pos in range(len(new_array)):
	new_array[pos] += 2

modified_array = [pos for pos in new_array if pos > 5]

non_dup_array = []
seen = set()

for pos1 in modified_array:
	if pos1 not in seen:
		seen.add(pos1)
		non_dup_array.append(pos1)


non_dup_array = "{" + ", ".join(map(str, non_dup_array)) + "}"


print(f'''Original array: {original_array}
New array: {new_array}
Modified new array: {modified_array}
Non duplicated array: {non_dup_array}''')

