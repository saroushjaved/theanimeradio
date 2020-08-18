from django.shortcuts import render

# Create your views here.
def reccomendation_home(request):
    return render(request, "reccomendation_home.html")

def reccomendation_engine(request):
    return render(request, "recommendation_engine.html")
 
def recc1(request):
    # receviing the response of instant or question
    val1= request.GET['answer1']
    if val1 == "1":
        #moved to next part of the quiz (aer you new to anime )
        return render(request, "recommendation_engine_questions.html")
    else: 
        #code to reccomend anime over here ( instant recommendation)
        return render(request, 'anime_recc_template.html')
        
def recc2(request):
    #receiving the answer to are you new to anime
    val1= request.GET['answer2']
    if val1 == "1":
        #moved to next part of the quiz ( mainstream or not)
        return render(request, "recommendation_engine_questions2.html")
    else: 
        #code to code learding to page when he says he is old
        return render(request, 'recommendation_engine_questions3.html')

def recc3(request):
    # receiving the answer of have you seen mainstream
    val1= request.GET['answer3']
    if val1 == "0":
        #moved to next part not seen then anime shown
        return render(request, "anime_recc_template.html")
    else: 
        #code if they have not seen leading to next page
        return render(request, 'recommendation_engine_questions3.html')

def recc4(request):
    # receiving the answer to before or after 2010
    val1= request.GET['answer4']
    if val1 == "1": #Before 2020
        return render(request, "recc_genre_before_2020.html")
    else: #After 2020 
        #genre will be showed after 2020
        return render(request, 'recc_genre_after_2020.html')

def genre_before_2010(requests):
    #received the answer on genre 
    genre = requests.GET['answer_before_genre']
    
    if  genre == 1: #will have further subcateogries
    
    elif genre ==2: #No Sub categories

    elif genre ==3: # Wil have further subcateogies
    
    elif genre ==4: # Sports
    
    elif genre ==5: # Comedy

    elif genre ==6: # Will have further subcateogires
    return render(requests, 'index.html')
   

def genre_after_2010(requests):
    #received the answer on genre 
    genre = requests.GET['answer_after_genre']
    
    if  genre == 1: #will have further subcateogries
    
    elif genre ==2: #No Sub categories

    elif genre ==3: # Wil have further subcateogies
    
    elif genre ==4: # Sports
    
    elif genre ==5: # Comedy

    elif genre ==6: # Will have further subcateogires
    return render(requests, 'index.html')
    