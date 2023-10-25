from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from . import models
import requests
import json

# Create your views here.


def login(request):
	print (request.session)
	request.session.flush()
	return render(request,'login.html',{})

def logout(request):
	request.session.flush()
	return render(request,'login.html',{})

def checkusername(request):
	print(request.body)
	code = 500
	message = 'server error'
	json_data = json.loads(request.body)
	username = json_data['username']	
	if username != '':
		user = models.Reader.objects.filter(username=username)
		if not user:
			code = 403
			message = 'forbbiden'
		else:
			code = 200
			message = user[0].username
			print(user[0].username)
			request.session["valid"] = True
			request.session["username"] = message

	return JsonResponse({'code':code,'message':message})

def newuser(request):
	json_data = json.loads(request.body)
	username = json_data['username']
	code = 500
	if username != '':
		reader = models.Reader(username=username)
		reader.save()
		code = 200
	return JsonResponse({'code':code})

def main(request):
	if request.session.get("valid",False):
		view = 'main.html'
		return render(request,'main.html',{})
	else:
		request.session.flush()
		return redirect('login')

def register(request):
	request.session.flush()
	return render(request,'register.html',{})


def more(request,isbn):
	if request.session.get("valid",False):
		r = requests.get('https://openlibrary.org/api/books?bibkeys=ISBN:'+str(isbn)+'&format=json&jscmd=details', params=request.GET)
		result_json = r.json()
		print(result_json['ISBN:'+str(isbn)])
		title = result_json['ISBN:'+str(isbn)]['details']['title']
		author = result_json['ISBN:'+str(isbn)]['details']['authors'][0]['name']
		publish_date = result_json['ISBN:'+str(isbn)]['details']['publish_date']
		if 'description' in result_json['ISBN:'+str(isbn)]['details']:
			description = result_json['ISBN:'+str(isbn)]['details']['description']
		else:
			description = 'No Description'
		return render(request,'more.html',{'title':title,'author':author,'publish_date':publish_date,'description':description,'isbn':isbn})
	else:
		request.session.flush()
		return redirect('login')

def mylist(request):
	if request.session.get("valid",False):
		username = request.session.get("username",False)
		if username:
			user = models.Reader.objects.filter(username=username)
			books = list(user[0].books.all().values())
			print(books)
			return render(request,'mylist.html',{'books':books})
	else:
		request.session.flush()
		return redirect('login')

def addlist(request):
	code = 500
	message = 'server error'
	if request.session.get("valid",False):
		json_data = json.loads(request.body)
		isbn = json_data['isbn']
		username = request.session.get("username",False)
		if username:
			r = requests.get('https://openlibrary.org/api/books?bibkeys=ISBN:'+str(isbn)+'&format=json&jscmd=details', params=request.GET)
			result_json = r.json()
			title = result_json['ISBN:'+str(isbn)]['details']['title']
			user = models.Reader.objects.filter(username=username)
			print(isbn)
			print(user[0])
			book = models.Book(isbn=isbn,title=title)
			book.save()
			user[0].books.add(book)
			code = 200
	else:
		request.session.flush()
	
	return JsonResponse({'code':code,'message':message})