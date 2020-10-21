import random




class country:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital

jav = country('JAV', 'Vasingtonas')
kanada = country('Kanada', 'Otava')
meksika = country('Meksika', 'Meksikas')
bahamai = country('Bahamai', 'Nasau')
kuba = country('Kuba', 'Havana')
grenlandija = country('Grenlandija', 'Nuukas')
havajai = country('Havajai', 'Honolulu')
bermuda = country('Bermuda', 'Hamiltonas')
gvatemala = country('Gvatemala', 'Gvatemala')
belizas = country('Belizas', 'Belmopanas')
honduras = country('Honduras', 'Tegusigalpa')
salvadoras = country('Salvadoras', 'San Salvadoras')
nikaragva = country('Nikaragva', 'Managva')
kosta_rika = country('Kosta Rika', 'San Chose')
panama = country('Panama', 'Panama')
jamaika = country('Jamaika', 'Kingstonas')
haitis = country('Haitis', 'Port Prensas')
dominikos_respublika = country('Dominykos respublika', 'Santo Domingas')
puerto_rikas = country('Puerto Rikas', 'San Chuanas')
venesuela = country('Venesuela', 'Karakasas')
kolumbija = country('Kolumbija', 'Bogota')
gajana = country('Gajana', 'Dzordztaunas')
surinamas = country('Surinamas', 'Paramaribas')
ekvadoras = country('Ekvadoras', 'Kitas')
peru = country('Peru', 'Lima')
bolivija = country('Bolivija', 'La Pasas')
brazilija = country('Brazilija', 'Brazilija')
paragvajus = country('Paragvajus', 'Asunsjonas')
urugvajus = country('Urugvajus', 'Montevidejas')
argentina = country('Argentina', 'Buenos Aires')
cile = country('Čilė', 'Santjagas')

islandija = country('Islandija', 'Reikjavikas')
norvegija = country('Norvegija', 'Oslas')
svedija = country('Švedija', 'Stokholmas')
suomija = country('Suomija', 'Helsinkis')
danija = country('Danija', 'Kopenhaga')
airija = country('Airija', 'Dublinas')
anglija = country('Anglija', 'Londonas')
belgija = country('Belgija', 'Briuselis')
liuksenburgas = country('Liuksenburgas', 'Liuksenburgas')
olandija = country('Olandija', 'Amsterdamas')
vokietija = country('Vokietija', 'Berlynas')
prancuzija = country('Prancūzija', 'Paryzius')
monakas = country('Monakas', 'Monakas')
sveicarija = country('Šveicarija', 'Bernas')
austrija = country('Austrija', 'Viena')
lichtensteinas = country('Lichtenšteinas', 'Vaduzas')
vengrija = country('Vengrija', 'Budapestas')
lenkija = country('Lenkija', 'Varsuva')
cekija= country('Čekija', 'Praha')
slovakija = country('Slovakija', 'Bratislava')
ispanija = country('Ispanija', 'Madridas')
andora = country('Andora', 'Andora')
portugalija = country('Portugalija', 'Lisabona')
italija = country('Italija', 'Roma')
san_marinas = country('San Marinas', 'San Marinas')
vatikanas = country('Vatikanas', 'Vatikanas')
slovenija = country('Slovėnija', 'Liubliana')
malta = country('Malta', 'Valeta')
kroatija = country('Kroatija', 'Zagrebas')
bosnija_hercogovina = country('Bosnija ir Hercogovina', 'Sarajevas')
makedonija = country('Makedonija', 'Skopje')
graikija = country('Graikija', 'Atenai')
bulgarija = country('Bulgarija', 'Sofija')
estija = country('Estija', 'Talinas')
latvija = country('Latvija', 'Ryga')
lietuva = country('Lietuva', 'Vilnius')
baltarusija = country('Baltarusija', 'Minskas')
moldova = country('Moldova', 'Kisiniovas')
rumunija = country('Rumunija', 'Bukarestas')
ukraina = country('Ukraina', 'Kijevas')

