from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import operator

# Create your views here.
def index(request):
    return render(request, "wordcounter/index.html")


def homepage(request):
    return render(request, "wordcounter/homepage.html")

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
