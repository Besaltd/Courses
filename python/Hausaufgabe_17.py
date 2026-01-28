# 1. Проверка на подмножество

set1 = {1, 2, 3, 4}
set2 = {2, 5}

is_subset = True
for elem in set2:
    if elem not in set1:
        is_subset = False
        break

print(set1 >= set2)
print(is_subset)
# 2. Зеркальное подмножество

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

set1_super = set2.issubset(set1)
set2_super = set1.issubset(set2)

is_subset = set1_super or set2_super

print("Подмножество найдено: ", is_subset)

if is_subset:
    if set1_super:
        difference = set1 - set2
    else:
        difference = set2 - set1
    print(f"Разница", difference)

print("Подмножество найдено: ", is_subset)
