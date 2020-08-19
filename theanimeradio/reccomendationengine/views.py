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

def genre_before_2010(request):
    #received the answer on genre 
    genre = request.GET['answer_before_genre']

    # 1- SLICE OF LIFE
    # 2- Dark and Fantasy
    # 3- ISIKAI
    # 4- SPORTS
    # 5- Comedy 
    # 6- Shonin 

    if  genre =="1": #will have further subcateogries
        return render(request, 'slice_of_life_before_2010.html')
    elif genre =="2": #No Sub categories
        pass
    elif genre =="3": # Wil have further subcateogies
        pass
    elif genre =="4": # Sports
        pass
    elif genre =="5": # Comedy
        pass
    elif genre =="6": # Will have further subcateogires
        pass
    else:
        pass
   

def genre_after_2010(request):
    #received the answer on genre 
    genre = request.GET['answer_after_genre']

    # 1- SLICE OF LIFE
    # 2- Dark and Fantasy
    # 3- ISIKAI
    # 4- SPORTS
    # 5- Comedy 
    # 6- Shonin

    if  genre == "1": #will have further subcateogries
         return render(request, 'slice_of_life_after_2010.html')
    elif genre == "2": #No Sub categories
        pass
    elif genre == "3": # Wil have further subcateogies
        pass
    elif genre == "4": # Sports
        pass
    elif genre == "5": # Comedy
        pass
    elif genre == "6": # Will have further subcateogires
        pass
    



def sliceoflife_before_2010(requests):
    pass
def sliceoflife_after_2010(requests):
    pass





