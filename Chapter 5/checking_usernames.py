current_users = ["bob", "alice", "eve", "admin", "Shodan"]
new_users = ["bob", "joe", "ada", "cathrine", "shodan"]
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() not in current_users_lower:
        print(f"The username {user} is available!")
    else:
        print(f"The username {user} is not available :(")