#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011 Hunter Lang
#
# MIT Liscence
import os.path
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.template as template
from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
			(r"/", IndexHandler),
			(r"/upload/([A-Za-z0-9\_\.\-]+)", UploadHandler),
			(r"/undefined", ErrorHandler),
        ]
        
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings) 
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
		items = []
		for filename in os.listdir("upload/"):
			items.append(filename)
		self.render('static/index.html', items=items)
    def post(self):
    	file_content = self.request.files['datafile'][0]['body']
    	file_name = self.request.files['datafile'][0]['filename']
    	x = open("upload/" + file_name, 'w')
    	x.write(file_content)
    	x.close()
    	self.redirect("/")
class UploadHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self, filename):
		x = open("upload/" + filename)
		self.set_header('Content-Type', 'text/csv')
		self.set_header('Content-Disposition', 'attachment; filename=' + filename)
		self.finish(x.read())
class ErrorHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		self.redirect('/')
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()
