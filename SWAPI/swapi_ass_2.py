import json
import requests

ENDPOINT = 'https://swapi.co/api'
SPECIES_URL = '/species/'
PEOPLE_URL = '/people/'

PERSON_KEYS = (
    'url', 'name', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
    'gender', 'homeworld', 'species',
)

PLANET_KEYS = (
    'url', 'name', 'rotation_period', 'orbital_period', 'diameter', 'climate',
    'gravity', 'terrain', 'surface_water', 'population',
)

HOTH_KEYS = (
    'url', 'name', 'system_position', 'natural_satelites', 'rotation_period',
    'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water',
    'population', 'indigenous_life_forms',
)

SPECIES_KEYS = (
    'url', 'name', 'classification', 'average_height', 'skin_colors', 'hair_colors',
    'eye_colors', 'average_lifespan', 'language',
)

STARSHIP_KEYS = (
    'url', 'starship_class', 'name', 'model', 'manufacturer', 'length', 'width',
    'max_atmosphering_speed', 'hyperdrive_rating', 'crew', 'passengers', 'cargo_capacity',
    'consumables', 'armament',
)

VEHICLE_KEYS = (
    'url', 'vehicle_class', 'name', 'model', 'manufacturer', 'length', 'max_atmosphering_speed',
    'crew', 'passengers', 'cargo_capacity', 'consumables', 'armament',
)


def assign_crew(starship, crew):
    """ The function assigns crew members to a starship.

    Parameters:
        starship (dict): used to containing crew key-pairs.
        crew (dict): defines role as key and name of member as value.

    Returns:
        dict: updated starship dict with crew members added.
    """
    for key, value in crew.items():
        if key not in starship.keys():
            starship[key] = value
    return starship


def clean_data(entity):
    """Converts dictionary string values to more appropriate types such as float, int, list, or None.

    Parameters:
        entity (dict): dictionary with values to be cleaned.


    Returns:
        Dict: a new entity with 'cleaned' values to the caller.
    """
    float_props = (
        'gravity', 'length', 'width', 'hyperdrive_rating',
    )
    int_props = (
        'rotation_period', 'orbital_period', 'diameter', 'surface_water', 'population', 'height', 'mass',
        'average_height', 'average_lifespan', 'max_atmosphering_speed', 'MGLT', 'crew', 'passengers', 'cargo_capacity',
    )
    list_props = (
        'hair_color', 'skin_color', 'climate', 'terrain', 'skin_colors', 'hair_colors', 'eye_colors',

    )
    dict_props = (
        'homeworld', 'species',
    )


    cleaned = {}

    for key, value in entity.items():
        if type(value) == str and is_unknown(value):
            cleaned[key] = None
        elif key in float_props:
            if key == 'gravity':
                value = value.replace('standard', ' ').strip()
            cleaned[key] = convert_string_to_float(value)
        elif key in int_props:
            cleaned[key] = convert_string_to_int(value)
        elif key in list_props:
            cleaned[key] = convert_string_to_list(value, ', ')
        elif key in dict_props:
            if key == 'homeworld':
                swapi_data = get_swapi_resource(value)
                filtered_data = filter_data(swapi_data, PLANET_KEYS)
                cleaned[key] = clean_data(filtered_data)
            if key == 'species':
                swapi_data = get_swapi_resource(value[0])
                filtered_data = filter_data(swapi_data, SPECIES_KEYS)
                cleaned[key] = [clean_data(filtered_data)]
        else:
            cleaned[key] = value

    return cleaned




def combine_data(default_data, override_data):
    """Creates a shallow copy of the default dictionary then updates the copy with
    specified key-value pairs that override values on matching keys. If a deep copy is
    required use the copy module copy.deepcopy() method.

    Parameters:
        default_data (dict): key-value pairs provide a collection of default values.
        override_data (dict): key-value pairs that are intended to override default values.

    Returns:
        dict: dictionary with updated key-value pairs.
    """

    combined_data = default_data.copy()  # shallow
    combined_data.update(override_data)  # in place

    return combined_data


def convert_string_to_float(value):
    """ Attempts to convert a string to a floating point value.
    If unsuccessful, returns the value unchanged.

    Parameters:
        value (str):

    Returns:
        None
    """
    try:
        return float(value)
    except ValueError:
        return value


def convert_string_to_int(value):
    """ Attempts to convert a string to an integers.
    If unsuccessful, returns the value unchanged.

    Parameters:
        value (str):

    Returns:
        None
    """
    try:
       return int(value)
    except ValueError:
        return value


def convert_string_to_list(value, delimiter=','):
    """Attempts to convert a string to a list.  If unsuccessful returns
    the value unchanged.

    Parameters:
        value (str): string to be converted.
        delimiter (str): delimiter used for spliting the string

    Returns:
        list: if string successfully converted.
        str: if string could not be converted.
    """
    try:
        splitted = value.split(delimiter)
        for element in splited:
            element.strip()
        return list(splitted)
    except ValueError:
        return value


