# -*- encoding: utf-8 -*-
drink_list = [{
        'name': 'Vesper',
        'ingredients': {
            'gin': 60,
            'vodka': 15.0,
            'vermouth': 7.5
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Bacardi Cocktail',
        'ingredients': {
            'whiteRum': 45.0,
            'lej': 20,
            'grenadine': 10
        },
        'prep': 'Kasper mener: Et lidt kedeligt,',
        'prep1':  'men sikkert valg. Bortset fra lidt',
        'prep2': 'grenadine er der ikke meget farve ved',
        'prep3': 'den her. 5 ud af 10 stjerner fra mig',
    },
    {
        'name': 'Negroni',
        'ingredients': {
            'gin': 30,
            'campari': 30,
            'vermouth': 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Rose',
        'ingredients': {
            'cherryBrandy': 20,
            'vermouth': 40
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['3 dashes Strawberry syrup']
    },
    {
        'name': 'Old Fashioned',
        'ingredients': {
            'whiskey': 45.0
        },
        'prep': 'R fra prep der tilhøre old Fashioned40k',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['2 dashes Angostura Bitters',
        '1 sugar cube']
    },
    {
        'name': 'Tuxedo',
        'ingredients': {
            'gin': 30,
            'vermouth': 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['1/2 bar spoon Maraschino',
        '1/4 bar spoon Absinthe',
        '3 dashes Orange Bitters']
    },
    {
        'name': 'Mojito',
        'ingredients': {
            'whiteRum': 45,
            'soda': 45,
            'sugar': 45,
            'lej': 25
        },
        'prep': 'TILFØJ: En ske knust mynte ',
        'prep1':  '',
        'prep2': '',
        'prep3': '',
        'specials': ['2 teaspoons white sugar',
        'Soda water']
    },
    {
        'name': "Horse's Neck",
        'ingredients': {
            'brandy': 40,
            'gingerAle': 120
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['Dash of Angostura bitters (optional)']
    },
    {
        'name': "Planter's Punch",
        'ingredients': {
            'darkRum': 45.0,
            'oj': 35.0,
            'pj': 35.0,
            'lej': 20,
            'grenadine': 10
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['3 to 4 dashes Angostura bitters']
    },
    {
        'name': 'Sea Breeze',
        'ingredients': {
            'vodka': 40,
            'cj': 120,
            'gj': 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Pisco Sour',
        'ingredients': {
            'brandy': 45.0,
            'lej': 30,
            'grenadine': 20
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['1 raw egg white (small egg)']
    },
    {
        'name': 'Long Island Iced Tea',
        'ingredients': {
            'tequila': 15.0,
            'vodka': 15.0,
            'whiteRum': 15.0,
            'tripSec': 15.0,
            'gin': 15.0,
            'lej': 15.0,
            'cola': 30.0
        },
        'prep': 'Kasper mener: Du er godt nok modig',
        'prep1':  'men det kunne jeg have sagt mig',
        'prep2': 'selv. Du kender jo trods alt mig.',
        'prep3': '8 ud af 10 stjerner herfra',
        'specials': ['1 dash of Cola']
    },
    {
        'name': 'Clover Club',
        'ingredients': {
            'gin': 45.0,
            'grenadine': 15.0,
            'lej': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Angel Face',
        'ingredients': {
            'gin': 30,
            'apricotBrandy': 30,
            'appleBrandy': 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Mimosa',
        'ingredients': {
            'champagne': 75.0,
            'oj': 75.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Whiskey Sour',
        'ingredients': {
            'whiskey': 45.0,
            'lej': 30.0,
            'grenadine': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Screwdriver',
        'ingredients': {
            'vodka': 40,
            'oj': 100
        },
        'prep': 'Kasper mener: Den eneste',
        'prep1':  'skruetrækker, jeg bør komme',
        'prep2': 'i nærheden af. Men den er',
        'prep3': 'kedelig! 3 ud af 10 stjerner',
    },
    {
        'name': 'Cuba Libre',
        'ingredients': {
            'whiteRum': 50,
            'cola': 120,
            'lej': 10
        },
        'prep': 'Kasper mener: Navnet får den til at lyde',
        'prep1':  'meget mere fancy end den er.',
        'prep2': 'Derfor kan jeg kun give 3 ud af 10',
        'prep3': 'stjerner. Og jeg tager aldrig fejl!',
    },
    {
        'name': 'Manhattan',
        'ingredients': {
            'whiskey': 50,
            'vermouth': 20
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['1 dash Angostura Bitters']
    },
    {
        'name': 'Porto Flip',
        'ingredients': {
            'brandy': 15.0,
            'port': 45.0,
            'eggYolk': 10
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Gin Fizz',
        'ingredients': {
            'gin': 45.0,
            'lej': 30,
            'grenadine': 10,
            'soda': 80
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Espresso Martini',
        'ingredients': {
            'vodka': 50,
            'coffeeLiqueur': 10
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['Sugar syrup (according to individual preference of sweetness)',
'1 short strong Espresso']
    },
    {
        'name': 'Margarita',
        'ingredients': {
            'tequila': 35.0,
            'tripSec': 20,
            'lej': 15.0
        },
        'prep': 'Kasper mener: 100 gange bedre',
        'prep1':  'end pizzaen. Simpel og lækker. ',
        'prep2': 'Hvem minder det dig om?',
        'prep3': 'Antal stjerner afhænger af dit svar',
    },
    {
        'name': 'French 75',
        'ingredients': {
            'gin': 30,
            'lej': 15.0,
            'champagne': 60
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['2 dashes Sugar syrup']
    },
    {
        'name': 'Yellow Bird',
        'ingredients': {
            'whiteRum': 30,
            'galliano': 15.0,
            'tripSec': 15.0,
            'lij': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Pina Colada',
        'ingredients': {
            'whiteRum': 45,
            'pj': 135
        },
        'prep': 'Kasper mener: Den her drikkes',
        'prep1':  'bedst på en Hawaii-strand.',
        'prep2': 'TILFØJ: EN STOR OG EN LILLE',
        'prep3': 'KOP KOKOSMÆLK',
    },
    {
        'name': 'Aviation',
        'ingredients': {
            'gin': 45.0,
            'cherryLiqueur': 15.0,
            'lej': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Bellini',
        'ingredients': {
            'prosecco': 100,
            'peachPuree': 50
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Grasshopper',
        'ingredients': {
            'cremeCacao': 30,
            'cream': 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Tequila Sunrise',
        'ingredients': {
            'tequila': 45.0,
            'oj': 90,
            'grenadine': 15.0
        },
        'prep': 'Kasper mener: En sikker',
        'prep1':  'vinder hos de ældre.',
        'prep2': 'Måske derfor, jeg synes om den.',
        'prep3': '6 ud af 10 stjerner.',
    },
    {
        'name': 'Teddy Bear',
        'ingredients': {
            'vodka': 30,
            'tripSec': 30,
            'lej': 30,
            'oj': 30
        },
        'prep': '',
        'prep1': '',
        'prep2': '',
        'prep3': '',
        'specials': ['1 dash Angostura Bitters']
    },
    {
        'name': 'Daiquiri',
        'ingredients': {
            'whiteRum': 45.0,
            'lej': 25.0,
            'grenadine': 15.0
        },
        'prep': 'Kasper mener: Mindre tøset end',
        'prep1':  'jordbærudgaven. Både for kvinder og',
        'prep2': 'tøsedrenge. 6 ud af 10 stjerner.',
        'prep3': 'Skål!',
    },
    {
        'name': 'Gimlet',
        'ingredients': {
            'gin': 60.0,
            'lej': 15.0,
            'sugar': 15.0,
         },
        'prep': 'Kasper mener: Minder lidt om det,',
        'prep1': 'en privatdetektiv drikker i film.',
        'prep2': 'Det ville jeg nok være god til.',
        'prep3': '',
    },
{
        'name': 'Monkey Gland',
        'ingredients': {
            'gin': 45.0,
            'grenadine': 10.0,
            'oj': 30.0,

        },
        'prep': 'Kasper mener: Ved du,',
        'prep1': 'hvad gland betyder?',
        'prep2': 'Det er på eget ansvar. ',
        'prep3': 'Held og lykke',
    },
 {
        'name': 'Tooty Fruity',
        'ingredients': {
            'vodka': 30.0,
            'tripSec': 30.0,
            'grenadine': 15.0,
            'pj': 30.0,
            'oj': 30.0,
        },
         'prep': '',
        'prep1': '',
        'prep2': '',
        'prep3': '',
    },
{
        'name': 'Test pumpe 8',
        'ingredients': {
            'oj': 100.0,
        },
         'prep': '100 ml',
        'prep1': 'Stor pumpe',
        'prep2': '',
        'prep3': '',
    },
{
        'name': 'Test pumpe 1',
        'ingredients': {
            'sugar': 100.0,
        },
         'prep': '100 ml',
        'prep1': 'lille pumpe',
        'prep2': '',
        'prep3': '',
    },

{
        'name': 'Kamikaze',
        'ingredients': {
            'vodka': 45.0,
            'lej': 30.0,
            'tripSec': 30.0,
        },
        'prep': 'Kasper mener: Voldsomt navn,',
        'prep1': 'men du behøver ikke',
        'prep2': 'gå kamikaze når du',
        'prep3': 'drikker den. En 7er',
    },
{
        'name': 'Horney Bull',
        'ingredients': {
            'tequila': 45.0,
            'oj': 150.0
        },
        'prep': 'Kasper mener: En drink ,',
        'prep1': 'til de kedelige typer. .',
        'prep2': 'Sådan nogle kender jeg ',
        'prep3': 'åbenbart også. 2 stjerner',
    },
    {
        'name': 'John Collins',
        'ingredients': {
            'gin': 45.0,
            'lej': 30.0,
            'soda': 60.0
        },
        'prep': 'Kasper mener: Hvem er ham John',
        'prep1': 'Collins? Aner det ikke, men du',
        'prep2': 'møder ham snart.',
        'prep3': '',
    },
    {
        'name': 'Rusty Nail',
        'ingredients': {
            'whiskey': 25.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'B52',
        'ingredients': {
            'coffeeLiqueur': 20,
            'baileys': 20,
            'tripSec': 20
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Stinger',
        'ingredients': {
            'brandy': 50,
            'cremeCacao': 20
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Golden Dream',
        'ingredients': {
            'galliano': 20,
            'tripSec': 20,
            'oj': 20,
            'cream': 10
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'God Mother',
        'ingredients': {
            'vodka': 35.0,
            'amaretto': 35.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Spritz Veneziano',
        'ingredients': {
            'prosecco': 60,
            'aperol': 40
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['Splash of Soda water']
    },
    {
        'name': 'Bramble',
        'ingredients': {
            'gin': 40,
            'lej': 15.0,
            'grenadine': 10,
            'blackberryLiqueur': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Alexander',
        'ingredients': {
            'brandy': 30,
            'cremeCacao': 30,
            'cream': 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Lemon Drop Martini',
        'ingredients': {
            'vodka': 25.0,
            'tripSec': 20,
            'lej': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'French Martini',
        'ingredients': {
            'vodka': 45.0,
            'raspberryLiqueur': 15.0,
            'pj': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Black Russian',
        'ingredients': {
            'vodka': 50,
            'coffeeLiqueur': 20
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    },
    {
        'name': 'Bloody Mary',
        'ingredients': {
            'vodka': 45.0,
            'tj': 90,
            'lej': 15.0
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
        'specials': ['2 to 3 dashes of Worcestershire Sauce','Tabasco','Celery salt','Pepper']
    },
    {
        'name': 'Mai-tai',
        'ingredients': {
            'whiteRum': 40,
            'darkRum': 20,
            'tripSec': 15.0,
            'grenadine': 15.0,
            'lij': 10
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    }, {

        "name": "Madras",
        "ingredients": {

            "vodka": 45,
            "cj": 90,
            "oj": 30
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    }, {

        "name": "Lemon Drop",
        "ingredients": {

            "vodka": 40,
            "lej": 40,
            "grenadine": 15
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    }, {

        "name": "Cape Cod",
        "ingredients": {

            "vodka": 35,
            "cj": 135
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    }, {

        "name": "Bourbon Squash",
        "ingredients": {

            "whisky": 45,
            "oj": 50,
            "lej": 30,
            "grenadine": 20
        },
        'prep': 'ÆØÅ dette er prep',
        'prep1':  'ÆØÅ Detter er prep1',
        'prep2': 'ÆØÅ Dette er prep2',
        'prep3': 'ÆØÅ Dette er prep3',
    } 
     ]
    
    #, "pump_7": {"value": "tripSec", "name": "Pump 7", "pin": 10}, "pump_8": {"value": "oj", "name": "Pump 8", "pin": 9}

drink_options = [
    {
        "name": "Gin",
        "value": "gin"
    },
    {
        "name": "White Rum",
        "value": "whiteRum"
    },
    {
        "name": "Dark Rum",
        "value": "darkRum"
    },
    {
        "name": "Coconut Rum",
        "value": "coconutRum"
    },
    {
        "name": "Vodka",
        "value": "vodka"
    },
    {
        "name": "Tequila",
        "value": "tequila"
    },
    {
        "name": "Tonic Water",
        "value": "tonic"
    },
    {
        "name": "Coke",
        "value": "coke"
    },
    {
        "name": "Orange Juice",
        "value": "oj"
    },
    {
        "name": "Margarita Mix",
        "value": "mmix"
    },
    {
        "name": "Cranberry Juice",
        "value": "cj"
    },
    {
        "name": "Pineapple Juice",
        "value": "pj"
    },
    {
        "name": "Apple Juice",
        "value": "aj"
    },
    {
        "name": "Grapefruit Juice",
        "value": "gj"
    },
    {
        "name": "Tomato Juice",
        "value": "tj"
    },
    {
        "name": "Lime Juice",
        "value": "lij"
    },
    {
        "name": "Lemon Juice",
        "value": "lej"
    },
    {
        "name": "Whiskey",
        "value": "whiskey"
    },
    {
        "name": "Triple Sec",
        "value": "tripSec"
    },
    {
        "name": "Grenadine",
        "value": "grenadine"
    },
    {
        "name": "Vermouth",
        "value": "vermouth"
    },
    {
        "name": "Soda",
        "value": "soda"
    },
    {
        "name": "Peach Schnapps",
        "value": "peachSchnapps"
    },
    {
        "name": "Midori",
        "value": "midori"
    },
    {
        "name": "Presecco",
        "value": "prosecco"
    },
    {
        "name": "Cherry Brandy",
        "value": "cherryBrandy"
    },
    {
        "name": "Apple Brandy",
        "value": "appleBrandy"
    },
    {
        "name": "Apricot Brandy",
        "value": "apricotBrandy"
    },
    {
        "name": "Brandy (generic)",
        "value": "brandy"
    },
    {
        "name": "Champagne",
        "value": "champagne"
    },
    {
        "name": "Cola",
        "value": "cola"
    },
    {
        "name": "Port",
        "value": "port"
    },
    {
        "name": "Coconut Milk",
        "value": "coconutMilk"
    },
    {
        "name": "Creme de Cacao",
        "value": "cremeCacao"
    },
    {
        "name": "Grenadine",
        "value": "grenadine"
    },
      {
        "name": "Tom",
        "value": "Tom"
    },
{
        "name": "Sugar",
        "value": "sugar"
    },
]


# Check for ingredients that we don 't have a record for
if __name__ == "__main__":
    found = []
    drinks = [x["value"] for x in drink_options]
    for D in drink_list:
        for I in D["ingredients"]:
            if I not in drinks and I not in found:
                found.append(I)
    print(I)
