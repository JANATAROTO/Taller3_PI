import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Show the stored embedding of a randomly selected movie"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())
        if not movies:
            self.stderr.write("No movies found in the database.")
            return

        movie = random.choice(movies)
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)

        self.stdout.write(f"\U0001F3AC Película seleccionada: {movie.title}")
        self.stdout.write(f"\U0001F4CF Tamaño del embedding: {embedding_vector.shape[0]}")
        self.stdout.write(f"\U0001F522 Primeros 10 valores: {embedding_vector[:10]}")