def filter_data(data, filter_keys):
    """Returns a new dictionary based containing a filtered subset of key-value pairs
    sourced from a dictionary provided by the caller.

    Parameters:
        data (dict): source entity.
        filter_keys (tuple): sequence of keys used to select a subset of key-value pairs.

    Returns:
        dict: a new entity containing a subset of the source entity's key-value pairs.
    """
    # return {key: data[key] for key in filter_keys if key in data.keys()}

    filtered_dict = {}
    for key in filter_keys:
        if key in data.keys():
            filtered_dict[key] = data[key]
    return filtered_dict


def get_swapi_resource(url, params=None):
    """Issues an HTTP GET request to return a representation of a resource. If no category is
    provided, the root resource will be returned. An optional query string of key:value pairs
    may be provided as search terms (e.g., {'search': 'yoda'}). If a match is achieved the
    JSON object that is returned will include a list property named 'results' that contains the
    resource(s) matched by the search query.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.

    Returns:
        dict: decoded JSON document expressed as dictionary.
    """

    response = requests.get(url, params=params).json()
    return response


def is_unknown(value):
    """ This function is for telling if the given string equals to 'unknown' or 'n/a'.

    Parameters:
        value (str): given string for testing.

    Returns: 
        bool: returns True if string equals to 'unknown' or 'n/a'.
    """
    if value.lower().strip() == 'unknown':
        return True
    elif value.lower().strip() == 'n/a':
        return True
    else:
        return False


def read_json(filepath):
    """Given a valid filepath, reads a JSON document and returns a dictionary.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: decoded JSON document expressed as a dictionary.
    """
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data