albanija = country('Albanija', 'Tirana')
rusija = country('Rusija', 'Maskva')
gruzija = country('Gruzija', 'Tbilisis')
armenija = country('Armėnija', 'Jerevanas')
azerbaidzanas = country('Azerbaidžianas', 'Baku')
turkija = country('Turkija', 'Ankara')
kipras = country('Kipras', 'Nikosija')
sirija = country('Sirija', 'Damaskas')
izraelis = country('Izraelis', 'Jeruzale')
libanas = country('Libanas', 'Beirutas')
jordanija = country('Jordanija', 'Amanas')
irakas = country('Irakas', 'Bagdadas')
iranas = country('Iranas', 'Teheranas')
saudo_arabija = country('Saudo Arabija', 'Rijadas')
kuveitas = country('Kuveitas', 'Kuveitas')
bahreinas = country('Bahreinas', 'Menama')
kataras = country('Kataras', 'Doha')
jae = country('JAE', 'Abu Dabis')
omanas = country('Omanas', 'Maskatas')
jemenas = country('Jemenas', 'Gana')
kazachstanas = country('Kazachstanas', 'Astana')
uzbekistanas = country('Uzbekistanas', 'Taskentas')
turkmenistanas = country('Turkmenistanas', 'Aschaladas')
tadzikistanas = country('Tadžikistanas', 'Dusanke')
kirgizija = country('Kirgizija', 'Biskekas')
afganistanas = country('Afganistanas', 'Kabulas')
pakistanas = country('Pakistanas', 'Islamabadas')
indija = country('Indija', 'Delis')
bangladesas = country('Bangladešas', 'Dhaka')
nepalas = country('Nepalas', 'Katmandu')
butanas = country('Būtanas', 'Thimphu')
sri_lanka = country('Šri Lanka', 'Kolombas')
maldyvai = country('Maldyvas', 'Male')
madagaskaras = country('Madagaskaras', 'Antananaryvas')
taivanas = country('Taivanas', 'Taipejus')
kinija = country('Kinija', 'Pekinas')
mongolija = country('Mongolija', 'Ulan Batoras')
siaures_koreja = country('Šiaurės Korėja', 'Pchenjanas')
pietu_koreja = country('Pietų Korėja', 'Seulas')
japonija = country('Japonija', 'Tokijas')
tailandas = country('Tailandas', 'Bankokas')
birma = country('Birma', 'Rangunas')
vietnamas = country('Vietnamas', 'Hanojus')
kambodza = country('Kambodža', 'Pnompenis')
laosas = country('Laosas', 'Vientianas')
brunejus = country('Brunėjus', 'Bandar Seri Begawanas')
singapuras = country('Singapūras', 'Singapuras')
malaizija = country('Malaizija', 'Kvala Lampūras')
indonezija = country('Indonezija', 'Dzakarta')
rytu_timoras = country('Rytų Timoras', 'Dilis')
filipinai = country('Filipinai', 'Manila')


marokas = country('Marokas', 'Rabatas')
alzyras = country('Alžyras', 'Alzyras')
tunisas = country('Tunisas', 'Tunisas')
libija = country('Libija', 'Tripolis')
egiptas = country('Egiptas', 'Kairas')
sudanas = country('Sudanas', 'Chartumas')
somalis = country('Somalis', 'Mogadisas')
etiopija = country('Etiopija', 'Adis Adela')
eritreja = country('Eritrėja', 'Asmara')
dzibutis = country('Džibutis', 'Dzibutis')
mauritanija = country('Mauritanija', 'Nuaksatas')
malis = country('Malis', 'Bamakas')
nigeris = country('Nigeris', 'Niamejus')
senegalas = country('Senegalas', 'Dakaras')
gambija = country('Gambija', 'Bandzulis')
bisau_gvineja = country('Bisau Gvinėja', 'Bisau')
gvineja = country('Gvinėja', 'Konakris')
siera_leone = country('Siera Leonė', 'Fritaunas')
liberija = country('Liberija', 'Monrovija')
togas = country('Togas', 'Lome')
dramblio_kk = country('Dramblio Kaulo Krantas', 'Jamasukras')
gana = country('Gana', 'Akra')
nigerija = country('Nigerija', 'Abudza')
burkina_fasas = country('Burkina Fasas', 'Uagadugu')
beninas = country('Beninas', 'Porto Novas')
zambija = country('Zambija', 'Lusaka')
kamerunas = country('Kamerūnas', 'Jaunde')
car = country('CAR', 'Bangis')
pusiaujo_gvineja = country('Pusiaujo Gvinėja', 'Malabas')
cadas = country('Čadas', 'Ndzamena')
gabonas = country('Gabonas', 'Librevilis')
kongas = country('Kongas', 'Brazavilis')
kongo_dr = country('Kongo Demokratinė Respublika', 'Kinšasa')
uganda = country('Uganda', 'Kampala')
ruanda = country('Ruanda', 'Kigalis')
burundis = country('Burundis', 'Buzumbura')
kenija = country('Kenija', 'Nairobis')
tanzanija = country('Tanzanija', 'Dodoma')
malavis = country('Malavis', 'Lilongve')
angola = country('Angola', 'Luanda')
botsvana = country('Botsvana', 'Gaboronas')
namibija = country('Namibija', 'Vindhukas')
zimbabve = country('Zimbabvė', 'Harare')
mozambikas = country('Mozambikas', 'Maputu')
par = country('PAR', 'Keiptaunas')
svazilandas = country('Svazilandas', 'Mbabve')
lesotas = country('Lesotas', 'Maseru')

