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
