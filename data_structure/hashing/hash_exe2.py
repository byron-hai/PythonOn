#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""
# import the library module
import hashlib

# initialize a string
str = "www.MyTecBits.com"

# encode the string
encoded_str = str.encode()

# create sha3 hash objects initialized with the encoded string
obj_sha3_224 = hashlib.sha3_224(encoded_str)  # SHA3-224
obj_sha3_256 = hashlib.sha3_256(encoded_str)  # SHA3-256
obj_sha3_384 = hashlib.sha3_384(encoded_str)  # SHA3-384
obj_sha3_512 = hashlib.sha3_512(encoded_str)  # SHA3-512

# print in hexadecimal
print("\nSHA3-224 Hash: ", obj_sha3_224.hexdigest())
print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())
print("\nSHA3-384 Hash: ", obj_sha3_384.hexdigest())
print("\nSHA3-512 Hash: ", obj_sha3_512.hexdigest())