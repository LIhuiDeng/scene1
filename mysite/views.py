from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context
from books.models import Author,Book
    
def index(request):
    Book_l=Book.objects.all()
    c=Context({"Book_list":Book_l})
    return render_to_response("index.html",c)
    
def submit(request):
    p0  = Author.objects.get(authorid=request.GET['authorid'])
    p1=Book(isbn=request.GET['isbn'],title=request.GET['bookname'],author=p0,
            publisher=request.GET['publisher'],publishDate=request.GET['publishdate'],price=request.GET['price'])
    p1.save()
    return HttpResponseRedirect('/home/')

def addbook(request):
    authorid=request.GET['authorid']
    c=Context({"authorid":authorid})
    return render_to_response("addbook.html",c)
    
def detail(request):
    b=Book.objects.get(isbn=request.GET['ID'])
    c=Context({"b":b})
    return render_to_response("detail.html",c)

def submit_author(request):
    p1=Author(authorid=request.GET['authorid'],name=request.GET['name'],age=request.GET['age'],
              country=request.GET['country'])
    p1.save()
    return HttpResponseRedirect('/author/')
    
      
def addauthor(request):
    return render_to_response("addauthor.html")
    
def author(request):
    Author_l=Author.objects.all()
    c=Context({"Author_list":Author_l})
    return render_to_response("Author.html",c)
    
def search(request):
    if 'searchString' in request.GET:
        auth_list=Author.objects.filter(name=request.GET['searchString'])
        book_list=[]
        for auth in auth_list:
            book_list.extend(Book.objects.filter(author=auth))
        c=Context({"book_list":book_list})
        return render_to_response("result.html",c)
        
def deleteauthor(request):
    auth=Author.objects.get(authorid=request.GET['authorid'])
    book_list=Book.objects.filter(author=auth)
    for book in book_list:
        book.delete()
    auth.delete()
    return HttpResponseRedirect('/author/')
        
def delete(request):
    bookid=request.GET['bookid']
    Book.objects.get(isbn=bookid).delete()
    return HttpResponseRedirect('/home/')
