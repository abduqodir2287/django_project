from django.http import *
from django.template import loader
from .models import Member, Teachers
from random import randint


def members(request):
    return HttpResponse("Salom mening ismim Abduqodir\n"
                        "Tanishaganimdan xursandman")


def help_site(request):
    return HttpResponse("Bu saytda siz hech narsa qila olmaysiz chunki bu sayt hali tayyor emas!!!")


def goat(req):
    return HttpResponse("The Cristianooooo Siiuuuuuu  <<<   "
                        "Messi : Here he is again. Here he is again that's astonishing absolutely world class")


def best_players(request):
    return HttpResponse("1:Lionel Messi  2:Cristiano Ronaldo  3:Neymar Jr  4:Luis Suarez  5:Ronaldinho")


def first(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())


def second(req):
    template = loader.get_template("second.html")
    return HttpResponse(template.render())


def footballers(request):
    template = loader.get_template("footballers.html")
    return HttpResponse(template.render())


def welcome(request):
    template = loader.get_template("welcome.html")
    return HttpResponse(template.render())


def temp(request):
    my_data = Member.objects.all()
    template = loader.get_template("temp.html")
    context = {
        "mymembers": my_data
    }
    return HttpResponse(template.render(context, request))


def teachers(request):
    my_data = Teachers.objects.all()
    template = loader.get_template("teachers.html")
    context = {
        "mymembers": my_data
    }
    return HttpResponse(template.render(context, request))


def all_commands(request):
    template = loader.get_template("all.html")
    return HttpResponse(template.render())


def login(request):
    temlate = loader.get_template("login.html")
    return HttpResponse(temlate.render())


def testing(request):
    templates = loader.get_template("testing.html")
    ran = randint(1, 10)
    ran1 = randint(1, 10)
    javob = ran*ran1
    context = {
        "firstname": "Tom",
        "lastname": "Smith",
        "age": "16",
        "adres": "Tashkent",
        "kara": ran,
        "kara1": ran1,
        "javob": javob
    }

    return HttpResponse(templates.render(context, request))
