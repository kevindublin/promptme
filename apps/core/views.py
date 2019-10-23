from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Draft
import datetime
import random
import utils

currentprompt = 'What is the last smell you remember?'
imgurl = 'https://picsum.photos/1280/720/'
fulldict = utils.get_dict()


class WriteBox(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Draft
        fields = ['text', ]


def home(request):

    context = {
        '': '',
    }

    return render(request, 'pages/home.html', context)


@login_required
def dashboard(request):
    alldrafts = Draft.objects.order_by('-revised')
    userdrafts = alldrafts.filter(user=request.user)
    userdrafts = userdrafts

    context = {'user_drafts': userdrafts}

    return render(request, 'pages/dashboard.html', context)


@login_required
def delete_draft(request, draft_id):
    draft = Draft.objects.get(id=draft_id)
    draft.delete()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def update_draft(request, draft_id):
    text = request.POST['text']

    # Update draft
    draft = Draft.objects.get(id=draft_id)
    draft.text = text
    draft.save()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


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
    global currentprompt
    currentprompt = newprompt()
    print(currentprompt)
    context = {
        'random_image': newimage(),
        'new_prompt': currentprompt
    }

    return render(request, 'pages/prompt.html', context)


@login_required
def write(request):
    global currentprompt
    # Save Draft
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request,
        form = WriteBox(request.POST)

        if form.is_valid():
            # Use the form to save
            print('form is valid, sending to db...')
            newdraft = str(form)
            newdraft = newdraft.replace('<tr><th></th><td><textarea name="text" cols="40" rows="10" required id="id_text">', "")
            newdraft = newdraft.replace('</textarea></td></tr>', '')
            newdraft = newdraft.replace('&lt;p&gt;', '')
            newdraft = newdraft.replace('&lt;/p&gt;', '')
            print(newdraft)
            Draft = form.save(commit=False)
            Draft.user = request.user
            Draft.text = newdraft
            Draft.created = datetime.datetime.now()
            Draft.revised = datetime.datetime.now()
            Draft.prompt = currentprompt
            Draft.image = imgurl
            Draft.save()
            messages.success(request, 'Draft saved!')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            print('Form Data that is invalid')
            print(form)
    else:
        # if a GET we'll create a blank form
        form = WriteBox()

    context = {
        'form': form,
        'random_image': imgurl,
        'new_prompt': currentprompt,
        }

    return render(request, 'pages/write.html', context)


@login_required
def edit(request):
    context = {
    }

    return render(request, 'pages/edit.html', context)


def newprompt():

    currentprompt = "What attempts to be a tree in the wind?"

    return currentprompt


def newimage():
    global imgurl
    i = random.randint(1, 300000)
    randword = fulldict[i]
    print(i, fulldict[i])
    imgurl = 'https://picsum.photos/seed/' + randword + '/1280/720'
    return imgurl
