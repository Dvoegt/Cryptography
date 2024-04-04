import hashlib

password = "f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a"

# The hashed password you're trying to find a match for
def brute_force(old_list):
    
    new_list = []
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for start_letter in alpha:
        for combo in old_list:
            potential_word = start_letter + combo  
            new_list.append(potential_word)

    return(new_list)

# Function to hash a given password using SHA-512
def hash_word(password):
    hash_512 = hashlib.sha512()
    hash_512.update(password.encode())
    return(hash_512.hexdigest())

# Function to check if a potential password hash matches the target hash
def check_match(potential_password, target_hash):
    pp_hashed = hash_word(potential_password)
    if (pp_hashed == target_hash):
        return True
    else:
        return False



#iteraties in shortlex order through all elements in old_list, hashes each option and compares to the target hash
def find_match(target_hash):
    # List of characters used for generating passwords
    old_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
    stop = False
    match = False

    #check hash of all passwords length 1
    for password in old_list:
        #hashed_word = hash_word(password)
        match = check_match(password, target_hash)
        if match == True:
            return password
            


    # check hash of passwords of length greater then 1
    if match == False:

    # Perform brute force password generation
        for i in range(10):
            old_list = brute_force(old_list)
            for word in old_list:   

                match = check_match(word, target_hash)
              
                if match == True:
                    break
            if match == True:
                break
       
    if match == True: 
        return(word)
    else:
        return(False)
    

#breaking hashed passwords
hashed_passwords = ['f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a','e85e639da67767984cebd6347092df661ed79e1ad21e402f8e7de01fdedb5b0f165cbb30a20948f1ba3f94fe33de5d5377e7f6c7bb47d017e6dab6a217d6cc24','4e2589ee5a155a86ac912a5d34755f0e3a7d1f595914373da638c20fecd7256ea1647069a2bb48ac421111a875d7f4294c7236292590302497f84f19e7227d80','afd66cdf7114eae7bd91da3ae49b73b866299ae545a44677d72e09692cdee3b79a022d8dcec99948359e5f8b01b161cd6cfc7bd966c5becf1dff6abd21634f4b']
for hp in hashed_passwords:
    results = find_match(hp)
    print('The password is ', results)


