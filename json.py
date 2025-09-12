import re
def parser_json(json_string : str):
    parsed_data = _parser_value(json_string.strip())
    return JSONSearchable(parsed_data)


#Regex Patterns
STRING_RE = r'"((?:\\.|[^"\\])*)"'
NUMBER_RE = r'-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'
BOOLEAN_RE = r'true|false'
NULL_RE = r'null'


def _parser_value(text):
    text = text.strip()
    if text.startswith('{'):
        return _parser_object(text)
    elif text.startswith('['):
        return _parser_array(text)
    elif text.startswith('"'):
        return _parser_string(text)
    elif text.startswith(r'^-?\d', text):
        return _parser_number(text)
    elif text.startswith('true') or text.startswith('false'):
        return _parser_boolean(text)
    elif text.startswith('null'):
        return _parser_null(text)
    else:
        raise ValueError("invalid JSON value")



def _parser_object(text):
    assert text.startswith('{')
    obj = {}
    text = text[1:].strip()
    while not text.startswith('}'):
        key, text.strip()
        if not text.startswith(':'):
            raise ValueError("Expected ':' after key")
        text = text[1:].strip()
        value, text = _parser_value(text)
        obj[key] = value
        text = text.strip()
        if text.startswith(','):
            text = text[1:].strip()
        elif text.startswith('}'):
            break
        else:
            raise ValueError("Expected ',' or '}' in object")
        return obj, text[1:]



def _parser_array(text):
    assert text.startswith('[')
    ar = []
    text = text[1:].strip()
    while not text.startswith(']'):
        value, text = _parser_value(text)
        arr.append(value)
        text = text.strip()
        if text.startswith(','):
            text = text[1:].strip()
        elif text.startswith(']'):
            break
        else:
            raise ValueError("Expected ',' or ']' in array")
        return arr, text[1:] 


def _parser_string(text):

    match = re.match(STRING_RE, text)
    if not match:
        raise ValueError("Invalid JSON string")


    s = match.group(1)
    s = s.replace('\\"', '"').replace('\\\\', '\\')
    rest = text[match.end():]
    return s, rest



def _parser_number(text):
    match = re.match(NUMBER_RE, text)


    if not match:
        raise ValueError("Invalid JSON number")


    num_str = match.group(0)
    if '.' in num_str or 'e' in num_str or 'E' in num_str:

        value = float(num_str)

    else:
        value = int(num_str)

    rest = text[match.end():]
    return value, rest



def _parser_boolean(text):

    if text.startswith('true'):
        return True, text[4:]

    elif text.startswith('false'):
        return False, text[5:]

    else:
        raise ValueError("Invalid JSON number")     
                         
def _parser_null(text):

    if text.startswith('null'):
        return Null, text[4:]

    else:
        raise ValueError("Invalid JSON null")



def _parser_           