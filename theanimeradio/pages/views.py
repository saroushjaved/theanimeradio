from django.shortcuts import render
from pages.models import List2018
from django.db.models import F
from django.contrib import auth, messages


# Create your views here.
def home(request):
    return render(request, 'index.html')

def list2018(request):
    list1 = List2018.objects.all().order_by("-up_votes")

    if request.method == "POST":
        
        up_vote = request.POST.get('up_votes', None)
        print(up_vote)
        down_vote = request.POST.get('down_votes', None)
        print(down_vote)

        if request.user.is_authenticated:
            if up_vote is not None:
                List2018.objects.filter(name=up_vote).update(up_votes=F("up_votes")+1)
                messages.info(request, "YOU HAVE UP VOTED {}".format(up_vote))
                return render(request, 'list2018.html',{'list_2018':list1})
            elif down_vote is not None:
                messages.info(request, "YOU HAVE UP VOTED {}".format(up_vote))
                List2018.objects.filter(name=down_vote).update(down_votes=F("down_votes")+1)
                return render(request, 'list2018.html',{'list_2018':list1})
            else:
                pass
        else:
            messages.info(request, "Login to Vote")

    else:    
        return render(request, 'list2018.html',{'list_2018':list1})
