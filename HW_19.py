oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma Watson")
print("a with Emma Watson:", oscar_winners)

b = oscar_winners.copy()
b.discard("Meryl Streep")
print("b without Meryl Streep:", b)
b.clear()
print("b clear:", b)

print("c Titanic and The Dark Knight:", titanic_actors & dark_knight_actors)

print("d Iron Man and Avengers:", iron_man_actors.isdisjoint(avengers_actors))

print("e did all the actors win oscar?", actor_list <= oscar_winners)

print("f Avengers actors in actors_list:", actor_list >= avengers_actors)

print("g random exception:", movie_cast.pop())

movie_cast.remove("Matt Damon")
print("h without Matt Damon:", movie_cast)

print("i Titanic actors without oscar:", titanic_actors - oscar_winners)

print("j only one movie:", titanic_actors ^ dark_knight_actors)

new_names = {"Cate Blanchett", "Daniel Day-Lewis"}
print("k add names:", oscar_winners | new_names)

print("l Titanic + The Dark Knight:", titanic_actors.update(dark_knight_actors) or titanic_actors)
