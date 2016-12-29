"""Idiomatic ways of using exceptions."""

# Scenario 1: using exceptions to write code EAFP style rathe than LBYL
# LBYL: Look Before You Leap
# EAFP: Easie to ask for Forgiveness than Permission
# harmful
def get_log_level(config_dict):
    if 'ENABLE_LOGGING' in config_dict:
        if config_dict['ENABLE_LOGGING'] != True:
            return None
        elif not 'DEFAULT_LOG_LEVEL' in config_dict:
            return None
        else:
            return config_dict['DEFAULT_LOG_LEVEL']
    else:
        return None

# Idiomatic
def get_log_level(config_dict):
    try:
        if config_dict['ENABLE_LOGGING']:
            return config_dict['DEFAULT_LOG_LEVEL']
    except KeyError:
        # if either value wasn't present a KeyError will be raised
        return None

# Scenario 2: using bare exception clauses (not catching specific exceptions)
# harmful
import requests
def get_json_response(url):
    try:
        response = request.get(url)
        return response.json()
    except:
        print('Oops! Something went wrong')
        return None

# Idiomatic
import requests
# Ignoring the exception
def get_json_response(url):
    return requests.get(url).json()

# Taking account of the exception
def alternate_get_json_response():
    try:
        return requests.get(url).json()
    except:
        raise
