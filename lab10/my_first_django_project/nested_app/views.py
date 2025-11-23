from django.http import HttpResponse


def nested_index(request):
    return HttpResponse("<h1>Nested app index</h1>")


def nested_user(request, username):
    return HttpResponse(f"<h1>Nested user page: {username}</h1>")


def nested_info(request):
    return HttpResponse("<h1>Some info from nested_app</h1>")
