from pprint import pprint


first_name = "John"
last_name = "Doe"
height = 168
weight = 70

user = {
    "first_name": first_name,
    "last_name": last_name,
    "display_name": f"{first_name} {last_name}",
    "height": height,
    "weight": weight,
    "bmi": weight / (height / 100) ** 2,
}

if __name__ == "__main__":
    pprint(user)
