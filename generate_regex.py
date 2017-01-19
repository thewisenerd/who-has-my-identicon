#!/usr/bin/env python

import requests
import hashlib

import json
import sys

fg = "[0|2|4|6|8|a|c|e]"
bg = "[1|3|5|7|9|b|d|f]"
hexchar = "[0-9a-f]"

pattern = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]
];

matchHSL = None;

regex = "^";

def getPatternFile(filename):
	global pattern

	data = None
	with open(filename) as data_file:
		try:
			data = json.load(data_file)
		except:
			print("pattern loading failed")
			exit()

	if data['pattern'] is None:
		print("invalid pattern file")
		exit()

	pattern = data['pattern']

def getUserPattern(username):
	global pattern

	r = requests.get('https://api.github.com/users/' + username)

	if (r.status_code != 200):
		if (r.status_code == 404):
			print ("404 not found");
		else:
			print ("failed to connect to github API; err code = ", r.status_code)
		exit()

	try:
		j = r.json()
	except:
		print ("failure decoding json response")
		exit()

	if j['id'] is None:
		print ("failure decoding json response")
		exit()

	userid = str(j['id'])
	userhash = hashlib.md5(userid.encode('utf-8')).hexdigest()

	for i in range(0, 15):
		try:
			c = int( '0x' + userhash[i], 16 )
		except:
			print ("failure converting hex to decimal")
			exit()

		c = (c+1) % 2;
		if (i < 5):
			pattern[i][2] = c;
		elif (i < 10):
			pattern[i-5][1] = c;
			pattern[i-5][3] = c;
		else:
			pattern[i-10][0] = c;
			pattern[i-10][4] = c;

if (len(sys.argv) > 1):
	getUserPattern(sys.argv[1])
else:
	getPatternFile("pattern.json")

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
