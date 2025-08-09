import random
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "la", "english": "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "that"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself"},
    {"spanish": "no", "english": "no"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "by / for / through"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his / her / their"},
    {"spanish": "para", "english": "for / in order to"},
    {"spanish": "como", "english": "like / as"},
    {"spanish": "estar", "english": "to be (temporary)"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "to him/her"},
    {"spanish": "lo", "english": "it / him"},
    {"spanish": "todo", "english": "everything / all"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "más", "english": "more"},
    {"spanish": "hacer", "english": "to do / to make"},
    {"spanish": "o", "english": "or"},
    {"spanish": "poder", "english": "to be able to / can"},
    {"spanish": "decir", "english": "to say / to tell"},
    {"spanish": "este", "english": "this"},
    {"spanish": "ir", "english": "to go"},
    {"spanish": "otro", "english": "other / another"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "la", "english": "her / it (fem.)"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "me", "english": "me / myself"},
    {"spanish": "ya", "english": "already / now"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "dar", "english": "to give"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he / him"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "vez", "english": "time / instance"},
    {"spanish": "mucho", "english": "much / a lot"},
    {"spanish": "saber", "english": "to know (facts)"},
    {"spanish": "qué", "english": "what / which"},
    {"spanish": "sobre", "english": "on / about"},
    {"spanish": "mi", "english": "my"},
    {"spanish": "alguno", "english": "some / any"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "también", "english": "also / too"},
    {"spanish": "hasta", "english": "until / even"},
    {"spanish": "año", "english": "year"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "querer", "english": "to want / to love"},
    {"spanish": "entre", "english": "between / among"},
    {"spanish": "así", "english": "so / thus"},
    {"spanish": "primero", "english": "first"},
    {"spanish": "desde", "english": "from / since"},
    {"spanish": "grande", "english": "big / large"},
    {"spanish": "eso", "english": "that (neuter)"},
    {"spanish": "ni", "english": "nor / neither"},
    {"spanish": "nos", "english": "us / ourselves"},
    {"spanish": "llegar", "english": "to arrive"},
    {"spanish": "pasar", "english": "to pass / to happen"},
    {"spanish": "tiempo", "english": "time / weather"},
    {"spanish": "ella", "english": "she / her"},
    {"spanish": "sí", "english": "yes / himself"},
    {"spanish": "día", "english": "day"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "bien", "english": "well / good"},
    {"spanish": "poco", "english": "little / few"},
    {"spanish": "deber", "english": "should / to owe"},
    {"spanish": "entonces", "english": "then"},
    {"spanish": "poner", "english": "to put"},
    {"spanish": "cosa", "english": "thing"},
    {"spanish": "tanto", "english": "so much / so many"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "parecer", "english": "to seem / to appear"},
    {"spanish": "nuestro", "english": "our"},
    {"spanish": "tan", "english": "so / such"},
    {"spanish": "donde", "english": "where"},
    {"spanish": "ahora", "english": "now"},
    {"spanish": "parte", "english": "part"},
    {"spanish": "después", "english": "after / later"},
    {"spanish": "vida", "english": "life"},
    {"spanish": "quedar", "english": "to stay / to remain"},
    {"spanish": "siempre", "english": "always"},
    {"spanish": "creer", "english": "to believe"},
    {"spanish": "hablar", "english": "to speak"},
    {"spanish": "llevar", "english": "to carry / to wear"},
    {"spanish": "dejar", "english": "to leave / to let"},
    {"spanish": "nada", "english": "nothing"},
    {"spanish": "cada", "english": "each / every"},
    {"spanish": "seguir", "english": "to follow / to continue"},
    {"spanish": "menos", "english": "less / fewer"},
    {"spanish": "nuevo", "english": "new"},
    {"spanish": "encontrar", "english": "to find"},
    {"spanish": "algo", "english": "something"},
    {"spanish": "solo", "english": "only / alone"},
    {"spanish": "venir", "english": "to come"},
    {"spanish": "pensar", "english": "to think"},
    {"spanish": "salir", "english": "to leave / to go out"},
    {"spanish": "volver", "english": "to return"},
    {"spanish": "tomar", "english": "to take / to drink"},
    {"spanish": "conocer", "english": "to know (people/places)"}
]

def quiz_user(words):
    random.shuffle(words)
    score=0
    for word in words:
        print(f"what is the English translation of'{word['spanish']} '?")
        user_answer=input("Your answer=").strip().lower()
        correct_answer=word['english'].lower()

        if user_answer==correct_answer:
            print("Correct Answer !\n")
            score=score+10
        else:
            print("Incorrect Answer!!!!! ,Correct answer is =", correct_answer)
    print("your quiz is complete , your score is =",score)
def main():
    print("Welcome to the language learning flashcards app ")
    print("Press Enter to start the quiz")
    quiz_user(words)

if __name__=="__main__":
    main()

