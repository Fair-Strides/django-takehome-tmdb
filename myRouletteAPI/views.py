from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os

previousTerm = ''
previousResults = []

@api_view(['GET'])
def search(request, title):
    global previousTerm
    global previousResults

    if(previousTerm == None):
        previousTerm = ''
        previousResults = []

    if(title == '__'):
        previousTerm = ''
        previousResults = []
        return Response({'results': []})
    elif(title == previousTerm or title == 'none'):
        return Response({'results': previousResults})
    
    previousTerm = title
    apiKey = os.environ.get('TMDB_API_KEY')
    url = f'https://api.themoviedb.org/3/search/movie?api_key={apiKey}&language=en-US&query={title}&page=1&include_adult=false'
    response = requests.get(url)
    status = response.status_code

    if status == 200:
        data = response.json()
        previousResults = data['results']
        return Response(data)
    else:
        return Response({'error': f'An error occurred while fetching data. Status code: {status} Error: {response.text} {response.reason}'})

@api_view(['GET'])
def details(request, movieId):
    if(movieId == -1):
        return Response({'data': {}})
    

    apiKey = os.environ.get('TMDB_API_KEY')
    url = f'https://api.themoviedb.org/3/movie/{movieId}?api_key={apiKey}&language=en-US'
    response = requests.get(url)
    status = response.status_code

    if status == 200:
        data = response.json()
        return Response(data)
    else:
        return Response({'error': 'An error occurred while fetching data.'})