australija = country('Australija', 'Kanbera')
n_zelandija = country('Naujoji Zelandija', 'Velingtonas')

world_country = [jav, kanada, meksika, bahamai, kuba, grenlandija, havajai, bermuda,
                gvatemala, belizas, honduras, salvadoras, nikaragva, kosta_rika, panama, jamaika,
                bahamai, haitis, dominikos_respublika, puerto_rikas, venesuela, kolumbija, gajana, surinamas,
                ekvadoras, peru, bolivija, brazilija, paragvajus, urugvajus, argentina, cile, islandija, norvegija, 
                svedija, suomija, danija, airija, anglija, belgija, liuksenburgas, olandija, vokietija, prancuzija, 
                monakas, sveicarija, austrija, lichtensteinas, vengrija, lenkija, cekija, slovakija, ispanija, andora,
                portugalija, italija, san_marinas, vatikanas, slovenija, malta, kroatija, bosnija_hercogovina, makedonija,
                albanija, graikija, bulgarija, estija, latvija, lietuva, baltarusija, moldova, rumunija, ukraina, 
                rusija, gruzija, armenija, azerbaidzanas, turkija, kipras, sirija, izraelis, libanas, jordanija, irakas,
                iranas, saudo_arabija, kuveitas, bahreinas, kataras, jae, omanas, jemenas, kazachstanas, uzbekistanas,
                turkmenistanas, tadzikistanas, kirgizija, afganistanas, pakistanas, indija, bangladesas, nepalas, 
                butanas, sri_lanka, maldyvai, madagaskaras, taivanas, kinija, mongolija, siaures_koreja, pietu_koreja, japonija,
                tailandas, birma, vietnamas, kambodza, laosas, brunejus, singapuras, malaizija, indonezija, rytu_timoras, filipinai,
                marokas, alzyras, tunisas, libija, egiptas, sudanas, somalis, etiopija, eritreja, dzibutis, mauritanija, malis,
                nigeris, senegalas, gambija, bisau_gvineja, gvineja, siera_leone, liberija, togas, dramblio_kk, gana, nigerija, 
                burkina_fasas, beninas, zambija, kamerunas, car, pusiaujo_gvineja, cadas, gabonas, kongas, kongo_dr, uganda, 
                burundis, kenija, tanzanija, malavis, angola, botsvana, namibija, zimbabve, mozambikas, par, svazilandas, lesotas, 
                australija, n_zelandija] 

euro_country = [islandija, norvegija, 
                svedija, suomija, danija, airija, anglija, belgija, liuksenburgas, olandija, vokietija, prancuzija, 
                monakas, sveicarija, austrija, lichtensteinas, vengrija, lenkija, cekija, slovakija, ispanija, andora,
                portugalija, italija, san_marinas, vatikanas, slovenija, malta, kroatija, bosnija_hercogovina, makedonija,
                graikija, bulgarija, estija, latvija, lietuva, baltarusija, moldova, rumunija, ukraina]

asia_country = [albanija, rusija, gruzija, armenija, azerbaidzanas, turkija, kipras, sirija, izraelis, libanas, jordanija, irakas,
                iranas, saudo_arabija, kuveitas, bahreinas, kataras, jae, omanas, jemenas, kazachstanas, uzbekistanas,
                turkmenistanas, tadzikistanas, kirgizija, afganistanas, pakistanas, indija, bangladesas, nepalas, 
                butanas, sri_lanka, maldyvai, madagaskaras, taivanas, kinija, mongolija, siaures_koreja, pietu_koreja, japonija,
                tailandas, birma, vietnamas, kambodza, laosas, brunejus, singapuras, malaizija, indonezija, rytu_timoras, filipinai]

