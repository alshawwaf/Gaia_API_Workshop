#!/usr/bin/env python3

""" Simple code to Check the hostname using Gaia API"""

import sys
from cpapi import APIClient, APIClientArgs

def main():
    gaia_server = "203.0.113.81"
    username = "admin"
    password = "vpn123"

    client_args = APIClientArgs(server=gaia_server, context='gaia_api')
    with APIClient(client_args) as client:

        login = client.login(username, password)
        if not login.success:
            print(login.error_message)
            sys.exit(1)

        ###########################

        Check_hostname = client.api_call("show-hostname")

        print(Check_hostname)

        ###########################

if __name__ == "__main__":
    main()
