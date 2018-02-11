import json
import urllib2

poster_path = "/static/cinema/posters"


def get_poster(movie):
    name = movie["name"]
    name = name.replace(" ", "+")
    url = "https://api.themoviedb.org/3/search/movie?api_key=b8709f9f1b37bdb033200f1084de9ec8&query=%s" % name
    print(url)
    jsondata = urllib2.urlopen(url).read()
    movie_data = json.loads(jsondata)
    print(movie_data["page"])
    if "page" in movie_data:
        url2 = "https://image.tmdb.org/t/p/w500/%s" % movie_data["results"][0][
            "poster_path"]
    else:
        url2 = "https://image.tmdb.org/t/p/w500/%s" % movie_data["poster_path"]
    poster = urllib2.urlopen(url2).read()
    with open("%s%s.jpg" % (poster_path, name), 'w') as f:
        f.write(poster)