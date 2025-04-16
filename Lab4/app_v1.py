def process_users(users):
    result = []
    for user in users:
        name = user["name"]
        age = user["age"]
        if age >= 18:
            status = "adult"
        else:
            status = "minor"
        info = {
            "name": name,
            "age": age,
            "status": status
        }
        result.append(info)
    return result

def print_user_statistics(users):
    adults = 0
    minors = 0
    for user in users:
        if user["age"] >= 18:
            adults += 1
        else:
            minors += 1
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
    processed = process_users(users)
    print_user_statistics(users)
    for u in processed:
        print(u)

main()
