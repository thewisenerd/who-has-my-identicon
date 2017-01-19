#!/usr/bin/env python3

import hashlib

usercount = (30 * (10 ** 6));

for i in range(1, usercount):
	x = str(i)
	print(hashlib.md5(x.encode('utf-8')).hexdigest() + "\t" + x)
