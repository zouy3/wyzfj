# -*- coding: utf-8 -*-
from flask import *
import time
import hashlib
from lxml import etree

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/weixin/', methods = ['GET', 'POST'])
def whatusay():
	if request.method == 'GET':
		token = r'hahaha'
		data = request.args
		signature = data.get('signature','')
		timestamp = data.get('timestamp','')
		nonce = data.get('nonce','')
		echostr = data.get('echostr','')
		list = [timestamp,nonce,token]
		list.sort()
		s = list[0]+list[1]+list[2]
		code = hashlib.sha1(s.encode('utf-8')).hexdigest()
		if code == signature:
			return make_response(echostr)
		else:
			return "hello"
	xml_recv = etree.fromstring(request.data)
	TUN = xml_recv.find("ToUserName").text
	FUN = xml_recv.find("FromUserName").text
	Con = xml_recv.find("Content").text
	reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
	response = make_response(reply % (FUN, TUN, str(int(time.time())),  Con))
	return response




if __name__=='__main__':
	app.run()