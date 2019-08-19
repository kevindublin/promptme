from django.shortcuts import render


def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def form(request):
    context = {
    }

    return render(request, 'pages/form.html', context)
