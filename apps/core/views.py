from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import WriteBox, FeedbackBox
from .models import Draft, Feedback
import datetime
import random
import utils

currentprompt = 'What is the last smell you remember?'
imgurl = 'https://picsum.photos/1280/720/'
fulldict = utils.get_dict()
allprompts = utils.get_prompts()
feedback_questions = utils.get_questions()
q = 0


def home(request):

    context = {
        '': '',
    }

    return render(request, 'pages/home.html', context)


@login_required
def dashboard(request):
    # Get user drafts on dashboard #
    alldrafts = Draft.objects.order_by('-revised')
    userdrafts = alldrafts.filter(user=request.user)
    # Get user feedback #
    draftswithfeedback = userdrafts.filter(received_feedback=True)
    allfeedback = Feedback.objects.order_by('-added')
    userfeedback = allfeedback.filter(draft__user=request.user)
    # Make Feedback match the draft #

    '''
    try list comprehension syntax?


    draftfeedback.setdefault(feedback, [])
    for draft in draftswithfeedback:
        for feedback in userfeedback:
            if draft.id == feedback.draft__id:
                draftfeedback['feedback'].append = feedback

    print(draftfeedback)
    '''

    context = {'user_drafts': userdrafts, 'user_feedback': userfeedback}

    return render(request, 'pages/dashboard.html', context)


@login_required
def delete_draft(request, draft_id):
    draft = Draft.objects.get(id=draft_id)
    draft.delete()
    messages.warning(request, 'Draft deleted')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def send_to_queue(request, draft_id):
    draft = Draft.objects.get(id=draft_id)
    draft.in_queue = True
    draft.save()
    messages.success(request, 'Draft added to queue')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_queue(request, draft_id):
    draft = Draft.objects.get(id=draft_id)
    draft.in_queue = False
    draft.save()
    messages.warning(request, 'Draft removed from queue')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def update_draft(request, draft_id):
    text = request.POST['text']

    # Update draft
    draft = Draft.objects.get(id=draft_id)
    draft.text = text
    draft.save()
    messages.success(request, 'Draft upated')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


def form(request):
    context = {
    }

    return render(request, 'pages/form.html', context)


@login_required
def feedbackq(request):
    global feedback_questions
    alldrafts = Draft.objects.order_by('revised')
    queueddrafts = alldrafts.filter(in_queue=True)
    queueddrafts = alldrafts.exclude(user=request.user)

    if request.method == 'POST':
        form = request.POST
        two = request.POST
        print(request.POST)

        if form == two:
            # Use the form to save
            newfeedback = Feedback.objects.create(
                draft=queueddrafts[q],
                reader=request.user,
                summary=request.POST['q0'],
                progression=request.POST['q1'],
                aural_quality=request.POST['q2'],
                pov_clear=request.POST['q3'],
                style_distinct=request.POST['q4'],
                metaphors=request.POST['q5'],
                setting_specfic=request.POST['q6'],
                noun_specific=request.POST['q7'],
                verb_specific=request.POST['q8'],
                adjective_specific=request.POST['q9'],
                worldview=request.POST['q10'],
                emi=request.POST['emotional_impact'],
                favorite_lines=[request.POST['fave_line1'], request.POST['fave_line2'], request.POST['fave_line3']],
                comments=request.POST['comments']
                )
            newfeedback.save()
            # activate feedback on draft #
            turn_on_id = queueddrafts[q].id
            activate = Draft.objects.get(id=turn_on_id)
            activate.received_feedback = True
            activate.save()

            messages.success(request, 'Feedback saved!')
            print('form is valid, sending to db...')
    else:
        form = FeedbackBox()

    context = {
        'form': form,
        'queued_draft': queueddrafts[q],
        'feedback_questions': feedback_questions
    }

    return render(request, 'pages/feedbackq.html', context)


def next_in_q(request, queueddrafts):
    if q < len(queueddrafts)-1:
        q = q + 1
    else:
        q = 0

    return redirect(request.META.get('HTTP_REFERER', '/'))


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
            try:
                Draft = form.save(commit=False)
                Draft.user = request.user
                Draft.text = newdraft
                Draft.created = datetime.datetime.now()
                Draft.revised = datetime.datetime.now()
                Draft.prompt = currentprompt
                Draft.image = imgurl
                Draft.full_clean()
                Draft.save()
                messages.success(request, 'Draft saved!')
                return redirect(request.META.get('dashboard', '/dashboard/'))
            except ValidationError as error:
                messages.warning(request, error.messages_dict)
        else:
            print('Form Data is invalid')
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
    global currentprompt
    i = random.randint(0, len(allprompts)-1)
    currentprompt = allprompts[i]
    print(i, allprompts[i])
    return currentprompt


def newimage():
    global imgurl
    i = random.randint(0, len(fulldict)-1)
    randword = fulldict[i]
    print(i, fulldict[i])
    imgurl = 'https://picsum.photos/seed/' + randword + '/1280/720'
    return imgurl
