from unicodedata import normalize
from re import sub

def normalize_player_name(name:str | None) -> str:
    if not name:
        return None
    # Normalize to NFKD Unicode form to separate diacritics
    normalized_name = normalize('NFKD', name)
    # Remove any character that is not a letter, digit, or whitespace
    normalized_name = sub(r'[^\w\s]', '', normalized_name)
    # Convert to lowercase
    normalized_name = normalized_name.lower()
    # Remove leading and trailing whitespaces
    normalized_name = normalized_name.strip()
    # Remove ( ) from the name
    normalized_name = normalized_name.replace('(','').replace(')','')
    return normalized_name

def split_name(name:str) -> dict[str, str]:
    name = normalize_player_name(name).split(' ')
    return_dict = {'first_name':None, 'last_name':None}

    if len(name) == 1:
        return_dict['last_name'] = name[0]

    else:
        if name[0] == 'van' or name[0] == 'von' or name[0] == 'de' or name[0] == 'del' or name[0] == 'della' or name[0] == 'di' or name[0] == 'li' or name[0] == 'la' or name[0] == 'mac':
            return_dict['last_name'] = ' '.join(name)

        else:
            return_dict['first_name'] = name[0]
            return_dict['last_name'] = ' '.join(name[1:])
    return return_dict