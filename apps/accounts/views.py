from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


from apps.accounts.forms import UserEditForm, SignupForm, SubmitPrompt
from apps.accounts.models import User, UserPrompt

import datetime


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('home')


@login_required
def view_all_users(request):
    all_users = User.objects.all()
    context = {
        'users': all_users,
    }
    return render(request, 'accounts/view_all_users.html', context)


@login_required
def view_profile(request, username):
    currentuser = User.objects.get(username=username)
    alluserprompts = UserPrompt.objects.order_by('-upvotes')
    currentuserprompts = alluserprompts.filter(user=currentuser)


    if request.user == currentuser:
        is_viewing_self = True
    else:
        is_viewing_self = False
        currentuserprompts = currentuserprompts.filter(public=True)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request,
        form = SubmitPrompt(request.POST)

        if form.is_valid():

            newuserprompt = form.cleaned_data
            text = newuserprompt['text']
            text = text.capitalize()

            if not text.endswith('?'):
                text += '?'

            try:
                newuserprompt = UserPrompt.objects.create(
                    user=request.user,
                    text=text,
                    created=datetime.datetime.now(),
                    revised=datetime.datetime.now(),
                    public=request.POST['public'],
                    upvotes=0
                )
                newuserprompt.save()
                messages.success(request, 'New prompt saved!')
                return redirect(request.META.get('HTTP_REFERER', '/'))

            except ValidationError as e:
                print('getting validation error:', e)
                messages.warning(request, e.message_dict)
        else:
            print('Form Data is invalid')

    else:
        form = SubmitPrompt()


    context = {
        'currentuser': currentuser,
        'is_viewing_self': is_viewing_self,
        'form': form,
        'currentuserprompts': currentuserprompts,
    }
    return render(request, 'accounts/profile_page.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserEditForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required
def membership(request):
    context = {
    }

    return render(request, 'accounts/membership.html', context)


@login_required
def delete_prompt(request, prompt_id):
    prompt = UserPrompt.objects.get(id=prompt_id)
    prompt.delete()
    messages.warning(request, 'Prompt deleted')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def public_toggle(request, prompt_id):
    prompt = UserPrompt.objects.get(id=prompt_id)

    if prompt.public == False:
        prompt.public = True
        messages.success(request, 'Prompt now public.')
    else:
        prompt.public = False
        messages.success(request, 'Prompt now private.')

    prompt.save()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def update_prompt(request, prompt_id):
    text = request.POST['text']


    # Update draft
    prompt = UserPrompt.objects.get(id=prompt_id)
    prompt.text = text
    prompt.save()
    messages.success(request, 'Prompt upated')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def upvote_prompt(request, prompt_id):
    prompt = UserPrompt.objects.get(id=prompt_id)

    prompt.upvotes = prompt.upvotes + 1

    prompt.save()
    messages.success(request, 'Vote saved')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/dashboard'))


@login_required
def downvote_prompt(request, prompt_id):
    prompt = UserPrompt.objects.get(id=prompt_id)

    prompt.upvotes = prompt.upvotes - 1

    prompt.save()
    messages.success(request, 'Vote saved')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/dashboard'))
