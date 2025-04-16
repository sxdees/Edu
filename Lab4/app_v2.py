ADULT_AGE = 18

def is_adult(age):
    return age >= ADULT_AGE

def get_user_status(age):
    return "adult" if is_adult(age) else "minor"

def build_user_info(user): # Возвращает словарь с именем, возрастом и статусом пользователя
    return {
        "name": user["name"],
        "age": user["age"],
        "status": get_user_status(user["age"])
    }

def annotate_users(users): # Добавляет к каждому пользователю статус
    return [build_user_info(user) for user in users]

def print_user_statistics(users): # Печатает общее количество пользователей и распределение по статусам
    adults = sum(1 for user in users if is_adult(user["age"]))
    minors = len(users) - adults
    print("Total users:", len(users))
    print("Adults:", adults)
    print("Minors:", minors)

def main():
    users = [
        {"name": "Ivan", "age": 25},
        {"name": "Vladimir", "age": 17},
        {"name": "Petr", "age": 19},
        {"name": "Maxim", "age": 16}
    ]
    annotated = annotate_users(users)
    print_user_statistics(users)
    for user in annotated:
        print(user)

main()
