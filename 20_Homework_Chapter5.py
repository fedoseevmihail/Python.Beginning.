# Генератор персонажей ролевой игры
# 30 пунктов копилки, которые можно распределить между 4 характеристиками: Сила, Здоровье, Мудрость и Ловкость
# Можно их распределять и возвращать обратно в копилку
print("\t\t\tДобро пожаловать в Генератор персонажей ролевой игры!")
print("\t\t\tРаспределяйте 30 пунктов между 4 навыками персонажа как пожелаете!")
input("\nНажмите Enter, чтобы начать.")
generator={"Сила":"0", "Здоровье":"0", "Мудрость":"0", "Ловкость":"0"}
points=int(30)
points_choice = ""
print("В Вашей копилке ", points, " очков для распределения на навыки.")
print("Вот список Ваших навыков. В начале игры у Вас 0 пунктов у каждого навыка.")
for i in generator:
    print(i)
choice=None
while choice != "0":
    input("\nНажмите Enter, чтобы вывести меню.")
    print(
    """
    0 - Выйти
    1 - Распределить пункты на навыки
    2 - Вернуть пункты в копилку
    3 - Посмотреть текущее распределение характеристик и пункты в копилке
    """
    )
    choice = input("Ваш выбор?")
    if choice == "0":
        input("Спасибо за игру! До встречи!")
    elif choice == "1":
        points_choice=int(input("Сколько пунктов Вы хотите распределить?"))
        if points_choice<=points:
            skill=input("Напишите, какой навык Вы хотите улучшить?")
            if skill in generator:
                points_skill=generator[skill]
                points_skill=int(points_skill)
                generator[skill]=points_choice+points_skill
                points-=points_choice
                print(skill, "=", generator[skill])
            else:
                print("Вы написали несуществующий навык: ", skill)
        else:
            print("В копилке меньше очков, чем Вы хотите прибавить к навыку.")
    elif choice == "2":
        points_choice=int(input("Сколько пунктов Вы хотите убрать?"))
        skill=input("Напишите, какой навык Вы хотите уменьшить?")
        if skill in generator:
            points_skill=generator[skill]
            points_skill=int(points_skill)
            if points_skill>=points_choice:
                generator[skill]=points_skill-points_choice
                points+=points_choice
                print(skill, "=", generator[skill])
            else:
                print("В выбранном навыке меньше очков, чем Вы хотите отнять.")
        else:
            print("Вы написали несуществующий навык: ", skill)
    elif choice == "3":
        print (generator)
        print("В Вашей копилке сейчас ", points, " очков для распределения на навыки.")
    else:
        print("Вы выбрали несуществующий пункт, повторите попытку!")
