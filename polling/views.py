from django.shortcuts import render
from django.db.models import F
from polling.models import Polls, Choices, VotePolls
from django.contrib import auth, messages

# Create your views here.
def polling(requests):
    polls = Polls.objects.all().order_by("-pub_date")
   
    return render(requests, 'pollinghome.html', {"polls":polls})

def polling_page(requests):

    poll_id = requests.GET["poll"]
    poll = Polls.objects.filter(poll_id=poll_id)
    list_choice = Choices.objects.filter(Polls=poll[0])
    
    if requests.method == "POST":
        vote_choice = requests.POST.get("vote", None)
        userid = requests.user.id

        if userid == None:
        	userid = 0
        else:
            pass 

        if requests.user.is_authenticated:
            if VotePolls.objects.filter(user=userid, poll=poll_id).exists():
                messages.info(requests, "You Have Already Voted for this POLL")
                return render(requests, "pollingpage.html", {"choices":list_choice})
            else:
                VotePolls.objects.create(user=userid, poll=poll_id)
                Choices.objects.filter(choice=vote_choice).update(votes=F("votes")+1)
                messages.info(requests, "YOU HAVE UP VOTED {}".format(vote_choice))
                return render(requests, "pollingpage.html", {"choices":list_choice})
        else:
            messages.info(requests, "Please Login to Vote")
            return render(requests, "pollingpage.html", {"choices":list_choice})

    else:
        return render(requests, "pollingpage.html", {"choices":list_choice})
        


