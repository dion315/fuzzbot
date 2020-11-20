import json
import os
import random
import string
import requests
from art import tprint

print('-'*80)   
tprint('Welcome to Fuzzbot!', font='random')
print('-'*80)                    
url = input('Please enter target URL to post to: ')
user_argument = input('Enter the name of the argument used to pass the user name: ')
pass_argument = input('Enter the name of the argument used to pass the password: ')
firstinitial_switch = input('Is the first name to be abbreviated? (Y or N): ')
lastinitial_switch = input('Is the last name to be abbreviated? (Y or N): ')
specialswitch = input('Does email formatting require special charachters appended to end? (Y or N): ')
adddomain_switch = input('Does the username require a randomized eMail domain? (Y or N): ')
email_domain = input('If all emails should come from a common domain please enter it now, or leave blank for none: ')
send_limit = int(input('Please enter a number of fuzzing attempts to execute, enter 0 to run continuously: '))

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
while send_limit == send_limit :
    if firstinitial_switch == 'y':
        lower_upper_alphabet = string.ascii_letters
        username = random.choice(lower_upper_alphabet)
    else:
        firstname = json.loads(open('names.json').read())
        username = random.choice(firstname).lower()

    if lastinitial_switch.lower() == 'y':
        lower_upper_alphabet = string.ascii_letters
        username = username + random.choice(lower_upper_alphabet)
    else:
        lastname = json.loads(open('lastnames.json').read())
        username = username + random.choice(lastname).lower()
             
            
    if specialswitch.lower() == 'y':
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        name_extra = ''.join(random.choice(string.digits))
        username = username + name_extra
    else:
        pass

    if adddomain_switch.lower() == 'y':
        domainlist = json.loads(open('topemaildomains.json').read())
        email_domain = random.choice(domainlist)
    else:
        pass
    
    password = get_random_string(16)
    
    payload = {user_argument:username+email_domain, pass_argument:password}
    r = requests.post(url, allow_redirects=False, data=payload)
    print ('Sending username %s%s and password %s' % (username, email_domain, password))
    send_limit -= 1
    if send_limit == 0:
        break                   
