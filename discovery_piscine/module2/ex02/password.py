#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:06:44 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:06:44 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = "Python is awesome"


checkpass = input("Type your password: ")
if checkpass == password:
	print("ACCESS GRANTED!")
else:
	print("ACCESS DENIED!")