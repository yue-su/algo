


def generate_email_addresses(names,domain):
    storage = set()
    counter = 1
    for name in names:
        first_name, last_name = name
        email = f"{first_name.lower()}{last_name.lower()[0]}@{domain}"
        if email not in storage:
            storage.add(email)
        else:
            email = f"{first_name.lower()}{last_name.lower()[0]}{counter}@{domain}"
            counter += 1
            storage.add(email)

    return list(storage)

    

print(generate_email_addresses([
  ["Joe", "Smith"],
  ["Yuki", "Yamamoto"],
], "mystartup.com"
))

print(generate_email_addresses([
  ["Yuki", "Yamamoto"],
  ["Yuki", "Yamamoto"],
  ["Yuki", "Yamamoto"],
  ["Yuki", "Yamamoto"],
  ["Yuki", "Yamamoto"],
  ["Yuki", "Yamamoto"],
], "mystartup.com"
))