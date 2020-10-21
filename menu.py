dairy_section = ['milk', 'cheese', 'eggs', 'jogurt']

print (dairy_section[0], dairy_section[3])

milk_expiration = ('june', '16th', '2019')

print("Milk expires on %s %s %s"  % milk_expiration)

milk_carton = {
	'expiration_date': milk_expiration,
	'fl_oz': 1./2,
	'cost': 1,
	'brand_name': 'cowmilk',
}

print (milk_carton.get('expiration_date'), milk_carton.get('fl_oz'),
milk_carton.get('cost'), milk_carton.get('brand_name') )

cartons = input ('How many carton of milk you would like to buy?: ')

price = float(milk_carton.get('cost') * cartons)

print ('Its gonna cost you',  price, '$')