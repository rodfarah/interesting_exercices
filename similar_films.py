class User:
    def __init__(self, name: str):
        self.name = name

    def watched(self, film: str) -> list:
        self.watched_films = []
        self.watched_films.append(film)


    def rate(self, film: str, score: int):
        self.one_star = []
        self.two_stars = []
        self.three_stars = []
        self.four_stars = []
        self.five_stars = []
        if score == 1:
            self.one_star.append(film)
        elif score == 2:
            self.two_stars.append(film)
        elif score == 3:
            self.three_stars.append(film)
        elif score == 4:
            self.four_stars.append(film)
        elif score == 5:
            self.five_stars.append(film)

class Film:
    def __init__(self, name: str):
        self.name = name

p001 = User('Rodrigo')
p002 = User('Sandra')
p003 = User('Bruna')

f001 = Film('Um gênio indomável')
f002 = Film('A vida é bela')
f003 = Film('Alabama Monroe')

p001.watched(f001.name)

p001.rate(f001.name, 3)
p003.rate(f002.name, 5)
p002.rate(f003.name, 1)

print(p001.watched)