import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(text,shift):
#     encoded_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         new_position = (position + shift) % 25
#         encoded_text += alphabet[new_position]
#     print(f"The encoded text is {encoded_text}")

# def decrypt(text,shift):
#     decoded_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         new_position = (position - shift) 
#         if new_position < 0:
#             new_position += 25
#         decoded_text += alphabet[new_position]
#     print(f"The decoded text is {decoded_text}")


def ceaser(text,shift,direction):
    coded_text = ""
    for i in text:
        if i in alphabet:

            position = alphabet.index(i)
            shift = shift % 25
            if direction == 'encode':
                new_position = (position + shift) % 25 
            elif direction == 'decode':
                new_position = (position - shift) 
            if new_position < 0:
                new_position += 25
            coded_text += alphabet[new_position]
        else:
            coded_text += i
    print(f"The {direction}d text is {coded_text}")  


again = True
while (again == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction)
    ask = input("Type yes if you want to run again else type no " )
    if ask == 'no':
        again = False
        print("GoodBye")
    elif ask == 'yes':
        again == True

