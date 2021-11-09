mirai
---

## Steps

1. gobuster to discover directories and find php files

We find the page `/admin/`

2. default ssh login for raspberry pi + user flag

`pi:raspberry`

## Root Flag
1. Look at the history and run strings on it

`sudo cat /root/.bash_history`


Even though this box was super easy, it shows how default passwords can be likewise, so easily exploited, such as in the case of the Mirai botnet
