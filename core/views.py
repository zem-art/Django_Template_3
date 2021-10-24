from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {
        "": "",
    }
    return render(request, 'index.html', ctx)


def dashboard(request):
    ctx = {
        "title": "Dashboard",
        "sub_title": "Dashboard"
    }
    return render(request, "home/index.html", ctx)


def user(request):
    ctx = {
        "title": "User",
        "sub_title": "User profile"
    }
    return render(request, "layout/user.html", ctx)


def table(request):
    ctx = {
        "title": "Table",
        "sub_title": "Table"
    }
    return render(request, "layout/tables.html", ctx)


def typo(request):
    ctx = {
        "title": "Typography",
        "sub_title": "Typography"
    }
    return render(request, "layout/typography.html", ctx)


def icon(request):
    ctx = {
        "title": "Icon",
        "sub_title": "Icons"
    }
    return render(request, "layout/icons.html", ctx)


def maps(request):
    ctx = {
        "title": "Maps",
        "sub_title": "Maps"
    }
    return render(request, "layout/map.html", ctx)


def notif(request):
    ctx = {
        "title": "Notif",
        "sub_title": "Notifications"
    }
    return render(request, "layout/notifications.html", ctx)
