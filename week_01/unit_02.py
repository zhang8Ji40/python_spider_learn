import requests
import os


def getText(url, hd):
    try:
        rsp = requests.get(url, hd)
        rsp.raise_for_status()
        rsp.encoding = rsp.apparent_encoding
        print(rsp.text[:1000])
        # print(rsp.request.headers)
    except Exception as ex:
        print(ex)


def searchBing(key):
    url = "https://cn.bing.com/s"
    searchKey = {"q": key}
    rsp = requests.get(url, params=searchKey)
    print(rsp.status_code)
    print(rsp.request.url)
    print(len(rsp.text))
    print(rsp.text[:1000])


def savePic():
    url = "https://cn.bing.com/th?id=OHR.AschauChiemgau_ZH-CN1929016406_1920x1080.jpg&rf=LaDigue_1920x1080.jpg"
    saveDir = "pic/"
    filePath = saveDir + url.split("=")[-1]
    try:
        if not os.path.exists(saveDir):
            os.mkdir(saveDir)
        rsp = requests.get(url)
        print(rsp.status_code)
        with open(filePath, 'wb') as fd:
            fd.write(rsp.content)
            fd.close
    except Exception as ex:
        print("spider pic faild")
        print(ex)


if __name__ == "__main__":
    url = "https://item.jd.com/12898878.html"
    hd = {'user-agent': 'Chrome/10'}
    #getText(url, hd)
    # searchBing("zhang8jiao")
    savePic()
