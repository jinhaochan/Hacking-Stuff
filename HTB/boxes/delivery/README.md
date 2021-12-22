delivery
---

## Steps

1. Get to important sites

ticket submission: `helpdesk.delivery.htb`

mattermost: `delivery.htb:8065`

2. Registering with Mattermost

When you submit a ticket, it says you can add more information by sending it to a specified email

Register with Mattermost and put in that specified email to get the confirmation link

Once there, go to the chat and get the SSH login and user.txt

## Root Flag

1. Hashcat

`cat /var/www/osticket/included/ost-ticket.php` to get the mysql credentials

`select * from ost_user_accounts`

Crack the hash to get root password



