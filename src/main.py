from session import Session
from sys import argv

if len(argv) < 2:
    raise AttributeError('path pour les logins SVP')

new_session = Session(argv[1])