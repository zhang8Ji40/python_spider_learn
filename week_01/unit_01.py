import requests
import time


def test():
    resp = requests.get("http://www.bing.com")
    print(resp.status_code)
    print(type(resp))
    print(resp.headers)
    #print(resp.text)
    # print(resp.content)
    print(resp.encoding)
    print(resp.apparent_encoding)
    resp.encoding = resp.apparent_encoding
    #print(resp.text)
    rsp = requests.head("http://httpbin.org/get")
    print(rsp.headers)
    payload = {'a' : '1', 'b' : '2'}
    rsp = requests.post("http://httpbin.org/post", data = payload)
    print(rsp.text)
    rsp = requests.request("GET", "http://python123.io/ws", params=payload)
    print(rsp.url)
    rsp = requests.request("POST", "http://httpbin.org/post", data="test")
    print(rsp.text)
    hd = {'user-agent' : 'Chrome/10'}
    rsp = requests.request('POST', 'http://httpbin.org/post', headers=hd)
    print(rsp.text)
    filecontent = {"file": open('test.txt', 'rb')}
    rsp = requests.request('POST', 'http://httpbin.org/post', files=filecontent)
    print(rsp.text)


def getHtmlText(url):
    res = "test"
    try:
        rsp = requests.get(url)
    except Exception as ex:
        print(ex)
        res = "except"
    else:
        res = rsp.text
    finally:
        return res

def discuss():
    startTime = time.time()
    for proc in range(0,100):
        rsp = requests.get("http://www.bing.com")
        print(proc)
    endTime = time.time()
    print(endTime - startTime)
    

if __name__ == "__main__":
    url = "http://www.baidu.com"
    #print(getHtmlText(url))
    test()
    #discuss()
