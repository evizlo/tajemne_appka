

seznam_typu = ['oheň', 'zbraň', 'artefakt' , 'armáda', 'vůdce',
               'počasí', 'země', 'potopa','tvor', 'čaroděj']

seznam_karet = [
    {'name' : 'Svíčka', 'body' : 2, 'typ' : 'oheň',
     'bonus': 'bkt',
     'efekt': [0, 100, 'plus', ['Kniha proměn' , 'Zvonice'], 'čaroděj']},
############################################################################    
    {'name' : 'Blesk', 'body' : 11, 'typ' : 'oheň',
     'bonus': 'bkt',
     'efekt' : [0, 30, 'any_karta', ["Bouře",], []]},
############################################################################    
    {'name' : 'Požár', 'body' : 40, 'typ' : 'oheň',
     'mazani': 'priorita_3',
     'efekt3': [['Hora', 'Stoletá voda', 'Ostrov', 'Jednorožec', 'Drak', ],
               ['armáda', 'vůdce', 'země', 'potopa', 'tvor']]},
############################################################################    
    {'name' : 'Kovárna', 'body' : 9, 'typ' : 'oheň',
     'bonus': 'bkt',
     'efekt' : [9, 0, 'every', [], ['zbraň', 'artefakt']]},
############################################################################    
    {'name' : 'Elementál ohně',    'body' : 4,   'typ' : 'oheň',
     'bonus': 'bkt',
     'efekt' : [15, 0, "every", [], 'oheň']},
############################################################################    
    {'name' : 'Elfský luk',        'body' : 3,   'typ' : 'zbraň',
     'bonus': 'bkt',
     'efekt' : [0, 30, 'any_karta',
               ['Elfí lučištníci', 'Velitel', 'Pán šelem'],[]]},
############################################################################   
    {'name' : 'Kethský meč',       'body' : 7,   'typ' : 'zbraň',
     'bonus': 'bkt',
     'efekt' : [10, 30, 'plus', ['Kethský štít'], 'vůdce']},
############################################################################    
    {'name' : 'Bojová vzducholoď', 'body' : 35,  'typ' : 'zbraň',
     'vymaz_masli': True,
     'vymaz_nemasli': True,
     'efekt3': [[], [['armáda'], ['počasí']]]},
############################################################################    
    {'name' : 'Magická hůl',       'body' : 1,   'typ' : 'zbraň',
     'bonus': 'bkt',
     'efekt' : [25, 0, 'plus', [], 'čaroděj']},
############################################################################    
    {'name' : 'Válečná loď',       'body' : 23,  'typ' : 'zbraň',
     'vymaz_nemasli': True,
     'odstran': 'exclusive',
     'efekt3': [[], ['potopa']],
     'efekt4': ['potopa', 'armáda']},
############################################################################    
    {'name' : 'Kniha proměn',      'body' : 3,   'typ' : 'artefakt'},
############################################################################    
    {'name' : 'Ochranná runa',     'body' : 1,   'typ' : 'artefakt',
     'bonus': 'pn' },
############################################################################    
    {'name' : 'Strom světa',       'body' : 2,   'typ' : 'artefakt',
     'bonus': 'nt'},
############################################################################
    {'name' : 'Kethský štít',      'body' : 4,   'typ' : 'artefakt',
     'bonus': 'bkt',
     'efekt' : [15, 25, 'plus', ['Kethský meč'], 'vůdce']},
############################################################################    
    {'name' : 'Krystal řádu',      'body' : 5,   'typ' : 'artefakt',
     'bonus': 'post'},
############################################################################    
    {'name' : 'Trpasličí pěchota', 'body' : 15,  'typ' : 'armáda',
     'postih': 'bkt',
     'efekt2' : [-2, 0, 'every', [], ['armáda']]},
############################################################################    
    {'name' : 'Těžká jízda',       'body' : 17,  'typ' : 'armáda',
     'postih': 'bkt',
     'efekt2' : [-2, 0, 'every', [], ['země']]},
############################################################################    
    {'name' : 'Hraničáři',         'body' : 5,   'typ' : 'armáda',
     'bonus': 'bkt',
     'efekt' : [10, 0, 'every', [], 'země'],
     'odstran': 'slovo',
     'efekt4' : 'armáda'},
############################################################################    
    {'name' : 'Rytířky',           'body' : 20,  'typ' : 'armáda',
     'postih': 'bkt',
     'efekt2' : [-8, 0, 'nope', [], ['vůdce']]},
############################################################################    
    {'name' : 'Elfí lučištníci',    'body' : 10,  'typ' : 'armáda',
     'bonus': 'bkt',
     'efekt' : [5, 0, 'nope', [], ['počasí']]},
############################################################################    
    {'name' : 'Velitel',           'body' : 4,   'typ' : 'vůdce',
     'bonus': 'bkt',
     'efekt' : [0, 0, 'součet', [], 'armáda']},
############################################################################    
    {'name' : 'Princezna',         'body' : 2,   'typ' : 'vůdce',
     'bonus': 'bkt',
     'efekt' : [8, 0, 'every', [], ['armáda', 'čaroděj', 'vůdce']]},
############################################################################    
    {'name' : 'Císařovna',         'body' : 15,  'typ' : 'vůdce',
     'bonus': 'bkt',
     'efekt' : [10, 0, 'every', [], 'armáda'],
     'postih' : 'bkt',
     'efekt2' : [-5, 0, 'every', [], ['vůdce']]},
############################################################################    
    {'name' : 'Královna',          'body' : 6,   'typ' : 'vůdce',
     'bonus': 'bkt',
     'efekt' : [5, 15, 'plus_every', ['Král'], 'armáda']},
############################################################################    
    {'name' : 'Král',              'body' : 8,   'typ' : 'vůdce',
     'bonus': 'bkt',
     'efekt' : [5, 15, 'plus_every', ['Královna'], 'armáda']},
############################################################################    
    {'name' : 'Bouře',             'body' : 8,   'typ' : 'počasí',
     'bonus': 'bkt',
     'efekt' : [10, 0, 'every', [], 'potopa'],
     'mazani': 'priorita_1',
     'efekt3': [['Blesk'], ['oheň']]},
############################################################################    
    {'name' : 'Tornádo',           'body' : 13,  'typ' : 'počasí',
     'bonus': 'bkt',
     'efekt': [0, 40, 'vice_spec', [['Bouře'],
              ['Sněhová vánice', 'Stoletá voda']], []]},
############################################################################
    {'name' : 'Sněhová vánice',    'body' : 30,  'typ' : 'počasí',
     'postih': 'bkt',
     'efekt2' : [-5, 0, 'every', [], ['armáda', 'vůdce', 'tvor', 'oheň']],
     'mazani': 'priorita_1',
     'efekt3': [[], 'potopa']},
############################################################################
    {'name' : 'Kouř',              'body' : 27,  'typ' : 'počasí',
     'vymaz_nemasli': True,
     'efekt3': [[], ['oheň']]},
############################################################################
    {'name' : 'Elementál vzduchu', 'body' : 4,   'typ' : 'počasí',
     'bonus': 'bkt',
     'efekt' : [15, 0, 'every', [], 'počasí']},
############################################################################
    {'name' : 'Les',               'body' : 7,   'typ' : 'země',
     'bonus': 'bkt',
     'efekt': [12, 12, 'every', ['Elfí lučištníci'], 'tvor']},
############################################################################
    {'name' : 'Hora',              'body' : 9,   'typ' : 'země',
     'bonus': 'bkt',
     'efekt' : [0, 50, 'plus', ['Kouř' , 'Požár'], 'bez'],
     'odstran' : 'odstr',
     'efekt4' : 'potopa'},
############################################################################
    {'name' : 'Jeskyně',           'body' : 6,   'typ' : 'země',
     'bonus': 'bkt',
     'efekt': [0, 25, 'any_karta',
              ['Trpasličí pěchota', 'Drak'],[]],
     'odstran': 'odstr',
     'efekt4' : 'počasí'},
############################################################################
    {'name' : 'Zvonice',           'body' : 8,   'typ' : 'země',
     'bonus': 'bkt',
     'efekt': [15, 0, 'plus', [], 'čaroděj']},
############################################################################
    {'name' : 'Elementál země',    'body' : 4,   'typ' : 'země',
     'bonus': 'bkt',
     'efekt': [15, 0, 'every', [], 'země']},
############################################################################
    {'name' : 'Elementál vody',    'body' : 4,   'typ' : 'potopa',
     'bonus': 'bkt',
     'efekt': [15, 0, 'every', [], 'potopa']},
############################################################################
    {'name' : 'Fontána života',    'body' : 1,   'typ' : 'potopa',
     'bonus': 'ret',
     'efekt': ['přidej', ['zbraň', 'potopa', 'oheň', 'země', 'počasí']]},
############################################################################
    {'name' : 'Stoletá voda',      'body' : 32,  'typ' : 'potopa',
     'mazani': 'priorita_2',
     'efekt3': [['Hora', 'Blesk'], ['armáda','země', 'oheň']]},
############################################################################
    {'name' : 'Ostrov',            'body' : 14,  'typ' : 'potopa'},
############################################################################
    {'name' : 'Bažina',            'body' : 18,  'typ' : 'potopa',
     'postih': 'bkt',
     'efekt2' : [-3, 0, 'every', [], ['armáda', 'oheň']]},
############################################################################
    {'name' : 'Válečný oř',        'body' : 6,   'typ' : 'tvor',
     'bonus': 'bkt',
     'efekt' : [14, 0, 'any_typ', [], ['vůdce', 'čaroděj']]},
############################################################################
    {'name' : 'Drak',              'body' : 30,  'typ' : 'tvor',
     'postih': 'bkt',
     'efekt2' : [-40, 0, 'nope', [], ['čaroděj']]},
############################################################################
    {'name' : 'Bazilišek',         'body' : 35,  'typ' : 'tvor',
     'mazani': 'priorita_4',
     'efekt3': [[], ['armáda', 'vůdce', 'tvor']]},
############################################################################
    {'name' : 'Jednorožec',        'body' : 9,   'typ' : 'tvor',
     'bonus': 'bkt',
     'efekt': [0, [30, 15], 'mene_spec',
              [['Princezna'], ['Císařovna', 'Královna', 'Kouzelnice']],[]]},
############################################################################
    {'name' : 'Hydra',             'body' : 12,  'typ' : 'tvor',
     'bonus': 'bkt',
     'efekt': [0, 28, 'any_karta', ['Bažina'], []]},
############################################################################
    {'name' : 'Sběratel',          'body' : 7,   'typ' : 'čaroděj',
     'bonus': 'mt'},
############################################################################
    {'name' : 'Kouzelnice',        'body' : 5,   'typ' : 'čaroděj',
     'bonus': 'bkt',
     'efekt': [5, 0, 'every', [], ['země', 'počasí', 'potopa', 'oheň']]},
############################################################################    
    {'name' : 'Nekromant',         'body' : 3,   'typ' : 'čaroděj',
     'bonus': 'pl'},
############################################################################
    {'name' : 'Nejvyšší mág',      'body' : 25,  'typ' : 'čaroděj',
     'postih': 'bkt',
     'efekt2': [-10, 0, 'every', [], ['čaroděj', 'vůdce']]},
############################################################################
    {'name' : 'Pán šelem',         'body' : 9,   'typ' : 'čaroděj',
     'bonus': 'bkt',
     'efekt': [9, 0, 'every', [], 'tvor'],
     'odstran' : 'odstr',
     'efekt4' : 'tvor'},
############################################################################    
    {'name' : 'Šašek',         'body' : 3,   'typ' : 'čaroděj',
     'bonus': 'lc'}
     ]

