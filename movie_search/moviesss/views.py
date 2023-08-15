from django.shortcuts import render
from .models import Movie

def movie_search(request):
    if request.method == 'GET':
        year_filter = request.GET.get('year_filter', '')
        genre_filter = request.GET.get('genre_filter', '')
        title_filter = request.GET.get('title_filter', '')

        movies = Movie.objects.all().order_by('-rating')

        if year_filter:
            movies = movies.filter(year=year_filter)

        if genre_filter:
            movies = movies.filter(genre__icontains=genre_filter)

        if title_filter:
            movies = movies.filter(title__icontains=title_filter)

        years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
        all_genres = Movie.objects.values_list('genre', flat=True)
        unique_genres = set(g for genre_list in all_genres for g in genre_list.split(', '))
        genres = sorted(unique_genres) # Sort genres alphabetically
        context = {'movies': movies, 'years': years, 'genres': genres, 'year_filter': year_filter, 'genre_filter': genre_filter, 'title_filter': title_filter}
        return render(request, 'movie_search.html', context)
