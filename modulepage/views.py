from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def build_plain_msg(msg=''):
    init_msg = 'Message '
    end_msg = ' end'
    return init_msg + msg + end_msg


def myapp_blog(request):
    msg = build_plain_msg('custom message')
    return HttpResponse(msg, content_type='text/plain')
