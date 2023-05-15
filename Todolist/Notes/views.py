from django.shortcuts import render,HttpResponseRedirect
from .models import Note
from .form import notes_form,finishNote
# Create your views here
def home(request):
    notes=Note.objects.all()
    if request.method=="POST":
        form=notes_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=notes_form()
    return render(request,"home.html",{"notes":notes,"notes_form":notes_form})
def deleteTodo(request,id):
    if request.method=="POST":
        index=Note.objects.get(pk=id)
        index.delete()
        return HttpResponseRedirect("/")
def noteCompleted(request,id):
    a=[]
    if request.method=="POST":
        note_f=Note.objects.get(id=id)
        note_f.completed=True
    return HttpResponseRedirect("/",{"note_f":note_f})