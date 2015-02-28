#!/usr/bin/python2.7.9
#encoding: utf-8

import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		return "Hello Word"

if __name__ == "__main__":
	app.run()
