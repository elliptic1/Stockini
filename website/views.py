# Create your views here.

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from forms import RegisterForm

def home(request):

    data = {}
    data['in_or_out'] = "LOGIN"

    return HttpResponse (
        render_to_string('htmlheader.html', data) +\
        render_to_string('navbar.html', data) +\
        render_to_string('header.html', data) +\
        render_to_string('home.html', data) +\
        render_to_string('sidebar.html', data) +\
        render_to_string('footer.html', data))


def register(request):

    data = {}

    if request.method == 'GET':
        form = RegisterForm()
        data['form'] = form
        return HttpResponse (
            render_to_string('htmlheader.html', data) +\
            render_to_string('navbar.html', data) +\
            render_to_string('header.html', data) +\
            render_to_string('register.html', data, RequestContext(request)) +\
            render_to_string('sidebar.html', data) +\
            render_to_string('footer.html', data))
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        data['email'] = form.email
        return HttpResponse (
            render_to_string('htmlheader.html', data) +\
            render_to_string('navbar.html', data) +\
            render_to_string('header.html', data) +\
            render_to_string('thanks.html', data) +\
            render_to_string('sidebar.html', data) +\
            render_to_string('footer.html', data))




def user(request, in_or_out):

    data = {}

    if in_or_out == 'in':
        data['in_or_out'] = "LOGOUT"
        data['welcome_message'] = "User!"
    else:
        data['in_or_out'] = "LOGIN"
        data['welcome_message'] = "Guest."

    return HttpResponse (
        render_to_string('htmlheader.html', data) +\
        render_to_string('navbar.html', data) +\
        render_to_string('header.html', data) +\
        render_to_string('home.html', data) +\
        render_to_string('sidebar.html', data) +\
        render_to_string('footer.html', data))




