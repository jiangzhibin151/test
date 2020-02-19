from django.shortcuts import render
from jzb import model
from django.http import HttpRequest

def userInfor(request):
    if request.method == "POST":
        u = request.POST.get("user", None)
        s = request.POST.get("score", None)
        info = model.Test.objects.filter(user=u)
        if not info:
            model.Test.objects.create(user=u, score=s)
        else:
            model.Test.objects.filter(user=u).update(score=int(s))
        info = model.Test.objects.all()

        return render(request, "user_index.html", {'info_list':info, 'u':u})
    return render(request, "user_index.html")

def select(request,u):
    aa = model.Test.objects.all().order_by('-score')
    tmp = model.Test.objects.get(user=u)
    return render(request, "index.html", {'aa':aa, 'tmp':tmp})