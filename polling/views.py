from django.shortcuts import get_object_or_404, render
from django.db.models import F
from polling.models import Polls, Choices, VotePolls
from django.contrib import messages

# Create your views here.
def polling(request):
    polls = Polls.objects.all().order_by("-pub_date")
   
    return render(
        request,
        'pollinghome.html',
        {
            "polls": polls,
            "page_title": "Anime Polls | The Anime Radio",
            "page_description": "Vote in anime polls and compare community favorites on The Anime Radio.",
        },
    )

def polling_page(request):

    poll_id = request.GET.get("poll")
    poll = get_object_or_404(Polls, poll_id=poll_id)
    list_choice = Choices.objects.filter(Polls=poll).order_by("-votes")
    
    if request.method == "POST":
        vote_choice = request.POST.get("vote")

        if not vote_choice:
            messages.info(request, "Please choose an option before voting.")
            return render(request, "pollingpage.html", {"choices": list_choice})

        if not request.user.is_authenticated:
            messages.info(request, "Please log in to vote.")
            return render(request, "pollingpage.html", {"choices": list_choice})

        if VotePolls.objects.filter(user=request.user.id, poll=poll.poll_id).exists():
            messages.info(request, "You have already voted in this poll.")
            return render(request, "pollingpage.html", {"choices": list_choice})

        VotePolls.objects.create(user=request.user.id, poll=poll.poll_id)
        Choices.objects.filter(Polls=poll, choice=vote_choice).update(votes=F("votes") + 1)
        messages.info(request, f"You voted for {vote_choice}.")
        return render(request, "pollingpage.html", {"choices": list_choice})

    else:
        return render(request, "pollingpage.html", {"choices": list_choice})
        


