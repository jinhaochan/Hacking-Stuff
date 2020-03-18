# Solution

A bit of guesswork here, but basically

```
1) Base64 Decode
2) Inflate
3) openssl rsautl -decrypt -in <file> -inkeys <fixed_key>
```
