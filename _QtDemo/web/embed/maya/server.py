# coding:utf-8

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-03-14 23:54:08'

"""

"""
import sys
import rpyc
from rpyc import Service  
from rpyc.utils.server import ThreadedServer  


class TestService(Service):  
    resize = False
    url = None
    
    def exposed_onResizeCall(self):
        TestService.resize = True
        return TestService.resize

    def exposed_resizeCall(self):  
        if TestService.resize:
            TestService.resize = False
            return True

    def exposed_onLoadUrl(self,_url):
        TestService.url = _url

    def exposed_loadUrl(self):
        if TestService.url:
            _url = TestService.url
            TestService.url = None
            return _url


sr = ThreadedServer(TestService, port=int(sys.argv[1]), auto_register=False)  
sr.start()
