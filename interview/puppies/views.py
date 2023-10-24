from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.


def main(request):
	return render(request,'main.html',{})

def more(request,isbn):
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
	return render(request,'more.html',{'title':title,'author':author,'publish_date':publish_date,'description':description})
