# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.
profile = {
    "name": "Steve The Cat",
    "age": "6 months old",
    "birth place": "'Merica",
    "favorite language": "Python"
}


def profile_info(in_dict):
    for key, value in in_dict.items():
        print("My {} is {}".format(key, value))


profile_info(profile)
