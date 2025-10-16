from django.shortcuts import render
from django.http import JsonResponse
from webscraper import get_irna_titles, get_isna_titles, get_mehr_titles, get_news_text
import Summary_and_Highlight.Highlight.Frequency_Based as frequency_based
import Summary_and_Highlight.Highlight.Luhn as luhn
import Summary_and_Highlight.Highlight.TextRank as textrank
from Summary_and_Highlight.Summary.summarizer import get_summaries


def home(request):
    return render(request, 'home.html')

news_data = {}
article = ''
def get_titles(request):
    global news_data
    if request.method == 'GET':
        agency = request.GET.get('agency', '')

        if agency == 'irna':
            news_data = get_irna_titles()

        elif agency == 'isna':
            news_data = get_isna_titles()

        elif agency == 'mehr':
            news_data = get_mehr_titles()

        # headings = ['عنوان اول', 'عنوان دوم با متن بلند، بلند که میگم ینی خیلیییی بلند، ببین، خیییییییییییییلییییییی بلننننننننندددددددددد', 'عنوان سوم با متنی کمی بلند تر', 'عنوان چهارم با متنی بسیااااار بسیاااااار بلنننننندددددد', 'عنوان پنجم معمولی']
        headings = list(news_data.keys())
        return JsonResponse({'headings': headings})
    else:
        print("Invalid request method")  # Debugging statement
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

def get_article_using_title(request):
    global article
    global news_data
    if request.method == 'GET':
        title = request.GET.get('title', '')
        url = news_data[title]
        article = get_news_text(url)
        return JsonResponse({'article': article})
    else:
        print("Invalid request method")  # Debugging statement
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

def get_article_using_url(request):
    global article
    if request.method == 'GET':
        url = request.GET.get('url', '')
        article = get_news_text(url)
        return JsonResponse({'article': article})
    else:
        print("Invalid request method")  # Debugging statement
        return JsonResponse({'error': 'Invalid request method'}, status=400)
        

def highlight_text(text, best_sentences):
    for sentence in best_sentences:
        if sentence in text:
            text = text.replace(sentence, f'<mark>{sentence}</mark>')
    return text

def get_extractive(request):
    global article
    if request.method == 'GET':
        freqbased_sents = frequency_based.get_best_sentences(article)
        luhn_sents = luhn.get_best_sentences(article, 4, 3)
        textrank_sents = textrank.get_best_sentences(article)
        freqbased_article = highlight_text(article, freqbased_sents)
        luhn_article = highlight_text(article, luhn_sents)
        textrank_article = highlight_text(article, textrank_sents)
        return JsonResponse({'frequency_based': freqbased_article, 'luhn':luhn_article, 'textrank':textrank_article})
    else:
        print("Invalid request method")  # Debugging statement
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_abstractive(request):
    global article
    if request.method == 'GET':
        summaries = get_summaries(article)
        return JsonResponse(summaries)
    else:
        print("Invalid request method")  # Debugging statement
        return JsonResponse({'error': 'Invalid request method'}, status=400)
