seconds = input("Введите количество секунд")
seconds2 = int(seconds) % 60
minutes = int(seconds) // 60
hours = minutes // 60
print(
    f"В указанном количестве секунд {seconds}:\nЧасов: {hours}\nМинут: {minutes}\nСекунд: {seconds2}"
)

# Задание 2

cels = int(input("Введите температуру в градусах Цельсия"))
celv = cels + 273.15
fareng = (cels * 9 / 5) + 32
reom = cels * 4 / 5
print(
    f"Если температура в градусах Цельсия равна {cels}°C, то:\nКельвин: {celv} K\nФаренгейт: {fareng}°F\nРеомюр: {reom}°Ré"
)
