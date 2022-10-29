def is_valid_password(password):
    
    SpecialSym =['!', '@', '#', '$', '%', '&', '*']
    val = True
      
    if len(password) < 6:
        val = False
          
    if len(password) > 20:
        val = False
          
    if not any(char.isdigit() for char in password):
        val = False
          
    if not any(char.isupper() for char in password):
        val = False
          
    if not any(char.islower() for char in password):
        val = False
          
    if not any(char in SpecialSym for char in password):
        val = False
    if val:
        return val

    return False    

def main():
    # Repeatedly ask the user for a password until they enter one that we
    # consider to be valid/secure.
    
    password = input("Enter a password: ")
    while not is_valid_password(password):
        print("Sorry, that password is not secure. Please try again.")
        password = input("Enter a password: ")
    print("That password is secure.")
    
main()
