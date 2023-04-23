from pwn import xor

s = "label"
key = 13
result = xor(s, key)
print(result)
