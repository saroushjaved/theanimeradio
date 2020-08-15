from django.shortcuts import render
from pages.models import List2018, Votes
from django.db.models import F
from django.contrib import auth, messages


# Create your views here.
def home(request):
    return render(request, 'index.html')

#LIST PAGE 2018
def list2018(request):
    list1 = List2018.objects.all().order_by("-up_votes")

    if request.method == "POST":
        up_vote = request.POST.get('up_votes', None)
        down_vote = request.POST.get('down_votes', None)
        userid = request.user.id

        if up_vote != None:
            anime= List2018.objects.get(name=up_vote)
            animeid = anime.anime_id
        else:
            anime= List2018.objects.get(name=down_vote)
            animeid = anime.anime_id

        if Votes.objects.filter(user_id=userid, anime_id=animeid).exists():
            messages.info(request, "You Have Already Voted {}".format(up_vote))
            return render(request, 'list2018.html',{'list_2018':list1})
        else:
            Votes.objects.create(anime_id=animeid, user_id=userid)

            if request.user.is_authenticated:
                if up_vote is not None:
                    List2018.objects.filter(name=up_vote).update(up_votes=F("up_votes")+1)
                    messages.info(request, "YOU HAVE UP VOTED {}".format(up_vote))
                    return render(request, 'list2018.html',{'list_2018':list1})
                elif down_vote is not None:
                    messages.info(request, "YOU HAVE DOWN VOTED {}".format(down_vote))
                    List2018.objects.filter(name=down_vote).update(down_votes=F("down_votes")+1)
                    return render(request, 'list2018.html',{'list_2018':list1})

            else:
                messages.info(request, "Login to Vote or Register if you have no account")
                return render(request, 'list2018.html',{'list_2018':list1})
    else:    
        return render(request, 'list2018.html',{'list_2018':list1})

