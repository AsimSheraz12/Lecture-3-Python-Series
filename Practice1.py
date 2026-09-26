movies = []
movieName1 = input("Enter first movie name : " )
movieName2 = input("Enter Second movie name : " )
movieName3 = input("Enter Third movie name : " )

movies.append(movieName1)
movies.append(movieName2)
movies.append(movieName3)

movies.sort()

print(f"Your Movies name which you enter {movies} {len(movies)} {movies}")