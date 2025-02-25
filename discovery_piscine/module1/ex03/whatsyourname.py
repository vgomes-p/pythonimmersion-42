# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calledwhatsyourname.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 10:46:51 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/24 11:35:45 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first_name = input("What's your first name?\n: ").strip()
last_name = input("And your last name?\n: ").strip()
wl_name = first_name + " " + last_name
print(f"Well, pleased to meet you, {wl_name}.")