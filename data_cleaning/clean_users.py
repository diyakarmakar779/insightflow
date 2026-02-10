def clean_user_record(user: dict) -> dict:
    """
    Cleans a single user record and returns a new dictionary.
    """
    cleaned = {}

    name = user.get("name")
    cleaned["name"] = name.strip() if isinstance(name, str) and name.strip() else None

    age = user.get("age")
    cleaned["age"] = int(age) if isinstance(age, str) and age.isdigit() else None

    city = user.get("city")
    cleaned["city"] = city.strip().title() if isinstance(city, str) and city.strip() else None

    return cleaned


def clean_users(users: list) -> list:
    """
    Cleans a list of user records.
    """
    return [clean_user_record(user) for user in users]

if __name__ == "__main__":
    users = [
        {"name": " Diya ", "age": "24", "city": "Bangalore "},
        {"name": "Rahul", "age": None, "city": " mumbai"},
        {"name": "  Ankit", "age": "29", "city": ""},
    ]

    print(clean_users(users))
