# Python Encryption and Decryption
def machine():
  keys = 'abcdefghijklmnopqrstuvwxyz |'
  value = keys[01] + keys[0:-1]
  
  encrypDict = dict(zip(keys, value))
  decryptDict = dict(zip(value, keys))
  
  message = input("Please enter your message")
  mode = input("Please select the mode ; E for Encode ; D for Decode")
  
  if mode.upper() == 'E':
    newMessage = ''.join([encyptDict[letter]
                          for letter in message.lower()])
  elif mode.upper() == 'D':
    newMessage = ''.join([decryptDict[letter]
                          for letter in message.lower()])
  else:
      print("Error: The choice does not exist")
      
  return newMessage
  
print(machine())
