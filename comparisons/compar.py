def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie['year'], reverse=True)

def sort_by_title(movies):
    ignore_words = ['A', 'An', 'The']
    return sorted(movies, key=lambda movie: ' '.join(word for word in movie['title'].split() if word not in ignore_words))


movies = [
    {'title': 'The Avengers', 'year': 2012, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
    {'title': 'Anchorman: The Legend of Ron Burgundy', 'year': 2004, 'genres': ['Comedy']},
    {'title': 'Iron Man', 'year': 2008, 'genres': ['Action', 'Adventure', 'Sci-Fi']},
    {'title': 'The Dark Knight', 'year': 2008, 'genres': ['Action', 'Crime', 'Drama']},
    {'title': 'Avatar', 'year': 2009, 'genres': ['Action', 'Adventure', 'Fantasy', 'Sci-Fi']}
]


sorted_by_year = sort_by_year(movies)
print("Sorted by year:")
for movie in sorted_by_year:
    print(movie)

print()


sorted_by_title = sort_by_title(movies)
print("Sorted by title:")
for movie in sorted_by_title:
    print(movie)
