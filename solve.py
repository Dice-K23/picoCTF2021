import string

alphabets = string.ascii_lowercase

crypt = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"


for c in crypt:
    if c.isupper():
        print(alphabets[(alphabets.index(c.lower())+13)%26].upper(), end="")

    elif c.islower():
        print(alphabets[(alphabets.index(c)+13)%26], end="")

    else:
        print(c, end="")

print()