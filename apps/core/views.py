from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
        'random_image': 'https://picsum.photos/1280/720/',
        'new_prompt': 'What is the last smell you remember?'
    }

    return render(request, 'pages/prompt.html', context)


@login_required
def write(request):
    context = {
        'random_image': 'https://picsum.photos/1280/720/',
        'new_prompt': 'What is the last smell you remember?',
    }

    return render(request, 'pages/write.html', context)


@login_required
def edit(request):
    context = {
    }

    return render(request, 'pages/edit.html', context)
