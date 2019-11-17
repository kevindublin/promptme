from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import WriteBox, FeedbackBox
from .models import Draft, Feedback
import datetime
import random
import utils


fulldict = utils.get_dict()
blanklist = utils.get_blanklist()
allprompts = utils.get_prompts()
q = 0
queueddrafts = []
qcalls = 0


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
    allfeedback = Feedback.objects.order_by('-added')
    userfeedback = allfeedback.filter(draft__user=request.user)

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


def privacy(request):
    context = {
    }

    return render(request, 'pages/privacy.html', context)


@login_required
def feedbackq(request):
    global feedback_questions
    global queueddrafts
    # getting all drafts from db
    alldrafts = Draft.objects.order_by('revised')
    # making sure all drafts have been added to the queue
    queueddrafts = alldrafts.filter(in_queue=True)
    # making sure drafts are written by other user
    queueddrafts = queueddrafts.exclude(user=request.user)
    # making sure that the current user hasn't already given feedback
    queueddrafts = queueddrafts.exclude(allfeedback__reader=request.user)

    if len(queueddrafts) == 0 or q >= len(queueddrafts):
        messages.warning(request, 'Sorry, there are currently no more drafts in the queue.')
        return redirect(request.META.get('dashboard', '/dashboard/'))

    if request.method == 'POST':
        form = FeedbackBox(request.POST)

        if form.is_valid():

            newfeedback = form.cleaned_data
            # Use the form to save
            try:
                newfeedback = Feedback.objects.create(
                    draft=queueddrafts[q],
                    reader=request.user,
                    added=datetime.datetime.now(),
                    summary=request.POST['summary'],
                    progression=request.POST['progression'],
                    aural_quality=request.POST['aural_quality'],
                    pov_clear=request.POST['pov_clear'],
                    style_distinct=request.POST['style_distinct'],
                    metaphors=request.POST['metaphors'],
                    setting_specific=request.POST['setting_specific'],
                    noun_specific=request.POST['noun_specific'],
                    verb_specific=request.POST['verb_specific'],
                    adjective_specific=request.POST['adjective_specific'],
                    worldview=request.POST['worldview'],
                    emi=request.POST['emi'],
                    favorite_lines=request.POST['favorite_lines'],
                    comments=request.POST['comments']
                    )
                newfeedback.save()
                # activate feedback on draft #
                draft_id = queueddrafts[q].id
                draft = Draft.objects.get(id=draft_id)
                draft.feedback_amount = draft.feedback_amount + 1
                draft.save()
                check_feedback(draft_id)

                global qcalls
                qcalls = 0
                messages.success(request, 'Feedback saved!')
                return redirect(request.META.get('HTTP_REFERER', '/'))

            except ValidationError as e:
                print('getting validation error:', e)
                messages.warning(request, e.message_dict)
    else:
        form = FeedbackBox()

    context = {
        'form': form,
        'queued_draft': queueddrafts[q],
        'feedback_questions': feedback_questions
    }

    return render(request, 'pages/feedbackq.html', context)


def queue_next(request):
    global queueddrafts
    global q
    global qcalls

    if len(queueddrafts) <= 1:
        messages.warning(request, 'No more drafts in the gueue.')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    if qcalls < 3:
        qcalls = qcalls + 1
        if q < len(queueddrafts)-1:
            q = q + 1
        else:
            q = 0
        messages.success(request, 'Next in queue.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        messages.warning(request, 'No more skips available!')
        return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def delete_feedback(request, feedback_id, draft_id):

    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()

    draft = Draft.objects.get(id=draft_id)
    draft.feedback_amount = draft.feedback_amount - 1
    draft.save()
    check_feedback(draft_id)

    messages.warning(request, 'That feedback was deleted')
    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


def check_feedback(draft_id):

    draft = Draft.objects.get(id=draft_id)
    if draft.feedback_amount <= 0:
        draft.received_feedback = False
        draft.save()

    else:
        draft.received_feedback = True
        draft.save()


@login_required
def prompt(request):

    # Set as global variables as backup attempt
    global currentprompt
    global imgurl

    currentprompt = newprompt()
    imgurl = newimage()
    # Set the variables to the session
    request.session['currentprompt'] = currentprompt
    request.session['imgurl'] = imgurl
    print(currentprompt)
    context = {
        'random_image': imgurl,
        'new_prompt': currentprompt
    }

    return render(request, 'pages/prompt.html', context)


@login_required
def write(request):

    # Attempt to pull variables from previous view
    global currentprompt
    global imgurl
    # Pull the prompt and image from the session data as a backup
    currentprompt = request.session['currentprompt']
    imgurl = request.session['imgurl']
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
            newdraft = newdraft.replace('&lt;/p&gt;', '<br />')
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
                messages.warning(request, error.message_dict)
        else:
            print('Form Data is invalid')
    else:
        # blank form on GET
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

    for word in blanklist:
        if word == randword:
            return newimage()

    print(i, fulldict[i])
    imgurl = 'https://picsum.photos/seed/' + randword + '/1280/720'
    return imgurl
