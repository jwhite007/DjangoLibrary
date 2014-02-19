from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from users.forms import UsersForm
from users.models import users
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    entries = users.objects.all().order_by('last_name')[:]
    return render_to_response('users/index.html', {'users': entries})


def DeleteUser(request, pk):
    try:
        cardholder = get_object_or_404(users, pk=pk)
    except:
        return index(request)

    users.delete(cardholder)
    return render(request, 'users/delete_user.html', {'cardholder': cardholder})


def SubmitView(request):
    if request.method == 'GET':
        form = UsersForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = UsersForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            eddress = form.cleaned_data['eddress']
            # timestamp = form.cleaned_data['timestamp']
            post = users.objects.create(first_name=first_name, last_name=last_name, eddress=eddress)
            return HttpResponseRedirect(reverse('users:index'))
    return render(request, 'users/submit.html', {
        'form': form,
    })
