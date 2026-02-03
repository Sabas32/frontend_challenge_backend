SCHOOL_OPTIONS = [
    "Gayaza High School",
    "St. Mary's College Kisubi",
    "King's College Budo",
    "Namilyango College",
    "Nabisunsa Girls' School",
    "Mt. St. Mary's College Namagunga",
    "Ndejje Senior School",
    "Makerere College School",
    "Mengo Senior School",
    "Kibuli Secondary School",
    "Lubiri Secondary School",
    "Bweranyangi Girls' Secondary School",
    "Ntare School",
    "Gombe Secondary School",
    "St. Henry's College Kitovu",
    "Mt. St. Henry's High School Mukono",
    "Riverside Tech College",
    "Frontier Tech Institute",
    "Metro Design Academy",
    "Makerere University",
    "Kyambogo University",
    "Uganda Christian University",
    "Mbarara University of Science and Technology",
    "Islamic University in Uganda",
    "ISCC Guests",
    "ISCC Panel",
]


def normalize_school_name(value: str):
    if not value:
        return None
    normalized = value.strip()
    if not normalized:
        return None
    by_lower = {item.lower(): item for item in SCHOOL_OPTIONS}
    return by_lower.get(normalized.lower())
