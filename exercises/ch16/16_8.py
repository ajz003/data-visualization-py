from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Gambia':
            return 'gm'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Hong Kong SAR':
            return 'hk'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cf'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Gambia':
            return 'gm'
    # If the country wasn't found, return None.
    return None
