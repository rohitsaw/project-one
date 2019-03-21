from django.shortcuts import render
from .models import Notes
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    #print("in index")
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userprofile:index"))
    notes = Notes.objects.filter(user=request.user)
    context = {}
    context['notes'] = {}
    for note in notes:
        noteAsList = []
        noteAsList.append(note.notes)
        noteAsList.append(note.date)
        context['notes'][note.heading] = noteAsList
        #print(context['notes'])

    return render(request,"noteapp/index.html", context)

def storenote(request):
    if not (request.user.is_authenticated):
        return HttpResponseRedirect(reverse("userprofile:index"))
    if not request.method == "POST":
        return HttpResponseRedirect(reverse("noteapp:index"))
    heading = request.POST["heading"]
    notes = request.POST["note"]
    user = request.user
    try:
        notesexist = Notes.objects.get(heading=heading, user=request.user)
    except Notes.DoesNotExist:
        p = Notes(heading=heading, user=request.user, notes=notes)
        p.save()
        return HttpResponseRedirect(reverse("noteapp:index"))
    raise SuspiciousOperation("Invalid request; Same heading already exist.")

def remove(request):
    if not (request.user.is_authenticated):
        return HttpResponseRedirect(reverse("userprofile:index"))
    if not (request.method=="POST" and request.is_ajax()):
        return HttpResponseRedirect(reverse("noteapp:index"))
    # user = request.POST['user']
    heading = request.POST['heading']
    note = request.POST['note']
    Notes.objects.filter(user=request.user, heading=heading)[0].delete()

    return HttpResponse("success")
