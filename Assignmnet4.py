#Hangman Game - Movie Edition
import random

MOVIES = ["Titanic","Avatar","Avatar The Way of Water","Inception","Interstellar","The Dark Knight","The Batman","Batman Begins","Joker","The Matrix","The Matrix Reloaded",
          "The Matrix Revolutions","Gladiator","Troy","300","The Lion King", "Frozen","Frozen II","Moana","Coco","Inside Out",
          "Finding Nemo","Finding Dory","Toy Story", "Toy Story 2","Toy Story 3","Toy Story 4","Cars","Up","Wall E","Ratatouille","Brave",
            "Encanto","Zootopia","Shrek","Shrek 2","Kung Fu Panda","How to Train Your Dragon","Minions","Despicable Me","Ice Age","Madagascar",
           "The Incredibles","Spider Man","Spider Man No Way Home","Iron Man","Captain America","Thor", "Doctor Strange", "Black Panther", "Avengers",
             "Avengers Endgame","Avengers Infinity War","Ant Man","Guardians of the Galaxy","Deadpool","Logan","Venom","Aquaman","Wonder Woman",
             "Man of Steel","Justice League","Fast Five","Fast and Furious 6","Furious 7","The Fate of the Furious","John Wick","John Wick Chapter 2",
                "John Wick Chapter 3", "Mission Impossible", "Top Gun", "Top Gun Maverick", "The Revenant", "The Wolf of Wall Street", "The Prestige",
             "Dunkirk","Tenet","Oppenheimer","Barbie","La La Land","Whiplash","The Shawshank Redemption","Forrest Gump","The Green Mile",
               "The Godfather","Pulp Fiction","Fight Club","Se7en","The Silence of the Lambs","The Social Network","The Pursuit of Happyness",
                 "Cast Away","Jurassic Park","Jurassic World","Jaws","King Kong","Godzilla","The Mummy","Pirates of the Caribbean","Harry Potter",
                 "The Lord of the Rings"]

movie = random.choice(MOVIES)
guessed_letters = set()
letter_strikes = 0
movie_strikes = 0

print("Movie Hangman!")
print("Type 1 letter to guess a letter (Max 5 wrong).")
print("Type the whole title to solve (Max 2 wrong).")

while letter_strikes < 5 and movie_strikes < 2:
    display = [
        char if (char.lower() in guessed_letters or char == " ") else "_"
        for char in movie
    ]
    print(f"\nMovie: {' '.join(display)}")
    print(
        f"Wrong letters: {letter_strikes}/5 | Wrong movie guesses: {movie_strikes}/2"
    )

    if "_" not in display:
        print(f" You won! The movie was: {movie}")
        break

    guess = input("Enter your guess: ").strip()

    if not guess:
        continue

    if len(guess) > 1:
        if guess.lower() == movie.lower():
            print(f" Correct! The movie was: {movie}")
            break
        else:
            print(" Wrong movie guess!")
            movie_strikes += 1
    else:
        guess = guess.lower()
        if guess in guessed_letters:
            print(" You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in movie.lower():
            print(" Correct letter!")
        else:
            print(" Wrong letter!")
            letter_strikes += 1
else:
    print(f"\n Game over! The movie was: {movie}")