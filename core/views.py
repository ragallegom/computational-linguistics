from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def index(request):

    print(request)
    
    example_string = "The friends of DeSoto love scarves."

    words_in_quote = word_tokenize(example_string)

    stop_words = set(stopwords.words("english"))

    filtered_list = []

    for word in words_in_quote:
        if word.casefold() not in stop_words:
                filtered_list.append(word)

    filtered_list = [
        word for word in words_in_quote if word.casefold() not in stop_words
    ]

    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_list]

    lemmatizer = WordNetLemmatizer()
    lemmatizer.lemmatize("scarves")

    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]

    response_data = {}
    response_data['result'] = lemmatized_words

    return JsonResponse(response_data)
