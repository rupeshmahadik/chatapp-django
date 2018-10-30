from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import chatter
from .forms import chatterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello twice, chat once ")

def chat_display(request):
	c = chatter.objects.all()
	context= {
		"object_list" : c ,
	}
	return render(request, 'chatpage.html' , context)


@login_required
def create_chat(request):
	c = chatter.objects.all()

	form = chatterForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect('/chat/create/')

	context = {
		"form": form,
		"object_list" : c ,
	}
	return render(request,"chat_create.html", context)