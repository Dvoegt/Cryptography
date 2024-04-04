import urllib.request
import hashlib
import random

# Retrieve a dictionary of potential words from a URL
dictionary = urllib.request.urlopen('https://gist.githubusercontent.com/PeterStaev/e707c22307537faeca7bb0893fdc18b7/raw/6c591618b8c0c46cb7db7a6966754455164cb433/PasswordDictionary.txt')
dictionary = dictionary.read()
dictionary = dictionary.decode("utf-8")

# A list of sample hashed passwords and their corresponding salts
entry = [('63328352350c9bd9611497d97fef965bda1d94ca15cc47d5053e164f4066f546828eee451cb5edd6f2bba1ea0a82278d0aa76c7003c79082d3a31b8c9bc1f58b','dbc3ab99'),('86ed9024514f1e475378f395556d4d1c2bdb681617157e1d4c7d18fb1b992d0921684263d03dc4506783649ea49bc3c9c7acf020939f1b0daf44adbea6072be6','fa46510a'),('16ac21a470fb5164b69fc9e4c5482e447f04f67227102107ff778ed76577b560f62a586a159ce826780e7749eadd083876b89de3506a95f51521774fff91497e','9e8dc114'),('13ef55f6fdfc540bdedcfafb41d9fe5038a6c52736e5b421ea6caf47ba03025e8d4f83573147bc06f769f8aeba0abd0053ca2348ee2924ffa769e393afb7f8b5','c202aebb'),('9602a9e9531bfb9e386c1565ee733a312bda7fd52b8acd0e51e2a0a13cce0f43551dfb3fe2fc5464d436491a832a23136c48f80b3ea00b7bfb29fedad86fc37a','d831c568'),('799ed233b218c9073e8aa57f3dad50fbf2156b77436f9dd341615e128bb2cb31f2d4c0f7f8367d7cdeacc7f6e46bd53be9f7773204127e14020854d2a63c6c18','86d01e25'),('7586ee7271f8ac620af8c00b60f2f4175529ce355d8f51b270128e8ad868b78af852a50174218a03135b5fc319c20fcdc38aa96cd10c6e974f909433c3e559aa','a3582e40'),('8522d4954fae2a9ad9155025ebc6f2ccd97e540942379fd8f291f1a022e5fa683acd19cb8cde9bd891763a2837a4ceffc5e89d1a99b5c45ea458a60cb7510a73','6f966981'),('6f5ad32136a430850add25317336847005e72a7cfe4e90ce9d86b89d87196ff6566322d11c13675906883c8072a66ebe87226e2bc834ea523adbbc88d2463ab3','894c88a4'),('21a60bdd58abc97b1c3084ea8c89aeaef97d682c543ff6edd540040af20b5db228fbce66fac962bdb2b2492f40dd977a944f1c25bc8243a4061dfeeb02ab721e','4c8f1a45')]

# Function to hash a given password using SHA-512
def hash_word(password):  
    hash_512 = hashlib.sha512()
    hash_512.update(password.encode())
    return(hash_512.hexdigest())

# Function to get a random word from the dictionary
def get_word():
    potential_words = dictionary.split()
    word = random.choice(potential_words)
    return word

# Function to perform character substitution in a word
def char_sub(word): 
    num = random.randrange(1,5)
    
    letters_to_change = ['a','s','o']
    letters_present = []
    change = {'a':'@', 's':'5','o':'0'} #potential letter swaps to be made

    no_lettersTo_change = True
    for letter in letters_to_change:

        if letter in word:
            no_lettersTo_change = False

    if no_lettersTo_change == True:
        return word
    
    for letter in word:
        if letter in letters_to_change:
            letters_present.append(letter)
            letters_to_change.remove(letter)

    ran_letter = random.choice(letters_present)
    word = word.replace(ran_letter, change[ran_letter], num)
    
    return word

# Function to add a suffix to a word (year of birth or month)
def add_suffix(word):
    yr_birth = str(random.randrange(1930,2020))
    month = str(random.randrange(1,12))
    if len(month) < 2:
        month = '0' + month

    suffix = random.choice([yr_birth, month])
    word = word + suffix
    return word

# Function to capitalize the first letter of a word
def capital_letter(word):
    return word.capitalize()

# Function to mangle a word by performing character substitution, adding a suffix, and capitalizing it
def mangle_word(word):
    word = char_sub(word)
    word = add_suffix(word)
    word = capital_letter(word)
    return word

# Mangle a random word from the dictionary, hash it, and store the result in hashed_mw
mangled_word = mangle_word(random.choice(dictionary.split()))
hashed_mw = hash_word(mangled_word)
print(hashed_mw)

#CODE BREAK


word_bank = dictionary.split()
combinations = []

# Function to replace every character in the word with possible substitutions
def replace_every_letter(word):
    word = word.capitalize()
    letters = ['a','s','o']
    letter_swap = {'a':'@','s':'5','o':'0'}
    for letter in letters:
        for repetitions in range(1,word.count(letter)+1):
            one_combo = word.replace(letter, letter_swap[letter], repetitions) #replace each letter that can be replaced in every combination possible and add to a list
            add_every_suffix(one_combo) #add every possible suffix to every possible combination of potential substitutions 

    if('a' not in word) and ('s' not in word) and ('o' not in word):
        add_every_suffix(word)

# Function to add every possible suffix (year or month) to a word
def add_every_suffix(word):

    for year in range(1920,2020):
        combinations.append(word + str(year))
    for month in range(1,13):
        if len(str(month)) < 2:
            month = '0' + str(month)

        combinations.append(word + str(month))



print('word to be guessed is: ',mangled_word)
#print('the hash of this is: ',hashed_mw)




for i in word_bank:
    replace_every_letter(i)

for i in combinations:
    
    if hash_word(i)== hashed_mw:
        print('The password is ', i)
        break

