#!/usr/bin/env python3
import requests

def download(url):
    """
    Download the file from the specified URL and stores it in the current directory
    url: the url to download the content of the page
    """

    #Check if the URL exists
    try:
        req = requests.get(url)
    except requests.execeptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    #Verify that the site was successfully accessed
    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input("Enter a URL: ")
    download(url)

