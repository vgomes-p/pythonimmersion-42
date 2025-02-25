#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    i_got_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgomes-p <vgomes-p@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/25 13:07:37 by vgomes-p          #+#    #+#              #
#    Updated: 2025/02/25 13:07:37 by vgomes-p         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("What you gotta say?")
while True:
	user = input(": ")
	if user != "STOP":
		print("I got that! Anything else?")
		continue
	elif user == "STOP":
		exit()