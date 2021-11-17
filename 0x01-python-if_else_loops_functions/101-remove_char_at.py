#!/usr/bin/python3

def remove_char_at(str, n):
	str_cp = ""
	count = 0

	for i in str:
		count = count + 1

		if count == n:
			continue

		str_cp += str[i]

	return str_cp
