def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if not all(isinstance(x, int) for x in [strength, intelligence, charisma]):
        return 'All stats should be integers'
    if any(x < 1 for x in [strength, intelligence, charisma]):
        return 'All stats should be no less than 1'
    if any(x > 4 for x in [strength, intelligence, charisma]):
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    return f"""{name}
STR {('●' * strength) + ('○' * (10 - strength))}
INT {('●' * intelligence) + ('○' * (10 - intelligence))}
CHA {('●' * charisma) + ('○' * (10 - charisma))}"""

print(create_character('ren', 4, 2, 1))