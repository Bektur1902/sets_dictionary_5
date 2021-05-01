menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

menu.update({'besh_barmak': 130})

print(menu)

menu.update({'besh_barmak': 135})

print(menu)

menu.pop('borsh')	
print(menu)