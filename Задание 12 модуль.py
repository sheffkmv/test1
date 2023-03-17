
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
values = per_cent.values()
deposit = []
for values in per_cent:
    money = int(input('Введите сумму вклада:'))
    deposit.append(per_cent[values] * money / 100)

print("Максимальная сумма, которую вы можете заработать -", int(max(deposit)))