memory = {}

def save(user_id, message):
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append(message)

def get(user_id):
    return memory.get(user_id, [])