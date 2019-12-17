empty_dict = {}
 ud = {}
  fd = {}

   for key, value in entity.items():
        if is_unknown(value):
            empty_dict[key] = None
        elif key in float_props:
            if key == 'gravity':
                value = value.replace('standard', '').strip()
            empty_dict[key] = convert_string_to_float(value)
        elif key in list_props:
            if (key in list_props for key in ('climate', 'terrain')):
                val = value.strip()
            empty_dict[key] = convert_string_to_list(val)
        elif key in int_props:
            empty_dict[key] = convert_string_to_int(value)
        elif key in dict_props:
            if key == 'homeworld':
                ud = get_swapi_resource(ENDPOINT + PEOPLE_URL)
                fd = filter_data(ud, PLANET_KEYS)
            elif key == 'species':
                ud = get_swapi_resource(ENDPOINT + SPECIES_URL[0])
                fd = filter_data(ud, SWAPI_SPECIES_KEYS)
            empty_dict[key] = clean_data(fd)
        #elif key == 'homeworld':
            # ud = get_swapi_resource(value)
            # fd = filter_data(ud, PLANET_KEYS)
            # empty_dict[key] = [clean_data(fd)]
        # elif key == 'species':
        #     ud = get_swapi_resource(value[0])
        #     fd = filter_data(ud, SWAPI_SPECIES_KEYS)
        #     empty_dict[key] = [clean_data(fd)]
        else:
            empty_dict[key] = value
    return empty_dict


      """ elif key in dict_props:
            if key == 'homeworld':
                ud = get_swapi_resource(ENDPOINT + PEOPLE_URL)
                fd = filter_data(ud, PLANET_KEYS)
            elif key == 'species':
                ud = get_swapi_resource(ENDPOINT + SPECIES_URL[0])
                fd = filter_data(ud, SPECIES_KEYS)
            empty_dict[key] = clean_data(fd) """
