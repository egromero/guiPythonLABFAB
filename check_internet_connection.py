import urllib.request


def check():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
    
    
