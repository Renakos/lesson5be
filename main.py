def create_player(nickname, /, class_name="Воин",*,level=1):
  return (nickname, class_name, level)
player1 = create_player("Aragorn")
player2 = create_player("Aragorn","Воин Получше",level=5)
print(player1)
print(player2)

print(player1[0])
# player1[2] = 10 # tuple не поддерживает изменение элементов
inventory = ["Меч","Щит","Зелье"]
inventory.append("Факел")
inventory[1] = "Улучшенный щит"
inventory.pop(0)
inventory.pop()
print(inventory)
