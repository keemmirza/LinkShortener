import pyshorteners

def shorten(url):
    lurl = pyshorteners.Shortener()
    return lurl.tinyurl.short(url)

if __name__ == "__main__":
    link = input("Enter Website Link You Wish To Shorten : ")
    print(f"\n{shorten(link)}")