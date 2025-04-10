#!/usr/bin/python3
# https://github.com/rouze-d

import secp256k1 as ice
import random
#import bit

count=0
total=0

while True:
    num = random.randrange(295147905179352825856, 590295810358705651711)
    compress_address = ice.privatekey_to_address( 0, True, num)
    magic = hex(num)[2:].zfill(64)

    count+=1
    total+=1
    print(total, magic, compress_address, end='\r')

    if compress_address == "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG" :

        
        print('\nPrivate HEX     : ', magic)
        print('PrivateKey DEC  : ', num)
        print('Bitcoin Address : ', compress_address)
        print('')
        f=open('winner.txt','a')
        f.write('\nPrivateKey (DEC): ' + magic)
        f.write('\nBitcoin Address Compressed : ' + compress_address)
        f.close()
        exit()