africa_country = [marokas, alzyras, tunisas, libija, egiptas, sudanas, somalis, etiopija, eritreja, dzibutis, mauritanija, malis,
                nigeris, senegalas, gambija, bisau_gvineja, gvineja, siera_leone, liberija, togas, dramblio_kk, gana, nigerija, 
                burkina_fasas, beninas, zambija, kamerunas, car, pusiaujo_gvineja, cadas, gabonas, kongas, kongo_dr, uganda, 
                burundis, kenija, tanzanija, malavis, angola, botsvana, namibija, zimbabve, mozambikas, par, svazilandas, lesotas]

america_country = [jav, kanada, meksika, bahamai, kuba, grenlandija, havajai, bermuda,
                gvatemala, belizas, honduras, salvadoras, nikaragva, kosta_rika, panama, jamaika,
                bahamai, haitis, dominikos_respublika, puerto_rikas, venesuela, kolumbija, gajana, surinamas,
                ekvadoras, peru, bolivija, brazilija, paragvajus, urugvajus, argentina, cile]


random.shuffle(world_country)
random.shuffle(euro_country)
random.shuffle(asia_country)
random.shuffle(africa_country)
random.shuffle(america_country)

def all_world():
    health = 3
    score = 0
    x=0
    while health > 0 and x < 167:
        

        country_choice = world_country[x]
        c_choice  = country_choice.capital
        question_text = 'Šalis: '+ country_choice.country


        
        hint = c_choice[0:3]
        print('\n',question_text)

        answer = input('Sostinė: ')
    
        if answer.lower() == 'pagalba':
            print('\nPirmosios', country_choice.country,'trys raidės yra', hint)
            answer = input('Atsakymas: ')
            health = health - 1
        if answer.lower() == c_choice.lower():
            print('!<>! TEISINGAI!<>!')
            health=health+0.5
            print('Tau liko', health, 'gyvybių')
            score = score +1
        if answer.lower() != c_choice.lower():
            print('NETEISINGAI!')
            print('Teisingas atsakymas yra -', c_choice.upper())
            health = health -1
            print('Tau liko', health, 'gyvybių')
        
        x+=1
    
    
        if x == 167:
            print('Žaidimas baigtas, atsakei į',score, 'iš 167')
        if health <= 0:
            print('\nBaigėsi gyvybės!!! Atsakei į', score, 'iš 167')

def euro():
    health = 3
    score = 0
    x=0
    while health > 0 and x < 39:
        

        country_choice = euro_country[x]
        c_choice  = country_choice.capital
        question_text = 'Šalis: '+ country_choice.country
        
        hint = c_choice[0:3]
        print('\n',question_text)

        answer = input('Sostinė: ')
    
        if answer.lower() == 'pagalba':
            print('\nPirmosios', country_choice.country,'trys raidės yra', hint)
            answer = input('Atsakymas: ')
            health = health - 1
        if answer.lower() == c_choice.lower():
            print('!<>! TEISINGAI!<>!')
            health=health+0.5
            print('Tau liko', health, 'gyvybių')
            score = score +1
        if answer.lower() != c_choice.lower():
            print('NETEISINGAI!')
            print('Teisingas atsakymas yra -', c_choice.upper())
            health = health -1
            print('Tau liko', health, 'gyvybių')
        
        x+=1
    
    
        if x == 39:
            print('Žaidimas baigtas, atsakei į',score, 'iš 39')
        if health <= 0:
            print('\nBaigėsi gyvybės!!! Atsakei į', score, 'iš 39')

def asia():
    health = 3
    score = 0
    x=0
    while health > 0 and x < 50:
        

        country_choice = asia_country[x]
        c_choice  = country_choice.capital
        question_text = 'Šalis: '+ country_choice.country
        
        hint = c_choice[0:3]
        print('\n',question_text)

        answer = input('Sostinė: ')
    
        if answer.lower() == 'pagalba':
            print('\nPirmosios', country_choice.country,'trys raidės yra', hint)
            answer = input('Atsakymas: ')
            health = health - 1
        if answer.lower() == c_choice.lower():
            print('!<>! TEISINGAI!<>!')
            health=health+0.5
            print('Tau liko', health, 'gyvybių')
            score = score +1
        if answer.lower() != c_choice.lower():
            print('NETEISINGAI!')
            print('Teisingas atsakymas yra -', c_choice.upper())
            health = health -1
            print('Tau liko', health, 'gyvybių')
        
        x+=1
    
    
        if x == 50:
            print('Žaidimas baigtas, atsakei į',score, 'iš 50')
        if health <= 0:
            print('\nBaigėsi gyvybės!!! Atsakei į', score, 'iš 50')
            
