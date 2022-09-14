a = input("Input a letter of the alphabet: ")
if a.lower() in "aeiouy":
    print("{} is vowel".format(a))
else:
    print("{} is consonant".format(a))