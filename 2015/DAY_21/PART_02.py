import sys, itertools, re
from queue import PriorityQueue

PLAYER_HP = 100
BOSS_HP = 109
BOSS_DAMAGE = 8
BOSS_ARMOR = 2

items = {
	"rings" : [],
	"weapons" : [],
	"armor" : []
}

q = PriorityQueue()

class Character:
	def __init__(self, name, hp, damage, armor):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.armor = armor

	def takeDamage(self, damage):
		if damage <= self.armor:
			self.hp -= 1
		else:
			self.hp -= (damage - self.armor)

class Item:
	def __init__(self, args):
		self.cost = int(args[1])
		self.damage = int(args[2])
		self.armor = int(args[3])

def loadItems():
	for key in items:
		file = open(key + ".txt",'r')

		for line in file:
			args = re.split('[ \t]{2,}',line.strip())
			items[key].append(Item(args))

		file.close()

	items["armor"].append(Item(["No Armor", "0","0","0"]))

def loadQueue():
	for weapon in items["weapons"]:
		q.put((-weapon.cost,weapon.damage,0))

		for armor in items["armor"]:
			myCost = armor.cost + weapon.cost
			myDamage = weapon.damage
			myArmor = armor.armor

			q.put((-myCost,myDamage,myArmor))

			for ring in items["rings"]:
				myCost = armor.cost + weapon.cost + ring.cost
				myDamage = weapon.damage + ring.damage
				myArmor = armor.armor + ring.armor
				q.put((-myCost,myDamage,myArmor))

			for rings in itertools.combinations(items["rings"], 2):
				myCost = armor.cost + weapon.cost + rings[0].cost + rings[1].cost
				myDamage = weapon.damage + rings[0].damage + rings[1].damage
				myArmor = armor.armor + rings[0].armor + rings[1].armor
				q.put((-myCost,myDamage,myArmor))

def battle(damage, armor):
	player = Character("Player", PLAYER_HP, damage, armor)
	boss  = Character("Boss", BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR)

	while True:
		boss.takeDamage(player.damage)

		if (boss.hp <= 0):
			return True

		player.takeDamage(boss.damage)

		if (player.hp <= 0):
			return False

loadItems()
loadQueue()
losses = []
print(q.qsize())
while not q.empty():
	stats = q.get()
	if not battle(stats[1], stats[2]):
		print(abs(stats[0]))
		break