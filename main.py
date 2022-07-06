git ‐‐versionimport utils
from classes import Player

def main():
    #Приветствие игрока
    player = Player(input("Введите имя игрока: "))
    print(f"Привет, {player.name}!")

    #Начало игры
    game_word = utils.load_random_word()
    print(f"Составьте {len(game_word.subwords)} слов из слова {game_word.word.upper()}")
    print("Слова должны быть не короче 3 букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("Поехали, ваше первое слово?")

    #Игра
    correct_count = 0
#    for i in range(game_word.number_subwords()):
    while correct_count != game_word.number_subwords():
        new_word = input().lower()
        if new_word in ('stop', 'стоп', 'FLŰGGÅƏNK∂€ČHIŒβØL∫ÊN'):
            break
        elif len(new_word) < 3:
            print("слишком короткое слово")
            continue
        elif player.is_repeat(new_word):
            print("Неверно. Слово уже использовалось")
            continue
        elif game_word.is_correct(new_word):
            correct_count += 1
            player.append_word(new_word)
            print("верно")
        else:
            player.append_word(new_word)
            print("неверно")

    #Итог
    unguessed = set(game_word.subwords) - set(player.words)
    print(f"Игра завершена, вы угадали {correct_count} слов из {game_word.number_subwords()}!")
    if len(unguessed) != 0:
        print(f"Вы не угадали следующие слова: {', '.join(unguessed)}")


if __name__ == '__main__':
    main()
