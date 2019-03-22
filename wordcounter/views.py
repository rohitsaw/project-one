from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from userprofile.models import Myuser

# Create your views here.
def index(request):
    return render(request, "wordcounter/index.html")


def homepage(request):
    if not request.user.is_authenticated:
        context = {
        'login' : False,
        }
    else:
        try:
            myuser = Myuser.objects.get(user=request.user)
        except Myuser.DoesNotExist:
            myuser = request.user
        context = {
        'login' : True,
        'myuser': myuser
        #'user' : request.user
        }
    return render(request, "wordcounter/homepage.html", context)

def count(request):
    temp = request.GET.get("text", None)
    lcount = len(temp)
    temp = list(temp.strip().split())
    d = {}
    wcount = 0
    for item in temp:
        if item == "": continue
        wcount += 1
        d[item] = d.get(item,0) + 1
    temp = 0
    mfw = []
    for key, value in d.items():
        if value > temp:
            temp = value
            mfw = []
            mfw.append(key)
            if len(mfw) == 5:
                break
        elif value == temp:
            mfw.append(key)
            if len(mfw) == 5:
                break
    if len(mfw) == 5:
        mfw[4] += " etc.."

    #print(d)
    #mfw = max(d.items(), key=operator.itemgetter(1))[0]
    d = {"word_count": wcount, "letter_count":lcount, "most_frequent_word":mfw}
    return JsonResponse(d)
