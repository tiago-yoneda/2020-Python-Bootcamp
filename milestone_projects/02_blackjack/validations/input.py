def validate_input():
    while True:
        action = input("What will you do? (H)it or (P)ass? ")
        if action.upper() in ["H", "P"]:
            break
    return action.upper()