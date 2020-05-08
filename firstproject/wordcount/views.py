from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['text']
    words = text.split()
    dictionary = {}

    for word in words:
        if word in dictionary:
            #increase
            dictionary[word] += 1
        else:
            # add to dictionary
            dictionary[word] = 1

    return render(request, 'result.html', {'text': text, 'total': len(words), 'dictionary' : dictionary.items()})