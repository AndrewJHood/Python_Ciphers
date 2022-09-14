# Function to decrypt caesar cipher
def caesar_decrypt(secret_message, offset):
  # Error Handling
  if not(type(offset) == type(0)):
    return("Error! Offset is of type {dt}. Expected: int".format(dt=type(offset)))
  if not(type(secret_message) == type("str")):
    return("Error! Argument secret_message is of type {dt}. Expected: str".format(dt=type(secret_message)))
  # Checking for offset of 0
  if offset == 0:
    return secret_message
  # Local variable to hold final message
  decrypted_message = ""
  # Iterate through each character in string
  for letter in secret_message:
    # Checking for special characters such as punctuation
    if (ord(letter) > ord('z') or ord(letter) < ord('a')) and (ord(letter) > ord('Z') or ord(letter) < ord('A')):
      decrypted_message += letter
      continue
    # If offset > 0 then shift right
    if offset > 0:
      decrypted_letter = chr(ord(letter) + offset)
      # Standardized variable to determine distance from 'z' to letter
      overflow_control = ord('z') - ord(letter)
    # If offset < 0 then shift left
    if offset < 0:
      decrypted_letter = chr(ord(letter) + offset)
      # Standardized variable to determine distance from letter to 'a'
      overflow_control = ord(letter) - ord('a')
    # If decrypted letter falls outside of the alphabet
    if overflow_control < abs(offset):
      overflow_control = abs(offset) - overflow_control
      # If decrypted letter goes beyond upper bound ('z')
      if offset > 0:
        decrypted_letter = chr(ord('a') + overflow_control - 1)
      # If decrypted letter falls below lower bound ('a')
      if offset < 0:
        decrypted_letter = chr(ord('z') - overflow_control + 1)
    # Build decrypted message
    decrypted_message += decrypted_letter
  # Return final message
  return decrypted_message

# Function to encrypt a message using caesar cipher
def caesar_encrypt(message, offset):
  # Error Handling
  if not(type(message) == type("str")):
    return("Error! Argument message is of type {dt}. Expected: str".format(dt=type(message)))
  if not(type(offset) == type(0)):
    return("Error! Offset is of type {dt}. Expected: int".format(dt=type(offset)))
  # Remove capitalization to add security
  message = message.lower()
  # Checking for offset of 0
  if offset == 0:
    return message
  # Local variable to hold final message
  encrypted_message = ""
  # Iterate through each character in string
  for letter in message:
    # Checking for special characters such as punctuation
    if (ord(letter) > ord('z') or ord(letter) < ord('a')) and (ord(letter) > ord('Z') or ord(letter) < ord('A')):
      encrypted_message += letter
      continue
    # If offset > 0 then shift left
    if offset > 0:
      encrypted_letter = chr(ord(letter) - offset)
      # Standardized variable to determine distance from 'z' to letter
      overflow_control = ord(letter) - ord('a')
    # If offset < 0 then shift right
    if offset < 0:
      encrypted_letter = chr(ord(letter) + offset)
      # Standardized variable to determine distance from letter to 'a'
      overflow_control = ord('z') - ord(letter)
    # If encrypted letter falls outside of the alphabet
    if overflow_control < abs(offset):
      overflow_control = abs(offset) - overflow_control
      # If encrypted letter goes beyond upper bound ('z')
      if offset < 0:
        encrypted_letter = chr(ord('a') + overflow_control - 1)
      # If encrypted letter falls below lower bound ('a')
      if offset > 0:
        encrypted_letter = chr(ord('z') - overflow_control + 1)
    # Build decrypted message
    encrypted_message += encrypted_letter
  # Return final message
  return encrypted_message

# Function to decrypt an encrypted message using a Vigenere Cipher
def vig_decrypt(secret_message, keyword):
  # Error handling
  if not type(secret_message) == type(""):
    return "Error! Secret Message is of type: {}; Expected type: {}".format(type(secret_message), type(""))
  if not type(keyword) == type (""):
    return "Error! Keyword is of type: {}; Expected type: {}".format(type(keyword), type(""))
  # Local variable to hold final encrypted message
  encrypted_message = ""
  # Local variable to hold shift value of keyword index
  shift = 0
  # Iterate through each character of secret message
  for index in range(len(secret_message)):
    # Checking for special characters such as punctuation
    if ord(secret_message[index]) > ord('z') or ord(secret_message[index]) < ord('a'):
      encrypted_message += secret_message[index]
      # Allows keyword to keep index while secret_message skips special character
      shift -= 1
      continue
    # Grabbing ASCII value of letter in each string
    key_letter_index = ord(keyword[(index + shift) % len(keyword)])
    secret_letter_index = ord(secret_message[index])
    # Checking for new character passing upper bound
    if secret_letter_index + key_letter_index - ord('a') > ord('z'):
      # Adds new character to final message 
      encrypted_message += chr(secret_letter_index + key_letter_index - ord('z') - 1)
    else:
      # Adds new character to final message
      encrypted_message += chr(secret_letter_index + key_letter_index - ord('a'))
  # Returns final message
  return encrypted_message

# Function to encrypt a secret message using a Vigenere Cipher
def vig_encrypt(secret_message, keyword):
   # Error handling
  if not type(secret_message) == type(""):
    return "Error! Secret Message is of type: {}; Expected type: {}".format(type(secret_message), type(""))
  if not type(keyword) == type (""):
    return "Error! Keyword is of type: {}; Expected type: {}".format(type(keyword), type(""))
  # Remove capitalization to add security
  secret_message = secret_message.lower()
  # Local variable to hold final encrypted message
  decrypted_message = ""
  # Local variable to hold shift value of keyword index
  shift = 0
  # Iterate through each character of secret message
  for index in range(len(secret_message)):
    # Checking for special characters such as punctuation
    if ord(secret_message[index]) > ord('z') or ord(secret_message[index]) < ord('a'):
      # Remove punctuation to add security
      if not (secret_message[index] == ' '):
        decrypted_message += ''
      else:
        decrypted_message += ' '
      # Allows keyword to keep index while secret_message skips special character
      shift -= 1
      continue
    # Grabbing ASCII value of letter in each string
    key_letter_index = ord(keyword[(index + shift) % len(keyword)])
    secret_letter_index = ord(secret_message[index])
    # Checking for new character passing upper bound
    if secret_letter_index - key_letter_index < 0:
      # Adds new character to final message 
      decrypted_message += chr(ord('z') + secret_letter_index - key_letter_index + 1)
    else:
      # Adds new character to final message 
      decrypted_message += chr(ord('a') + secret_letter_index - key_letter_index)
  return decrypted_message

# Sample function calls
# print(caesar_encrypt("Hello world", 5))
# print(caesar_decrypt(caesar_encrypt("Hello world", 5), 5))
# print(vig_encrypt("This is a sample call to the Vigenere encryption function", "cryptography"))
# print(vig_decrypt(vig_encrypt("This is a sample call to the Vigenere encryption function", "cryptography"),"cryptography"))

# Error Testing
# print(caesar_encrypt("Hello world", "Hello world"))
# print(caesar_encrypt(5, "Hello world"))
# print(vig_encrypt(0, "friends"))
# print(vig_encrypt("you were able to decode this? nice work! you are becoming quite the expert at crytography!", 0))