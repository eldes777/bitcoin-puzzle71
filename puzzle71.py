#!/usr/bin/python3
#
# FORKED FROM:
# https://github.com/rouze-d/bitcoin-puzzle69

#-------------------------------------
# PLEASE DONATE TO ORIGINAL OWNER
#-------------------------------------

# PUZZLE 71 

import secp256k1 as ice
import random
#import bit

count=0
total=0

while True:
    num = random.randrange(1180591620717411303424, 2361183241434822606847)
    compress_address = ice.privatekey_to_address( 0, True, num)
    magic = hex(num)[2:].zfill(64)

    count+=1
    total+=1
    print(total, magic, compress_address, end='\r')

    if compress_address == "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU" :

        
        print('\nPrivate HEX     : ', magic)
        print('PrivateKey DEC  : ', num)
        print('Bitcoin Address : ', compress_address)
        print('')
        f=open('winner.txt','a')
        f.write('\nPrivateKey (DEC): ' + magic)
        f.write('\nBitcoin Address Compressed : ' + compress_address)
        f.close()
        exit()
