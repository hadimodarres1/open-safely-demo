from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),

        age=patients.age_as_of(
        "2019-09-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}}}),

    region=patients.registered_practice_as_of(
        "2020-02-01",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2,
                },
            },
        }),

    admission_method=patients.admitted_to_hospital(
        with_admission_method=['21','22','23','28'],
        returning='admission_method',
        return_expectations={"rate": "universal",
        "category":{
            'ratios':{
                '21':0.25,
                 '22':0.25,
                 '23':0.25,
                 '28':0.25},
                 },
                 }),   

    primary_diagnosis=patients.admitted_to_hospital(
        with_these_primary_diagnoses=['J120'],
        returning='primary_diagnosis'),


)

#"""
#        return_expectations={"rate": "universal",
#        "category":{'ratios':
#                        {'J120':0.5,
#                        'J120':0.5}}}),   
                        
#"""