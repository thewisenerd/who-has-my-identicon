#!/usr/bin/env python3

# b9af39401fe82240a310644c54100e87
# b9af3
# 9401f
# e8224
# 1 0 0 0 1
# 1 1 0 1 1
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1

fg = "[0|2|4|6|8|a|c|e]"
bg = "[1|3|5|7|9|b|d|f]"
hexchar = "[0-9a-f]"

pattern = [
 [1, 0, 0, 0, 1],
 [1, 1, 0, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1],
 [1, 0, 0, 0, 1]
];

matchHSL = None;
# matchHSL = "4100e87";

regex = "^";

for i in range(0, 5):
	if (pattern[i][2]):
		regex += fg;
	else:
		regex += bg;

for i in range(0, 5):
	if (pattern[i][1]):
		regex += fg;
	else:
		regex += bg;

for i in range(0, 5):
	if (pattern[i][0]):
		regex += fg;
	else:
		regex += bg;

if matchHSL is not None:
	regex += hexchar
	regex += "{10}"
	regex += matchHSL

print (regex, end="")
