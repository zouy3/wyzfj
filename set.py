import web
import lxml
import time
import os
from lxml import etree

class Set:
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.templates_root)
	def GET(self):
		return "get"
	def POST(self):
		return "post"