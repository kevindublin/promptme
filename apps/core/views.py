from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Draft
import datetime

currentprompt = 'What is the last smell you remember?'
imgurl = 'https://picsum.photos/1280/720/'


class WriteBox(forms.ModelForm):
    class Meta:
        model = Draft
        fields = ['text', ]


def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)


@login_required
def dashboard(request):
    context = {
    }

    return render(request, 'pages/dashboard.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


@login_required
def membership(request):
    context = {
    }

    return render(request, 'pages/membership.html', context)


def form(request):
    context = {
    }

    return render(request, 'pages/form.html', context)


@login_required
def feedbackq(request):
    context = {
    }

    return render(request, 'pages/feedbackq.html', context)


@login_required
def prompt(request):
    context = {
        'random_image': newimage(imgurl),
        'new_prompt': newprompt(currentprompt)
    }

    return render(request, 'pages/prompt.html', context)


@login_required
def write(request):
    # Save Draft
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request,
        form = WriteBox(request.POST)

        if form.is_valid():
            # Use the form to save
            newdraft = form.save()
            newdraft = Draft.objects.create(
                user=request.user,
                text=form,
                created=datetime.datetime.now(),
                revised=datetime.datetime.now(),
                prompt=currentprompt,
                )
            messages.success(request, 'Draft saved!')
            return newdraft
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            print('THIS IS WHAT THE FORM DATA IS')
            print(form)
    else:
        # if a GET we'll create a blank form
        form = WriteBox()

    context = {
        'random_image': newimage(imgurl),
        'new_prompt': newprompt(currentprompt),
        }

    return render(request, 'pages/write.html', context)


@login_required
def edit(request):
    context = {
    }

    return render(request, 'pages/edit.html', context)


def newprompt(currentprompt):

    currentprompt = "What attempts to be a tree in the wind?"

    return currentprompt


def newimage(imgurl):

    imgurl = 'https://picsum.photos/1280/720/'

    return imgurl
