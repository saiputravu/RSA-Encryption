import random
from math import *


class Rsa:

    def __init__(self):
        self.__name__ = 'second'
        self.p, self.q = self.finding_p_and_q()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = 0

    def is_prime(self, n):
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False

        return True

    def mod_reverse(self, phi, e):
        pos00 = self.phi
        pos01 = self.phi
        pos10 = self.e
        pos11 = 1
        newpos10 = 0

        a =0

        while newpos10 != 1:
            # print('Doing mod thingy', a)
            pos00pos10int = floor(pos00 / pos10)
            inttimespos10 = pos00pos10int * pos10
            inttimespos11 = pos00pos10int * pos11

            newpos10 = pos00 - inttimespos10
            newpos11 = pos01 - inttimespos11
            if newpos10 < 0:
                newpos10 %= phi
            if newpos11 < 0:
                newpos11 %= phi

            pos00 = pos10
            pos01 = pos11
            pos10 = newpos10
            pos11 = newpos11

            # print(pos00, pos10, pos01, pos11)
            # print(newpos10, newpos11)
            if newpos10 == 1:
                break
            a+=1

        return newpos11

    def encrypt_msg(self, msg, n, e):
        msg = list(map(str, msg))
        ascii = []
        encrypted = []
        print("Encrypt ran")
        for char in msg:
            ascii.append(ord(char))

        for char in ascii:
            encrypted.append(str((char**e) % n))



        return ','.join(encrypted)

    def decrypt_msg(self, msg, n, d):
        msg = list(msg.split(','))
        ascii = []
        decrypted = []

        for num in msg:
            ascii.append(int(num)**d % n)

        for char in ascii:
            decrypted.append(chr(int(char)))

        return ''.join(decrypted)

    def coprime(self, a, b):
        return gcd(a, b) == 1

    def finding_p_and_q(self):
        a = random.randint(10,100)
        while not self.is_prime(a):
            a = random.randint(10,100)

        b = random.randint(10,100)
        while not self.is_prime(b):
            b = random.randint(10,100)
        return a, b

    def generate_keys(self, p, q):


        # print("Phi value", self.phi)
        # print(self.phi)
        for i in range(self.phi):
            # print(i, self.phi, self.is_prime(i), self.coprime(i, self.phi))
            if self.is_prime(i) and self.coprime(i, self.phi):
                self.e = i
        # print(e ,'is e ')
        self.d = self.mod_reverse(self.phi, self.e)
        # print(self.d)

        while self.e == self.d:
            # print(p, q)
            self.p, self.q = self.finding_p_and_q()

            while self.p == self.q:
                self.p, self.q = self.finding_p_and_q()
                self.n, self.e, self.d = self.generate_keys(self.p, self.q)
        return self.phi, self.e, self.d

# elif e != d:
#     return n, e, d


# p = 0
# ,85,21,21,1221,2422,2285,85,21,1221'



# n, e, d = generate_keys(p, q)


# print(encryptMsg(msg, n, e))
# print(decryptMsg(msg1, 3071, 227))
#
a = Rsa()
p, q = a.finding_p_and_q()
n,e,d = a.generate_keys(p, q)
remebe = a.encrypt_msg('Hello', n, e)
print(remebe, n, d)
print(a.decrypt_msg('288,1005,1193,336,128,15,2087,336,1193,15,845,1824,336,1233,128,336,1233,1440,1440,747,1104,1233,1824'
                    ,2704, 2163))