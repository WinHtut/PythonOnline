#CSPRNG 
#Cryptographically strong Pseudo-Random Number Generator
#random
#secrets 3.6 
# URL-safe test string
import secrets 
print('Printing integer number using secrets module')

passwordresetLink="https://winhtut.com/crazycoder/reset="
passwordresetLink += secrets.token_urlsafe(32)
print('Generating secure URL',passwordresetLink)

