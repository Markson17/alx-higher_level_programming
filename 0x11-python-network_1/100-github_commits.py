#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Arguments: arg1: repo name, arg2: repo owner"""
import requests
import sys



if __name__ == "__main__":
    # Get the arguments, arg1: repo name, arg2: repo owner
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            com = commits[i]
            print(f"{com['sha']}: {com['commit']['author']['name']}")
    except IndexError:
        pass
