# Solution

Loved this one!

1) Wireshark to find the offending entries
2) Decode the `support.php` file
3) Pass the parameters found in Wireshark to the decoded php shell
4) The output is a base64 encoded data
5) Upon decoding, you get a file, which is a kdbx file format
6) Use keepass2john tool to convert it to a hash crackable format
7) Run it through hashcat with cracklib-words
8) Open up the keepass kdbx file with the found password
9) The flag will be inside!

# Things learnt

To un-XOR a thing, XOR it with the results

a ^ b = c

c ^ b = a

How to use Hashcat, exposure to keepass, php coding. Excellent!
