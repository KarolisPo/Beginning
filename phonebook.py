people = {
	
	'Kotryna': {
		'phone':'860209946',
		'addr':'Architektu g 200-39'
	},
	'Mama': {
		'phone':'+4746273291',
		'addr':'Klokkenbakken 10, 3520, Jevnaker'
	},
	'Rokas': {
		'phone':'867848287',
		'addr':'Perkunkiemio g 19-62'
	},
	'Justinas':{
		'phone':'860423254',
		'addr':'Perkunkiemio g'},
	'Edgaras':{
		'phone':'869941636',
		'addr':'Sveicaru km,'},
	'Jonas':{
		'phone':'867807954',
		'addr':'J.Biliuno g, 4'},
	'Janina':{
		'phone':'865678736',
		'addr':'Sveicaru km'},
	'Aurimas':{
		'phone':'867821287',
		'addr':'Vilniaus g 90-27, Vilnius'},
	'Jokubas':{
		'phone':'862884417',
		'addr':'A.Vienuolio g 11, Vilnius'},
	'Pecia':{
		'phone':'862059600',
		'addr':'Grikiskes'},
	'Aiste':{
		'phone':'862083329',
		'addr':'Austejos g 17, Vilnius'},
	'Augis':{
		'phone':'860488570',
		'addr':'Tuskulenu g 13, Vilnius'},
	'Darius': {
		'phone':'862884417',
		'addr':'A.Vienuolio g 11, Vilnius'},
	}

	

labels = {
	'phone':'phone number',
	'addr':'adress'
}



name = input('Name: ')

request = input("Phone number (p) or adress (a)?")

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'


if name in people: print (name,"'s", labels[key], "is", people[name][key])