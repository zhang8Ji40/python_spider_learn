import requests
from bs4 import BeautifulSoup

def testSoup():
    url = "https://game.maj-soul.net/1/"
    rsp = requests.get(url)
    if rsp.status_code != 200:
        print("status_code error:%u" % rsp.status_code)
        return
    htmlText = rsp.text
    majParser = BeautifulSoup(htmlText, "html.parser")  
    print(majParser.prettify)
    print(majParser.title)
    print(majParser.label.name)
    print(majParser.label.parent.name)
    labelTag = majParser.label
    print(labelTag.attrs['id'])
    print(type(labelTag.attrs))
    print(labelTag.string)
    print(len(majParser.head.contents))
    print(len(majParser.body.contents))
    '''
    for child in majParser.body.contents:
        print(child)
    '''
    #print(majParser.title.parent)
    print(majParser.link.next_sibling)
    


if __name__ == "__main__":
    testSoup()