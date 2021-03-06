#!/usr/bin/env python
# -*- coding: utf-8 -*-

from admin import C224eAdmin
from user import C224eUser
import signal
import sys
if __name__ == "__main__":
    # Create administrator and user object
    admin = C224eAdmin()
    user = C224eUser()

    #Do some magic to make sure we always log out, otherwise we might block the printer
    def signal_handler(signal, frame):
        admin.logout()
        user.logout()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    try:
        admin.login('password', 'printer.hostname')

        #Let's create some test accounts
        admin.createUser('testUser', 'test123')
        admin.setLimits('testUser', 111, 222, 'abs')
        admin.setLimits('testUser', 9, 8, 'inc')
        admin.getUserByName('testUser')

        #And test some user stuff
        user.login('user', 'password', 'printer.hostname')
        user.getLimits()

    finally:
        admin.logout()
        user.logout()