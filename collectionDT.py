'''List Datatype'''
watches = ['rolex','fastrack','fossil','titan','casio']
# print(watches)
watches.append('seiko')
# print(watches)

watches_copy = watches.copy()
# print(watches_copy)

watches_copy.clear()
# print(watches_copy)

shoes = ['nike','puma','adidas','woodland','puma']
# result = shoes.count('puma')
# print(shoes.count('puma'))
# print(shoes.count('bata'))

countries = ['switzerland','pakistan','india','usa','russia']
countries.remove('pakistan')
# print(countries)

my_cartoons = ['tom and jerry','doraemon','ninja hattori','spongebob','pink panther']

your_cartoons = ['ben10','shinchan','chhota bheem','naruto','oggy']
# my_cartoons.append(your_cartoons)
# print(my_cartoons)
# print(my_cartoons+your_cartoons)

my_cartoons.extend(your_cartoons)
# print(my_cartoons)

# my_cartoons.extend('mickey')
# print(my_cartoons)

my_cartoons.insert(0,'noddy')
# print(my_cartoons)

'''Tuple Datatype'''

car = ("mustang","BMW","chevrolete","BMW")
# print(car)
# print(car.index("chevrolete"))
# print(car.count("BMW"))

'''Set Datatype'''
supercars = {'lambo','bugatti','porsche','ferrari','bujji','mustang','ferrari'}
# print(supercars)

supercars.add('aston martin')
# print(supercars)

supercars_copy = supercars.copy()
# print(supercars_copy)

supercars_copy.clear()
# print(supercars_copy)   #set() -> default value of set

games1 = {'gta','far cry','god of war','assassins creed'}

games2 = {'fifa','cricket 2007','super mario','gta','free fire'}

result = games1.union(games2)
# print(result)

result = games1.intersection(games2)
# print(result)

result = games1.difference(games2)
# print(result)

result = games1.symmetric_difference(games2)
# print(result)

fruits = {'mango','strawberry','apple','pomegranates','orange','grapes'}

fruits.remove('grapes')
# print(fruits)
# fruits.remove(' dragon fruit')   #key error
# print(fruits)
fruits.discard('dragon fruit')
# print(fruits)

junkfoodchains = {'kfc','mcd','dominos','burger king','pizzahutt','taco bell'}
result = junkfoodchains.pop()
print(result)
print(junkfoodchains)
