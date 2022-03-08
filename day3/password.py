#! python
import sys,pyperclip

passwords = {
'email' : 'wjdwjd',
'fb' : 'jbdakudk'
    }
#sys.argv[0]->pw sys.argv[1]-> email

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
