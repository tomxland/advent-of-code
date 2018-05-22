import sys, copy
from queue import PriorityQueue

class State:
	def __init__(self):
		self.bossHP = 55
		self.bossDamage = 8
		self.mana = 500
		self.hp = 50
		self.armor = 0
		self.manaSpent = 0
		self.timer = 0

		self.shieldTimer = 0
		self.poisonTimer = 0
		self.rechargeTimer = 0

	def __lt__(self, other):
		return self.manaSpent < other.manaSpent

	def beforeTurn(self):		
		if self.shieldTimer > 0:
			self.armor = 7
			self.shieldTimer -= 1
		else:
			self.armor = 0

		if self.poisonTimer > 0:
			self.bossHP -= 3
			self.poisonTimer -= 1

		if self.rechargeTimer > 0:
			self.mana += 101
			self.rechargeTimer -= 1

	def castMissile(self):
		self.mana -= 53
		self.manaSpent += 53
		self.bossHP -= 4

	def castDrain(self):
		self.mana -= 73
		self.manaSpent += 73
		self.bossHP -= 2
		self.hp += 2

	def castShield(self):
		self.mana -= 113
		self.manaSpent += 113
		self.shieldTimer = 6
		self.armor = 7

	def castPoison(self):
		self.mana -= 173
		self.manaSpent += 173
		self.poisonTimer = 6

	def castRecharge(self):
		self.mana -= 229
		self.manaSpent += 229
		self.rechargeTimer = 5

start = State()
q = PriorityQueue()
q.put((0,start))

while not q.empty():
	state = q.get()[1]

	state.timer += 1

	if state.timer % 2 == 1: #Player's turn

		state.hp -= 1
		if state.hp <= 0:
			continue

		state.beforeTurn()

		if state.bossHP <= 0:
			print(state.manaSpent)
			break

		if state.mana >= 53:
			nxt = copy.deepcopy(state)
			nxt.castMissile()

			if nxt.bossHP <= 0:
				print(nxt.manaSpent)
				break
			else:
				q.put((nxt.manaSpent, nxt))

		if state.mana >= 73:
			nxt = copy.deepcopy(state)
			nxt.castDrain()

			if nxt.bossHP <= 0:
				print(nxt.manaSpent)
				break
			else:
				q.put((nxt.manaSpent, nxt))

		if state.mana >= 113:
			nxt = copy.deepcopy(state)
			nxt.castShield()
			q.put((nxt.manaSpent, nxt))

		if state.mana >= 173:
			nxt = copy.deepcopy(state)
			nxt.castPoison()
			q.put((nxt.manaSpent, nxt))

		if state.mana >= 229:
			nxt = copy.deepcopy(state)
			nxt.castRecharge()
			q.put((nxt.manaSpent, nxt))

	else:
		state.beforeTurn()

		if state.bossHP <= 0:
			print(state.manaSpent)
			break

		state.hp -= (state.bossDamage - state.armor)

		if state.hp > 0:
			q.put((state.manaSpent, state))