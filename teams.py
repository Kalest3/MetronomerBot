import random
import re
def PackATeam(team:str):
    PackedTeam = ''
    searchPokemon = team.find('@')
    Pokemon = team[0:searchPokemon]
    print(Pokemon)
    PokemonHaveGender = False
    if "(M)" in Pokemon != False:
        PokemonHaveGender = True
        isMale = True
        isFemale = False
        Pokemon = Pokemon.replace("(M)", "")
    if "(F)" in Pokemon != False:
        PokemonHaveGender = True
        isMale = False
        isFemale = True
        Pokemon = Pokemon.replace("(F)", "")
    Pokemon = Pokemon.strip()
    Nickname = Pokemon
    if " (" in Pokemon != False:
        Space = team.find(' ')
        Nickname = team[0:Space]
        Nickname = Nickname.strip()
        searchParenteses = Pokemon.find('(')
        searchParenteses2 = Pokemon.rfind(')')
        Pokemon = Pokemon[searchParenteses:searchParenteses2]
        Pokemon = Pokemon.replace('(', '')
    PackedTeam += f'{Nickname}|{Pokemon}|'
    ItemSearch = re.compile(r'[\n\r].*{}\s*([^\n\r]*)'.format(" @ "))
    Item = ItemSearch.findall(team)
    Item = str(Item)
    Item = Item.replace('[', '')
    Item = Item.replace(']', '')
    Item = Item.replace("'", '')
    Item = Item.replace(' ', '')
    Item = Item.strip()
    Item = Item.lower()
    PackedTeam += f'{Item}|'
    AbilitySearch = re.compile(r'[\n\r].*Ability: \s*([^\n\r]*)') 
    Ability = AbilitySearch.findall(team)
    Ability = str(Ability)
    Ability = Ability.replace('[', '')
    Ability = Ability.replace(']', '')
    Ability = Ability.replace("'", '')
    Ability = Ability.replace(' ', '')
    Ability = Ability.strip()
    Ability = Ability.lower()
    Ability = Ability.split(",")[0]
    PackedTeam += f'{Ability}|'
    Move = 'metronome'
    PackedTeam += f'{Move}|'
    NatureSearch = re.compile("\w+\s" + "Nature")
    Nature = NatureSearch.findall(team)
    Nature = str(Nature)
    Nature = Nature.replace('[', '')
    Nature = Nature.replace(']', '')
    Nature = Nature.replace("'", '')
    Nature = Nature.replace('Nature', '')
    Nature = Nature.replace(' ', '')
    Nature = Nature.strip()
    Nature = Nature.lower()
    Nature = Nature.split(",")[0]
    PackedTeam += f'{Nature}|'
    EvsSearch = re.compile(r"[\n\r].*EVs: \s*([^\n\r]*)")
    EVs = EvsSearch.findall(team)
    EVs = str(EVs)
    EVs = EVs.replace('[', '')
    EVs = EVs.replace(']', '')
    EVs = EVs.replace("'", '')
    EVs = EVs.replace(' ', '')
    EVs = EVs.strip()
    EVs = EVs.lower()
    EVs = EVs.split(",")[0]
    EVs = EVs.replace('hp', '')
    EVs = EVs.replace('atk', '')
    EVs = EVs.replace('def', '')
    EVs = EVs.replace('spa', '')
    EVs = EVs.replace('spd', '')
    EVs = EVs.replace('spe', '')
    EVs = EVs.replace('/', ',')
    PackedTeam += f'{EVs}|'
    print(PokemonHaveGender)
    if PokemonHaveGender == True:
        if isMale != False:
            PackedTeam += 'M|'
        elif isFemale != False:
            PackedTeam += 'F|'
    else:
        PackedTeam += '|'
        pass
    if 'IVs: ' in team != False:
        PackedTeam += 'IVS: 31,31,31,31,31,31|'
        onlyIVs = 'hp31,atk31,def31,spa31,spd31,spe31|'
        IVsDetect = re.compile(r'[\n\r].*IVs: \s*([^\n\r]*)') 
        IVs = IVsDetect.findall(team)
        IVs = str(IVs)
        IVs = IVs.replace('[', '')
        IVs = IVs.replace(']', '')
        IVs = IVs.replace("'", '')
        IVSpace = IVs.find(' ')
        Number = IVs[0:IVSpace]
        Number = Number.strip()
        IVs = IVs.replace(Number, '')
        IVs = IVs.strip()
        if IVs == 'HP':
            onlyIVs = onlyIVs.replace('hp31', Number)
        else:
            onlyIVs = onlyIVs.replace('hp31', '31')
        if IVs == 'Atk':
            onlyIVs = onlyIVs.replace('atk31', Number)
        else:
            onlyIVs = onlyIVs.replace('atk31', '31')
        if IVs == 'Def':
            onlyIVs = onlyIVs.replace('def31', Number)
        else:
            onlyIVs = onlyIVs.replace('def31', '31')
        if IVs == 'SpA':
            onlyIVs = onlyIVs.replace('spa31', Number)
        else:
            onlyIVs = onlyIVs.replace('spa31', '31')
        if IVs == 'SpD':
            onlyIVs = onlyIVs.replace('spd31', Number)
        else:
            onlyIVs = onlyIVs.replace('spd31', '31')
        if IVs == 'Spe':
            onlyIVs = onlyIVs.replace('spe31', Number)
        else:
            onlyIVs = onlyIVs.replace('spe31', '31')
        PackedTeam = PackedTeam.replace('IVS: 31,31,31,31,31,31|', onlyIVs)
        print(PackedTeam)
    
    else:
        PackedTeam += '|'
        
teams = [
"""Venusaur-Mega @ Weakness Policy  
Ability: Friend Guard  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD
IVs: 0 Spe
Naive Nature  
- Metronome  

Venusaur-Mega @ Weakness Policy  
Ability: Friend Guard  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD  
Sassy Nature  
- Metronome""",

"""Type: Null @ Eviolite  
Ability: Unaware  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Relaxed Nature  
- Metronome  

Type: Null @ Eviolite  
Ability: Unaware  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Sassy Nature  
- Metronome"""
]

choice = random.choice(teams)
PackATeam(choice)