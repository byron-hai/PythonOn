#!/usr/bin/env python3
"""
@ Desc:
hashlib.algorithms_available   hashlib.sha256(
hashlib.algorithms_guaranteed  hashlib.sha384(
hashlib.blake2b(               hashlib.sha3_224(
hashlib.blake2s(               hashlib.sha3_256(
hashlib.md5(                   hashlib.sha3_384(
hashlib.new(                   hashlib.sha3_512(
hashlib.pbkdf2_hmac(           hashlib.sha512(
hashlib.scrypt(                hashlib.shake_128(
hashlib.sha1(                  hashlib.shake_256(
hashlib.sha224(

Functions associated :
    encode() : Converts the string into bytes to be acceptable by hash function.
    digest() : Returns the encoded data in byte format.
    hexdigest() : Returns the encoded data in hexadecimal format.

Note: Before hashing, encode for string is necessary
Reference: https://www.mytecbits.com/internet/python/sha3-hash-code

@ Author: Byron
@ Date: 
"""
import hashlib

str1 = "www.example.com"
str2 = "My password you can not guess"

encoded_str1 = str1.encode('utf-8')
encoded_str2 = str2.encode('utf-8')

sha3_256_str1 = hashlib.sha3_256(encoded_str1)
sha_512_str2 = hashlib.sha512(encoded_str2)
md5_str1 = hashlib.md5(encoded_str1)

print("SHA3-256 HASH of %s: %s" % (str1, sha3_256_str1.hexdigest()))
print("SHA-512 of %s: %s" % (str2, sha_512_str2.hexdigest()))
print("MD5 of %s: %s" % (str1, md5_str1.hexdigest()))

print("\ncompact version")
str3 = "This is a compact version"
print("String: '%s'\nsha3_512: %s" % (str3, hashlib.sha3_512(str3.encode()).hexdigest()))

print("\nUsing update()")
h_obj = hashlib.sha3_512()
h_obj.update(b'This is a ')
h_obj.update(b'compact version')
print("String: '%s'\nsha3_512 by update(): %s" % (str3, h_obj.hexdigest()))

print("\nUsing new()")
str3_md5 = hashlib.new("md5", str3.encode())
print("String: '%s'\nsha3_512 by new(): %s" % (str3, str3_md5.hexdigest()))
