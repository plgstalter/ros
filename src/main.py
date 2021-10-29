from session import Session
from sys import argv

if len(argv) < 2:
    raise AttributeError('pas de client id :(')


new_session = Session(argv[1])
new_session.grant_access()