from django.shortcuts import get_object_or_404,render
from django.template import loader

from polls.Models.models import User


def index(request):
    latest_question_list = User.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, user):
    user = get_object_or_404(User, pk=user)
    return render(request, 'polls/detail.html', {'user': user})

#def detail(request, forname, surname, email):
#    return HttpResponse("User %s." %user)
