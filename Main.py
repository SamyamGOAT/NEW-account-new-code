def save_name(name):
    with open("name.txt", "w") as f:
        f.write(name)

def load_name():
    try:
        with open("name.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

def respond(message):
    msg = message.lower().strip()
    name = load_name()

    if "my name is" in msg:
        user_name = message.split("is")[-1].strip()
        save_name(user_name)
        return f"Nice to meet you, {user_name}!"

    if name:
        return f"Welcome back, {name}! How can I help you?"
    else:
        return "Hello! What's your name?"

while True:
    user = input("You: ")
    print("AI:", respond(user))