def write_json(filepath, data):
    """Given a valid filepath, write data to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point. This program will interact with local file assets and the Star Wars
    API to create two data files required by Rebel Alliance Intelligence.

    - A JSON file comprising a list of likely uninhabited planets where a new rebel base could be
      situated if Imperial forces discover the location of Echo Base.

    - A JSON file of Echo Base information including an evacuation plan of base personnel
      along with passenger assignments for Princess Leia, the communications droid C-3PO aboard
      the transport Bright Hope escorted by two X-wing starfighters piloted by Luke Skywalker
      (with astromech droid R2-D2) and Wedge Antilles (with astromech droid R5-D4).

    Parameters:
        None

    Returns:
        None
    """

    #swapi_planets_uninhabited json file
    uninhabited = []
    file_in = 'swapi_planets-v1p0.json'
    file_out = 'swapi_planets_uninhabited-v1p1.json'

    planet_dicts = read_json(file_in)
    for d in planet_dicts:
        if is_unknown(d['population']):
            filtered = filter_data(d, PLANET_KEYS)
            cleaned = clean_data(filtered)
            uninhabited.append(cleaned)

    write_json(file_out, uninhabited)

    #Enrich echo base data
    f_in = 'swapi_echo_base-v1p0.json'
    f_out = 'swapi_echo_base-v1p1.json'

    #hoth data
    echo_base = read_json(f_in)
    swapi_planets_url = f"{ENDPOINT}/planets/"

    swapi_hoth = get_swapi_resource(
        swapi_planets_url, {'search': 'Hoth'})['results'][0]
    echo_base_hoth = echo_base['location']['planet']
    hoth = combine_data(echo_base_hoth, swapi_hoth)
    hoth = filter_data(hoth, HOTH_KEYS)
    hoth = clean_data(hoth)
    echo_base['location']['planet'] = hoth

    #commander data
    echo_base_commander = echo_base['garrison']['commander']
    echo_base_commander = clean_data(echo_base_commander)
    echo_base['garrison']['commander'] = echo_base_commander

    #enrich dash rendar
    echo_base_dash = echo_base['visiting_starships']['freighters'][1]['pilot']
    echo_base_dash = clean_data(echo_base_dash)
    echo_base['visiting_starships']['freighters'][1]['pilot'] = echo_base_dash

    #enrich snowspeeder data
    swapi_vehicles_url = f"{ENDPOINT}/vehicles/"
    swapi_snowspeeder = get_swapi_resource(
        swapi_vehicles_url, {'search': 'snowspeeder'})['results'][0]

    echo_base_snowspeeder = echo_base['vehicle_assets']['snowspeeders'][0]['type']

    snowspeeder = combine_data(echo_base_snowspeeder, swapi_snowspeeder)
    snowspeeder = filter_data(snowspeeder, VEHICLE_KEYS)
    snowspeeder = clean_data(snowspeeder)
    echo_base['vehicle_assets']['snowspeeders'][0]['type'] = snowspeeder

    #enrich t-65 x-wing
    swapi_starship_url = f"{ENDPOINT}/starships/"
    swapi_xwing = get_swapi_resource(
        swapi_starship_url, {'search': 'T-65 X-wing'})['results'][0]

    echo_base_xwing = echo_base['starship_assets']['starfighters'][0]['type']

    xwing = combine_data(echo_base_xwing, swapi_xwing)
    xwing = filter_data(xwing, STARSHIP_KEYS)
    xwing = clean_data(xwing)
    echo_base['starship_assets']['starfighters'][0]['type'] = xwing

    #enrich GR-75 medium transport
    swapi_gr75 = get_swapi_resource(
        swapi_starship_url, {'search': 'GR-75 medium transport'})['results'][0]

    echo_base_gr75 = echo_base['starship_assets']['transports'][0]['type']

    gr_75 = combine_data(echo_base_gr75, swapi_gr75)
    gr_75 = filter_data(gr_75, STARSHIP_KEYS)
    gr_75 = clean_data(gr_75)
    echo_base['starship_assets']['transports'][0]['type'] = gr_75

    #enrich Millennium Falcon
    swapi_falcon = get_swapi_resource(
        swapi_starship_url, {'search': 'Millennium Falcon'})['results'][0]
    echo_base_falcon = echo_base['visiting_starships']['freighters'][0]

    m_falcon = combine_data(echo_base_falcon, swapi_falcon)
    m_falcon = filter_data(m_falcon, STARSHIP_KEYS)
    m_falcon = clean_data(m_falcon)
    echo_base['visiting_starships']['freighters'][0] = m_falcon

    #Assign crew to the Millennium Falcon

    #retrieve han
    swapi_people_url = f"{ENDPOINT}/people/"
    han = get_swapi_resource(swapi_people_url, {'search': 'han solo'})[
        'results'][0]
    han = filter_data(han, PEOPLE_KEYS)
    han = clean_data(han)

    #retrieve Chewbacca
    chewie = get_swapi_resource(swapi_people_url, {'search': 'Chewbacca'})[
        'results'][0]
    chewie = filter_data(chewie, PEOPLE_KEYS)
    chewie = clean_data(chewie)

    #assign han and chewbacca
    m_falcon = assign_crew(m_falcon, {'pilot': han, 'copilot': chewie})
    echo_base['visiting_starships']['freighters'][0] = m_falcon

    #Update evacuation plan
    evac_plan = echo_base['evacuation_plan']
    evac_plan['max_base_personnel'] = 0
    for v_number in echo_base['garrison']['personnel'].values():
        evac_plan['max_base_personnel'] += v_number

    trans_num = echo_base['starship_assets']['transports'][0]['num_available']
    evac_plan['max_available_transports'] = 0
    evac_plan['max_available_transports'] += trans_num

    pass_num = 90
    total_trans_pass = trans_num * pass_num
    evac_plan['max_passenger_overload_capacity'] = 0
    evac_plan['max_passenger_overload_capacity'] = total_trans_pass * \
        evac_plan['passenger_overload_multiplier']

    #bright hope assignment
    evac_transport = echo_base['starship_assets']['transports'][0]['type'].copy(
    )
    evac_transport['name'] = 'Bright Hope'
    evac_transport['passenger_manifest'] = []

    #retrieve leia organa
    leia_o = get_swapi_resource(swapi_people_url, {'search': 'Leia Organa'})[
        'results'][0]
    leia_o = filter_data(leia_o, PEOPLE_KEYS)
    leia_o = clean_data(leia_o)

    #retrieve C-3PO
    c_3po = get_swapi_resource(
        swapi_people_url, {'search': 'C-3PO'})['results'][0]
    c_3po = filter_data(c_3po, PEOPLE_KEYS)
    c_3po = clean_data(c_3po)

    #assign the two passengers
    evac_transport['passenger_manifest'].append(leia_o)
    evac_transport['passenger_manifest'].append(c_3po)

    #assign escorts
    evac_transport['escorts'] = []
    xwing_copy = echo_base['starship_assets']['starfighters'][0]['type']
    luke_x_wing = xwing_copy.copy()
    wedge_x_wing = xwing_copy.copy()

    luke = get_swapi_resource(swapi_people_url, {'search': 'Luke Skywalker'})[
        'results'][0]
    luke = filter_data(luke, PEOPLE_KEYS)
    luke = clean_data(luke)
    r2_d2 = get_swapi_resource(
        swapi_people_url, {'search': 'R2-D2'})['results'][0]
    r2_d2 = filter_data(r2_d2, PEOPLE_KEYS)
    r2_d2 = clean_data(r2_d2)
    luke_x_wing = assign_crew(
        luke_x_wing, {'pilot': luke, 'astromech_droid': r2_d2})
    evac_transport['escorts'].append(luke_x_wing)

    wedge = get_swapi_resource(swapi_people_url, {'search': 'Wedge Antilles'})[
        'results'][0]
    wedge = filter_data(wedge, PEOPLE_KEYS)
    wedge = clean_data(wedge)
    r5_d4 = get_swapi_resource(
        swapi_people_url, {'search': 'R5-D4'})['results'][0]
    r5_d4 = filter_data(r5_d4, PEOPLE_KEYS)
    r5_d4 = clean_data(r5_d4)
    wedge_x_wing = assign_crew(
        wedge_x_wing, {'pilot': wedge, 'astromech_droid': r5_d4})
    evac_transport['escorts'].append(wedge_x_wing)

    evac_plan['transport_assignments'].append(evac_transport)
    echo_base['evacuation_plan'] = evac_plan

    #write into output file
    write_json(f_out, echo_base)


if __name__ == '__main__':
    main()
