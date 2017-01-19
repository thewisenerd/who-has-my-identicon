who-has-my-identicon
====================


_you're ~~identicon is~~ not special. there are a lot of others ~~identicons~~
just like you._

howto
-----

 - generate hashes (a 1.2 gigabyte file with hashes of numbers from 1 to 30mil).

```bash
./hashgen.py > hashes
```

 - the generated hashes are of the format
```
<md5sum>	<userid>
```

 - install requests
```bash
pip install requests
```

 - generate regex from pattern.json or username
```bash
./generate_regex.py
./generate_regex.py username
```

 - grep hashes for same identicon (w/ different color)
```bash
grep -E $(./generate_regex.py) hashes
grep -E $(./generate_regex.py username) hashes
```

 - find username of user id by going to url
```
https://api.github.com/user/<userid>
```

example: [https://api.github.com/user/34610](https://api.github.com/user/34610)

why?
----

to find out how many lucky people have the smiley face identicon. well, it began
there.

![smiley face identicon](https://github.com/identicons/marnix.png)

the number of people who had the above identicon:
 - 760, when github userbase was 25 million
 - 932, when github userbase hits 30 million users

credits
-------
 - [stewartlord/identicon.js](https://github.com/stewartlord/identicon.js)
