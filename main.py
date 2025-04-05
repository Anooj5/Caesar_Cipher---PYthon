    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text1,shift1,direction1):
    str=''
    if direction1 == 'decode':
        shift1*=-1
    for i in text1:
      if i in alphabet:
        position = alphabet.index(i)
        new_position = (position+ shift1)%len(alphabet)
        str+=alphabet[new_position]
      else:
        str+=i
    print(f"The {direction1}d result is {str}")

true = True
while true:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text1 = text,shift1 = shift,direction1 = direction)
    
    result = input("Type 'yes' to do it again. Otherwise type 'no'\n")
    if result == 'no':
        true = False
    else:
        print('Wrong input')

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
'''def encrypt(text1,shift1):

    str=""
    for i in text1:
        position = alphabet.index(i)
        new_position = (position+ shift1)%len(alphabet) 
        str += alphabet[new_position]
    print(f'The encoded text is {str}')


#encrypt(text1=text,shift1=shift)

def decrypt(text1,shift1):
    str=""
    for i in text1:
        index1 = alphabet.index(i)
        new_position = (index1 - shift) % len(alphabet)
        str += alphabet[new_position]
    print(f"The decoded text is {str}")
#decrypt(text1 = text,shift1 = shift)

if direction == 'encode':
    encrypt(text1=text,shift1=shift)
elif direction == 'decode':
    decrypt(text1 = text,shift1 = shift)
else:
    print(Nothing)
'''
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 