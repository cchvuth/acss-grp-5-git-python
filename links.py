import urllib.request

def test_link():
    url = input("Enter a URL: ")
    try:
        a = urllib.request.urlopen(url, timeout=4).getcode()
        if a == 200:
            print("This link is live.")
    except:
        print("This link is dead.")
