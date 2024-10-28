# a password checker to check if your password has ever been hacked

import requests
import hashlib
import sys 

# hashing a password is something u should always do never store plain text
# hashing is a 1 way function u cant reverse it
# we want to send the hashed version of our password
# the pwned api uses k anonimity allows someonet to receive info about us but still not know who u are we only give the first 5 characters of our hash and it has a list of all the passwords leaked and those passwords are stored with the sha1 algo so it looks in the database and picks the one with the first 5 characters matching it

# idempotent - a function given the same input always output the same output




def request_api_data(query_char):

    # we give it the first 5 characters of our hashed function
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check api and try again')

    return response




def get_password_leaks_count(hashes, hash_to_check):
    # the num of times it was pawned is after the column
    # this converts into a tuple that has hash and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    
    for hash,  count in hashes:
        if hash == hash_to_check:
            return count 
    return 0

def pwned_api_check(password):
    # check password if it exits in api response
    # run password thru sha1 algorithm
    
    # u must encode before hashing

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print('first', first5_char)
    # print('tail', tail)
    return get_password_leaks_count(response, tail)




def main(args):
    for password in args:
        count =  pwned_api_check(password)
        if count:
            print(f'{password} The password is found {count} you should probably change it')
            
        else:
            print(f'{password} was not found  you are all good to go')
            
    return 'done'




if __name__ == '__main__':
    # sys.exit is to exit the process incase if it does not exit 
    sys.exit(main(sys.argv[1:]))




