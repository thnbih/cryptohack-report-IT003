import codecs

data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
decoded_data = codecs.decode(data, 'hex')

for key in range(256):
    decrypted_data = ''.join([chr(b ^ key) for b in decoded_data])
    if 'crypto' in decrypted_data:
        print(f'Key: {key} | Decrypted data: {decrypted_data}')
