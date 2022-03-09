from requests import get
try:
    url = input("enter an url")
    response = get(url)
    if response!=None:
        print("valid")
except:
    print("url is invalid")
