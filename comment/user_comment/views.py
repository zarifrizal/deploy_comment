from django.shortcuts import render
from user_comment.models import Comment

# Create your views here.
def index(request):
    return render(request,'index.html')

def u_comment(request):
    if request.method == 'POST':
        name = request.POST['name']
        text= request.POST['text']
        data = Comment(name=name,text=text)
        data.save()

    data=Comment.objects.all()
    dict = {
        'allcomment': data
    }
    return render(request,'u_comment.html',dict)