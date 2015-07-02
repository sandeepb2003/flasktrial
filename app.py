
from flask import Flask
import socket
import redis
import subprocess
from docker import Client
from flask import Flask
import requests
from docker.client import Client
from docker.utils import kwargs_from_env
from flask.ext.bootstrap import Bootstrap
from flask import render_template,request
import json
from response import Info,Container,Version

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.debug = True

containerdata=""

@app.route('/<name>')
def details(name):
	r = redis.Redis(host="localhost",port="6379")
	val=r.get(name)
	dat=json.loads(val.decode('utf8'))
	info = Info(**dat)
	return render_template('index.html',info=info.__dict__)

@app.route('/containerdetails/<name>')
def containerdetails(name):
	r = redis.Redis(host="localhost",port="6379")
	val=r.get(name+"-container")
	print(val)
	dat=json.loads(val.decode('utf8'))
	print(type(dat))
	x = [Container(**i) for i in dat]
	return render_template('listdetails.html',info=x)

@app.route('/versiondetails/<name>')
def versiondetails(name):
	r = redis.Redis(host="localhost",port="6379")
	val=r.get(name+"-version")
	dat=json.loads(val.decode('utf8'))
	info = Version(**dat)
	#res=json.loads(val)
	return render_template('index.html',info=info.__dict__)



@app.route('/')
def index():
	r = redis.Redis(host="localhost",port="6379")
	val=r.keys(pattern="*")
	hosts = [x.decode('utf-8') for x in val if not '-' in x.decode('utf-8')] 
	return render_template('list.html',hostlist=hosts)



@app.route("/post/<name>/<val>")
def post(name,val):
	r = redis.Redis(host="localhost",port="6379")
	r.set(name,val)
	return "ok"

@app.route("/postdata",methods=['POST', 'GET'])
def info():
	r = redis.Redis(host="localhost",port="6379")
	if request.method=='POST':
		val = request.form['data']
		key=request.form['key']
		r.set(key,val)
		return "stored"

	return "ok"

@app.route("/containers",methods=['POST', 'GET'])
def container():
	r = redis.Redis(host="localhost",port="6379")
	if request.method=='POST':
		val = request.form['data']
		key=request.form['key']
		r.set(key+"-container",val)
		return "stored"

	return "ok"

@app.route("/version",methods=['POST', 'GET'])
def version():
	r = redis.Redis(host="localhost",port="6379")
	if request.method=='POST':
		val = request.form['data']
		key=request.form['key']
		r.set(key+"-version",val)
		return "stored"

	return "ok"

#hostname=socket.gethostname()
#variable = subprocess.Popen("curl http://127.0.0.1:2375/stdout",info=subprocess.PIPE,shell=True)
#data=variable.stdout.read()
#data=json.dumps(info)
#post(hostname,data)

def run_app_server():
	app.run(port=5000, debug=True, threaded=True, host='0.0.0.0')

if __name__ == '__main__':
	run_app_server()