def africa():
    health = 3
    score = 0
    x=0
    while health > 0 and x < 46:
        

        country_choice = africa_country[x]
        c_choice  = country_choice.capital
        question_text = 'Šalis: '+ country_choice.country
        
        hint = c_choice[0:3]
        print('\n',question_text)

        answer = input('Sostinė: ')
    
        if answer.lower() == 'pagalba':
            print('\nPirmosios', country_choice.country,'trys raidės yra', hint)
            answer = input('Atsakymas: ')
            health = health - 1
        if answer.lower() == c_choice.lower():
            print('!<>! TEISINGAI!<>!')
            health=health+0.5
            print('Tau liko', health, 'gyvybių')
            score = score +1
        if answer.lower() != c_choice.lower():
            print('NETEISINGAI!')
            print('Teisingas atsakymas yra -', c_choice.upper())
            health = health -1
            print('Tau liko', health, 'gyvybių')
        
        x+=1
    
    
        if x == 46:
            print('Žaidimas baigtas, atsakei į',score, 'iš 46')
        if health <= 0:
            print('\nBaigėsi gyvybės!!! Atsakei į', score, 'iš 46')

def america():
    health = 3
    score = 0
    x=0
    while health > 0 and x < 30:
        

        country_choice = america_country[x]
        c_choice  = country_choice.capital
        question_text = 'Šalis: '+ country_choice.country
        
        hint = c_choice[0:3]
        print('\n',question_text)

        answer = input('Sostinė: ')
    
        if answer.lower() == 'pagalba':
            print('\nPirmosios', country_choice.country,'trys raidės yra', hint)
            answer = input('Atsakymas: ')
            health = health - 1
        if answer.lower() == c_choice.lower():
            print('!<>! TEISINGAI!<>!')
            health=health+0.5
            print('Tau liko', health, 'gyvybių')
            score = score +1
        if answer.lower() != c_choice.lower():
            print('NETEISINGAI!')
            print('Teisingas atsakymas yra -', c_choice.upper())
            health = health -1
            print('Tau liko', health, 'gyvybių')
        
        x+=1
    
    
        if x == 30:
            print('Žaidimas baigtas, atsakei į',score, 'iš 30')
        if health <= 0:
            print('\nBaigėsi gyvybės!!! Atsakei į', score, 'iš 30')

print('\n              Žaidimo taisyklės           ')
print('~~!!!!!!######@@@@@@@######!!!!!!~~')
print('Pradėjus žaidimą turite 3 gyvybes, už kiekvieną teisingą atsakymą gausite 0.5 papildomos gyvybės, už neteisinga prarasite 1 !!!.\nJeigu reikia pagalbos į atsakymo laukelį surinkite "pagalba" ir bus pateiktos trys pirmos šalies sostinės raidės, bet tai kainuos vieną gyvybę.\nSekmės!')
print('~~!!!!!!######@@@@@@@######!!!!!!~~')


print('\nEuropos šalys - įrašykite "EUROPA"\nAzijos šalys - įrašykite "AZIJA"\nŠiaurės ir Pietų Amerika - įrašykite "AMERIKA"\nVisas pasaulis - įrašykite "ALL"')
class_choice = input('\nPasirinkimas: ')


    
if class_choice.lower() == 'all':
    print('\nPasirinkote visas pasaulio šalis.\nŽaidimas prasideda.Sekmės!')
    all_world()
elif class_choice.lower() == 'europa':
    print('\nPasirinkote Europos šalis.\nŽaidimas prasideda.Sekmės!')
    euro()
elif class_choice.lower() == 'azija':
    print('\nPasirinkote Azijos šalis.\nŽaidimas prasideda.Sekmės!')
    asia()
elif class_choice.lower() == 'afrika':
    print('\nPasirinkote Afrikos šalis.\nŽaidimas prasideda.Sekmės!')
    africa()
elif class_choice.lower() == 'amerika':
    print('\nPasirinkote Šiaurės ir Pietų Amerikos šalis.\nŽaidimas prasideda.Sekmės!')
    america()
else:
    print('Pasirinkimo klaida')


