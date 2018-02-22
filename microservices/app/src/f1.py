from flask import Flask, render_template,jsonify, redirect, url_for, request,make_response,abort
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('final1.html')

@app.route('/happiness')
def happiness():

    url = "https://data.chestnut27.hasura-app.io/v1/query"

    # This is the json payload for the query
    requestPayload = {
        "type": "select",
        "args": {
            "table": "happinessrepo",
            "columns": [
                "*"
            ]
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 39b0bfc7d2e483b74a2f35ad3754510e67641532d5a3a06c"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    return resp.content

@app.route('/q1/')
def hello_name():
   return  "Hello World - Anitha"
   
@app.route('/q2/')
def hello_name1():
   return  render_template('final.html')
@app.route('/author/')
def home():
    uri = "https://jsonplaceholder.typicode.com/users"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

  

    return render_template('author.html',authors=data)
@app.route('/post/')
def home1():
    uri = "https://jsonplaceholder.typicode.com/posts"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

  

    return render_template('post.html',posts=data)
@app.route('/count/')
def home2():
   uri1 = "https://jsonplaceholder.typicode.com/users"
   uri2 = "https://jsonplaceholder.typicode.com/posts"
   try:
       uResponse1 = requests.get(uri1)
       uResponse2 = requests.get(uri2)
   except requests.ConnectionError:
      return "Connection Error"  
   Jresponse1 = uResponse1.text
   Jresponse2 = uResponse2.text
   data1 = json.loads(Jresponse1)
   data2 = json.loads(Jresponse2)
   carr=[]
   for a in data1:
      ct=0
      d={}
      for p in data2:
         if a['id']==p['userId']:
            ct=ct+1	
      d['Name']=a['name']
      d['count']=ct
      carr.append(d)
   return render_template('count.html',res=carr) 
@app.route('/q3/')
def index1():
	return render_template('index.html')
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      age1 = request.form['age']
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   resp.set_cookie('Age', age1)
   return resp   

@app.route('/q4/')
def index2():
	return render_template('final2.html')   
@app.route('/getcookie/')
def getcookie():
   name = request.cookies.get('userID')
   age2 = request.cookies.get('Age')
   return '<h1> Stored key values:'+name+'with age '+age2+'</h1>'

@app.route('/q5/')
def index3():
	return render_template('final3.html')  	
@app.route('/robots1.txt/')
def login1():
    abort(403)	
@app.route('/robots.txt/')
def login():
    return redirect('http://httpbin.org/deny')
	
@app.route('/q6/')
def index4():
	return render_template('final4.html') 
@app.route('/html/')
def html1():
   return redirect('https://www.w3schools.com/html/')
@app.route('/image/')
def image1():
    return redirect('https://dab1nmslvvntp.cloudfront.net/wp-content/uploads/2016/03/1458289957powerful-images3.jpg') 	

@app.route('/q7/')
def index5():
	return render_template('final5.html') 
@app.route('/input/')
def index7():
   return render_template('q7.html')

@app.route('/result', methods = ['POST', 'GET'])
def setcookie1():
   if request.method == 'POST':
      user = request.form['nm']
      
   print(user)
   return user 

if __name__ == '__main__':
  app.run(debug=True)
