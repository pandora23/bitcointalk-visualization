import os.path

import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web

import multiprocessing
import time
from itertools import product
import json
import urllib2
import urllib
import re
import csv
import signal
import re
from bs4 import BeautifulSoup

from tornado.options import define, options
define("port", default=8416, type=int)



def css_files(self):
    return "style.css"


#stop the main loop when I press CTRL-C usually        
def signal_handler(signum, frame):
    print(signum)
    tornado.ioloop.IOLoop.instance().stop()

signal.signal(signal.SIGINT, signal_handler)

#hosts the web page also an example get
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('page.html')

#example post        
class ExamplePost(tornado.web.RequestHandler):
    def post(self):
        
        returnPacket = {'datawhatever1':"blahblahblahjson"}
        self.write(returnPacket)
        self.finish()

if __name__ == '__main__':
    allData = Data();
    tornado.options.parse_command_line()
    app = tornado.web.Application( #connect url paths with handlers
            handlers=[(r'/',IndexHandler), (r'/example/', ExamplePost)],
            #template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname("__file__"), "static"),
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

