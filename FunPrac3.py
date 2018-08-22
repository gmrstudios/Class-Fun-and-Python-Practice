def show_magicians(Magicians):
    for magician in Magicians:
        print(magician)

def make_great(Magicians):
    for i in range(len(Magicians)):
        Magicians[i] = Magicians[i] + " The Great"
    return Magicians

Magicians = ['Houdini', 'Kellar', 'Thurston', 'Blackstone', 'Copperfield']

show_magicians(Magicians)

print("\nHere are all the great magicians:")

Great_Magicians = Magicians[:]

Great_Magicians = make_great(Great_Magicians)

show_magicians(Great_Magicians)

print("\nHere are all the magicians again:")

show_magicians(Magicians)






# Original version:
# def show_magicians(Magicians):
#     for magician in Magicians:
#         print(magician)
#
# def make_great(Magicians):
#     for i in range(len(Magicians)):
#         Magicians[i] = Magicians[i] + " The Great"
#
# Magicians = ['Houdini', 'Kellar', 'Thurston', 'Blackstone', 'Copperfield']
#
# show_magicians(Magicians)
#
# print("\nHere are all the great magicians:")
#
# make_great(Magicians)
#
# show_magicians(Magicians)

# failed attempt
# def make_great(Magicians):
#     count = 0
#     str = ""
#     print("\n Hello Great")
#     for magician in Magicians:
#         str = magician[count]
#         str = str + " The Great"
#         magician[count] = str
#         count +=1
#
#     for i in range(len(magicians)):
#         magicians[i] = "The Great" + magicians[i]
#     return Magicians
