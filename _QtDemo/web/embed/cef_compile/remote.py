# coding:utf-8

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-03-13 10:27:56'

"""

"""

import sys
import time

# import sys
# MODULE = r"F:\Anaconda2\Lib\site-packages"
# if MODULE not in sys.path:
#     sys.path.append(MODULE)
# MODULE = r"F:\Anaconda2\Lib"
# if MODULE not in sys.path:
#     sys.path.append(MODULE)



import rpyc
from cefpython3 import cefpython as cef


def createBrowser():
    winId = int(sys.argv[1])
    windowInfo = cef.WindowInfo()
    windowInfo.SetAsChild(winId)


    settings = {}
    settings["context_menu"] = {
        "enabled": False,
        "navigation": False,  # Back, Forward, Reload
        "print": False,
        "view_source": False,
        "external_browser": False,  # Open in external browser
        "devtools": False,  # Developer Tools
    }
    cef.Initialize(settings)
    
    browser = cef.CreateBrowserSync(windowInfo,url="https://www.baidu.com")

    port = int(sys.argv[2])
    conn = None
    link_time = time.time()
    while True:
        
        cef.MessageLoopWork()

        # NOTE 用于保持 rpyc 的连接
        if time.time() - link_time < .5:continue
        link_time = time.time()

        if conn:
            try:
                url = conn.root.loadUrl()
            except:
                # NOTE 说明 rpyc 关闭 | 跳出循环
                break
            if url and url != browser.GetUrl():
                browser.LoadUrl(url)
            elif conn.root.resizeCall():
                cef.WindowUtils.OnSize(winId, 0, 0, 0)
        else:
            try:
                conn = rpyc.connect('localhost',port)
            except:
                pass
            
    cef.Shutdown()



if __name__ == "__main__":

    createBrowser()

    


    
