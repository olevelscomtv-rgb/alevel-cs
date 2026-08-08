# string = "helloaa"


# vowels = ["a","e","i","o","u"]


# count = 0
# for char in string: 
#     if char in vowels: 
#         count += 1 
#     else: continue

# print(count)





# def IterativeVowels(string: str) -> int : 
#     total = 0
#     lengthstring = len(string)
#     for i in range(lengthstring):
#         firstchar = string[0:1]
#         if firstchar == 'a' or firstchar == 'e'or firstchar == 'i' or firstchar == 'o' or firstchar == 'u':

#             total += 1 

#         string = string[1:]
#     return total

   
# print(IterativeVowels("eee"))
   











# vowels = ["a","e","i","o","u"]


# count = 0
# for char in string: 
#     if char in vowels: 
#         count += 1 
#     else: continue

# print(count)








def rec_vowels(string, total = 0):

    firstchar = string[0:1]
    if len(string) ==0:
        return total

    if firstchar == 'a' or firstchar == 'e'or firstchar == 'i' or firstchar == 'o' or firstchar == 'u':
        total += 1

    return rec_vowels(string[1:], total)

"eeefdoo"  "eefdoo"  "efdoo" "fdoo" "doo" "oo" "o" ""

print(rec_vowels("eeefdoo"))