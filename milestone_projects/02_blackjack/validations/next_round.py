def validate_next_round():
    while True:
        answer = input("Play another round? (Y)es or (N)o? ")
        if answer.lower() in ["yes", "y", "no", 'n']:
            break
    return answer.lower()