import re, sys

register = [0,0,0,0,0,0]

class Army:
	def __init__(self):
		self.units = 0
		self.hp = 0
		self.weaknesses = set()
		self.immunities = set()
		self.damage = 0
		self.damageType = None
		self.initiative = 0
		self.type = ""
		self.nextOpponent = None

	def __repr__(self):
		return "%i units with %i health points, %i %s damage, and %i initiative" % (self.units, self.hp, self.damage, self.damageType, self.initiative)

boost = 0

while True:
	print('Boosting by %i...' % boost)
	armies = {}
	count = {
		'Immune': 0,
		'Infection' : 0
	}

	isImmune = True

	id = ord('A');

	file = open(sys.argv[1], 'r')
	for line in file:
		line = line.strip()

		if (line == "Immune System:"):
			isImmune = True

		elif line == "Infection:" or line == "":
			isImmune = False

		else:
			args = re.split(" units each with | hit points |with an attack that does | damage at initiative ", line)

			a = Army()

			a.type = "Immune" if isImmune else "Infection"
			count[a.type] += 1
			a.units = int(args[0])
			a.hp = int(args[1])
			a.initiative = int(args[4])
			damage = args[3].split()
			a.damage = int(damage[0])

			if a.type == "Immune":
				a.damage += boost

			a.damageType = damage[1]

			specialties = re.sub('[()]', '', args[2])
			specialties = re.split('; ', specialties.strip())

			for sp in specialties:
				types = re.split(' to |, ', sp)

				type = ""

				for i, t in enumerate(types):
					if i == 0:
						type = t
					elif type == 'weak':
						a.weaknesses.add(t)
					elif type == 'immune':
						a.immunities.add(t)


			a.id = chr(id)
			armies[a.id] = a
			id += 1

	while count['Immune'] > 0 and count['Infection'] > 0:
		#print()
		# for id in armies:
		# 	a = armies[id]
		# 	print(a.type, a.id, a.units)
		#print()
		attackList = list(armies.values())
		attackList.sort(key=lambda x: (x.units*x.damage, x.initiative), reverse = True)
		targeted = set()

		for attacker in attackList:
			attacker = armies[attacker.id]

			if attacker.units > 0:
				maxDamage = 0
				maxOpps = []

				for id in armies:
					opp = armies[id]
					damage = 0

					if opp.type != attacker.type:
						if attacker.damageType not in opp.immunities:
							damage = attacker.damage * attacker.units

							if attacker.damageType in opp.weaknesses:
								damage *= 2

							maxOpps.append((damage, opp))

				#it chooses to target the defending group with the largest effective power;
				#if there is still a tie, it chooses the defending group with the highest initiative.
				maxOpps.sort(key=lambda x: (x[0], x[1].units*x[1].damage, x[1].initiative), reverse=True)

				# Defending groups can only be chosen as a target by one attacking group.
				attacker.opponent = None

				for i, opp in enumerate(maxOpps):
					if opp[1].id not in targeted:
						targeted.add(opp[1].id)
						attacker.opponent = opp[1].id
						attacker.opponentDamage = opp[0]
						break;
			else:
				attacker.opponent = None

			if attacker.opponent is not None:
				opp = armies[attacker.opponent]
				#print("%s %s would deal %s %s %i damage" % (attacker.type, attacker.id, opp.type, opp.id, attacker.opponentDamage))

		#Attack phase
		attackList = list(armies.values())
		attackList.sort(key=lambda x: x.initiative, reverse = True)
		#print()

		# Exit on stalement
		if len(targeted) == 0:
			break

		for attacker in attackList:
			if attacker.id in armies:
				attacker = armies[attacker.id]

				#If opponent is there
				if attacker.units > 0 and attacker.opponent in armies:
					opp = armies[attacker.opponent]
					attackDamage = attacker.units * attacker.damage

					if attacker.damageType in opp.weaknesses:
						attackDamage *= 2

					#print(attackDamage, opp.hp, attackDamage // (opp.hp))

					unitsKilled = min(attackDamage // (opp.hp), opp.units)
					opp.units -= unitsKilled

					#print("%s %s attacks defending group %s, killing %i units" % (attacker.type, attacker.id, opp.id, unitsKilled))

					if opp.units <= 0:
						count[opp.type] -= 1
						del armies[attacker.opponent]

	if count['Immune'] > 0 and count['Infection'] == 0:
		break
	else:
		boost += 1

#print()
total = 0
for id in armies:
	a = armies[id]
	#print("Group %s contains %i units" % (a.id, a.units))
	total += a.units

#print()
print("Immune system won with %i units" % total)