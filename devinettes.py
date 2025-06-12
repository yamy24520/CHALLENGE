import random

# Liste de devinettes et leurs reponses
RIDDLES = [
    (
        "Qu'est-ce qui a des clés mais ne peut pas ouvrir de porte?",
        "un piano",
    ),
    (
        "Je commence la nuit et je finis le matin, que suis-je?",
        "la lettre n",
    ),
    (
        "Plus je sèche, plus je deviens humide. Qui suis-je?",
        "une serviette",
    ),
]


def ask_riddle(riddle, answer):
    print(riddle)
    user_answer = input("Votre réponse: ").strip().lower()
    if user_answer == answer:
        print("Bravo! Vous avez trouvé la bonne réponse!")
    else:
        print(f"Dommage! La bonne réponse était: {answer}.")



def main():
    print("Bienvenue dans le jeu des devinettes! Tapez 'quit' pour arrêter.")
    while True:
        riddle, answer = random.choice(RIDDLES)
        ask_riddle(riddle, answer)
        again = input("Voulez-vous une autre devinette? (o/n) ").strip().lower()
        if again not in ["o", "oui", "y", "yes"]:
            break


if __name__ == "__main__":
    main()
