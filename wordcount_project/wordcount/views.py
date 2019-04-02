from operator import itemgetter
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hi_there': 'This is Brian'})


def eggs(request):
    return HttpResponse('Eggs are tasty when scrambled')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}
    
    for word in wordlist:
        if word in word_dict:
            # increase count if word is found in dictionary
            word_dict[word] += 1
        else:
            # add initial count of one to the dictionary
            word_dict[word] = 1
    
    sorted_words = sorted(word_dict.items(), reverse=True, key=itemgetter(1))
    
    return render(request,\
            'count.html',\
            {'fulltext': fulltext, 
            'count': len(wordlist), 
            'sorted_words': sorted_words
            }\
        )
