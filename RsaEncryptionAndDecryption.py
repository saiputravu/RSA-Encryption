# RSA ENCRYPTION AND DECRYPTION PROGRAM
# Project started: 11 February 2017
# Project completed: 11 February 2017
# Project by Aditya Putravu


# Libraries required for the program
import random
import math

class Rsa:

    def __init__(self, e=0, d=0, n=0, p=23, q=47):

        # Hard coding the e, d and n values and lists

        self.e = e
        self.n = n
        self.d = d

        self.p = p
        self.q = q


# Check the GCD and coprimes.py file

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b  # If later the b ends up as 0 the pair are
        return a

    def coprime(self, a, b):
        return self.gcd(a, b) == 1  # Is it true or false

    # Encryption, decryption, and finding keys functions
    # Also an experimental and working(?) mod function

    def en(self, tuple_e, text):

        numarray = self.change_text_num(text)

        new_numarray = []

        for i in range(len(numarray)):
            new_numarray.append((int(numarray[i]) ** int(tuple_e[0])) % int(tuple_e[1]))  # The way to encrypt with RSA : Ciphered text
            # Algorithm to encrypt

        numarray = new_numarray  # As manipulating data while looping through it is a bad idea

        cipher = ' '.join(map(str, numarray)) # How the user sees the data

        return numarray, cipher  # Return numarray for error checking and ciphered text

    def de(self, tuple_d, numarray):

        new_numarray = []  # Create new list
        numarray = list(map(int, numarray.split()))

        for i in range(len(numarray)):
            
            new_numarray.append((int(numarray[i]) ** int(tuple_d[0])) % (tuple_d[1]))
            # The way to decrypt with RSA: Deciphered text


        numarray = new_numarray  # As manipulating data while looping through it is a bad idea

        # print(numarray)  # Error checking
        text, _ = self.change_num_text(numarray)  # Change the numbers to text

        return numarray, text  # return the numarray for error checking and decrypted text 

    def modular(self, num, mod, printanswer=False):  # If I ever forget the % symbol for mod or just for fun
        # Imagining num = 15 and mod = 4
        firstvar = num / mod  # Takes the 15 and divides by 3 to get decimal
        secvar = firstvar - int(firstvar)  # Keeps the decimal remainder as it will be x/3
        thirdvar = int((secvar * mod))  # Multiplies x by the 3 to get the whole number
        if printanswer:
            print(thirdvar)  # Prints out the correct answer
    
        return thirdvar

    def finding_keys(self, p, q):
        # P and Q are 2 primes

        self.n = p * q  # Working out the n value with given primes

    #   2 ways of working out phiN one with a for loop or one for bigger numbers, the formula

        method = 'null'  # Just for finding which of the 2 methods implemented are being used

        if self.n <= math.pow(2, 8):  # Limits how high that the number can be for this method
            coprimes = [i for i in range(1, self.n) if self.coprime(i, self.n)]  # Kept a list instead of counter to refer to the coprimes

            phiN = (len(coprimes))  # All the numbers below n and are coprimes

            method = 'Forloop'  # Just for finding which of the 2 methods implemented are being used
        else:
            phiN = (p-1) * (q-1)  # Actual formula for finding out how many
            method = 'Formula'  # Just for finding which of the 2 methods implemented are being used

        self.e = random.randint(2, phiN)  # Hard coding e with randomised variable

        while not self.coprime(self.e, self.n) or not self.coprime(self.e, phiN):
            self.e = random.randint(2, phiN)  # Until e meets requirements re-choose e

        d_values = [de for de in range(1, (5 * phiN)) if(de * self.e) % phiN == 1]  # For picking d from

        self.d = random.choice(d_values[1:])  # Not including the first one as that is the same for e and is too simple

    #    print(p, q, n, phiN, method, e, d, d_values)  # Error checking

        return self.n, self.e, self.d  # What needs to be known

    def change_text_num(self, text):

        # self.text = text.lower()

        textarray = []  # Clears text array
        numarray = []  # Clears num array


        for i in text:
            textarray.append(i)  # Fills text array with letters of the text

        for i in textarray:
            numarray.append(ord(str(i)))  # Changes the items in textarray to integers

        # print(self.textarray) # Prints text array
        # print(self.numarray) # Prints text array

        return numarray  # Returns numarray because changing text to numbers

    def change_num_text(self, numarray):

        textarray = []  # Clears text array

        for i in numarray:
            textarray.append((chr(i)))  # Fills text array with letters converted from numarray integers

        text = ""  # Clears text

        for i in textarray:
            text += str(i)  # Fills text with the appropriate letters

        # print(textarray)  # Prints the array of letters
        # print(numarray)
        # print(text)  # Prints the text

        return text, textarray  # Returns these lists


if __name__ == '__main__':
    print("Welcome to the RSA Ciphering program!\n  Made by Aditya Putravu")

    rsa = Rsa()
    while True:
        try:
            rsa.finding_keys(rsa.p, rsa.q)  # Generate keys

            enc = (rsa.e, rsa.n)  # Encryption Key (Private)
            dec = (rsa.d, rsa.n)  # Decryption Key (Public)

            e_or_d = input("Would you like to encrypt or decrypt?\n <e> || <d>\n")  # Asks to encrypt or decrypt

            if e_or_d.lower() == 'e':
                text = input("What text would you like to encrypt?\n ")  # The text to encrypt
                _, cipher = rsa.en(enc, text)  # Runs the encryption function
                print("Ciphered text:\n" + str(cipher))  # Takes the ciphered text and gives it to user
                print("The decryption key: ", dec)  # Prints the public decryption key
            elif e_or_d.lower() == 'd':
                d = int(input("What was the first number in the decryption key?\n"))
                n = int(input("What was the second number in the decryption key?\n"))
                dec = (d, n)  # Takes the decryption key because it always changes

                cipher = input("What would you like to decrypt?\n"
                          "<TIP: Copy and paste ciphered text (ignore space at beginning and ending)!>\n")


                _, text = rsa.de(dec, cipher)  # Runs decryption program
                print(text)  # Prints the decrypted message

            ans = str(input("Is that all?\n<y> || <n>\n"))  # To keep program running so you don't have to re-run manually
            if ans.lower() == 'y':
                break
            else:
                continue
        except Exception as e:  # All listings for errors
            print("OOPS! Something went wrong!\n%s\n" % e)
            print("\nRE-RUNNING\n")
