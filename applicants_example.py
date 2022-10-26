class Applicant:
    IVANA_IVANOVA = 'ivana_ivanova'
    IVAN_IVANOV = 'ivan_ivanov'


APPLICANTS = {
    Applicant.IVANA_IVANOVA: {
        'first_name': 'Ivana',
        'last_name': 'Ivanova',
        'gender': 'F',
        'month_of_birth': '01',
        'day_of_birth': '01',
        'year_of_birth': '1970',
        'birth_city': 'San Francisco',
        'birth_country': 'USA',
        'address_street': 'Baker str, 13',
        'address_city': 'San Francisco',
        'address_region': 'California',
        'address_zip': '95000',
        'address_country': 'USA',
        'current_country': 'USA',
        'phone': '+10000000000',
        'email': 'email@gmail.com',
        'edu_level': '2',
        'marital_level': '1',
        'children_number': '0',
        'spouse': Applicant.IVAN_IVANOV
    },
    Applicant.IVAN_IVANOV: {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'gender': 'M',
        'month_of_birth': '05',
        'day_of_birth': '05',
        'year_of_birth': '1975',
        'birth_city': 'San Francisco',
        'birth_country': 'USA',
        'address_street': 'Baker str, 13',
        'address_city': 'San Francisco',
        'address_region': 'California',
        'address_zip': '95000',
        'address_country': 'USA',
        'current_country': 'USA',
        'phone': '+10000000000',
        'email': 'email@gmail.com',
        'edu_level': '5',  # check the drop box for correct edu level selected during run
        'marital_level': '1',  # check the drop box for correct marital level selected during run
        'children_number': '0',
        'spouse': Applicant.IVANA_IVANOVA
    }
}
