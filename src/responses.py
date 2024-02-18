import json
import random
from src.download import download

async def handleResponse(message, author):
    p_message = message.content.lower()

    if '/yt' in p_message:
        for word in p_message.split():
            if 'youtube.com' in word:
                url = word
                output_dir = './output'
                filebin = 'vu7lrn7ceafc' + str(random.randint(1000, 9999))

                initial_response = await message.channel.send(f"<@{str(author)}> Downloading...")

                try:
                    link = await download(url, output_dir, filebin)
                    await initial_response.edit(content=f"<@{str(author)}> {link}")
                except Exception as e:
                    await initial_response.edit(content=f"<@{str(author)}> Download failed: {e}")

                return

    # r6 operator
    elif '/r6' in p_message:
        randomOperator = check_for_random_operator(p_message, author)
        if(randomOperator != 0):
            return randomOperator
        
    # insult
    else:
        responseInsult = check_for_insults(p_message)
        if responseInsult != 0:
            return f"<@{author}> STFU, you're a **{responseInsult}**"
    
    # return "Not a valid command."

def check_for_insults(msg) -> str:
    with open("./src/insults.json", "r") as json_file:
        data = json.load(json_file)
    
    insults = data["insults"]

    for word in msg.split():
        if word in insults:
            print(f"Found insult: {word}, responding.")
            randomResponseInsultWord = random.randint(0,len(insults) - 1)
            return insults[randomResponseInsultWord]
    return 0

def check_for_random_operator(msg, author) -> str:
    with open("./src/operators.json", "r") as json_file:
        data = json.load(json_file)
    
    operators_defense = data["operators_defense"]
    operators_attack = data["operators_attack"]

    if msg == '/r6 attacker':
        rOperator = random.randint(0, len(operators_attack) - 1)
        return f"<@{author}> **{operators_attack[rOperator]}**"
    
    elif msg == '/r6 defender':
        rOperator = random.randint(0, len(operators_attack) - 1)
        return f"<@{author}> **{operators_defense[rOperator]}**"
    
    elif msg == '/r6 attackers':
        rOperator = random.randint(1, len(operators_attack) - 1)
        value = f"**{operators_attack[rOperator]}**"

        for i in range(4):
            rOperator = random.randint(1, len(operators_attack) - 1)
            value += f", **{operators_attack[rOperator]}**"

        return value
    
    elif msg == '/r6 defenders':
        rOperator = random.randint(1, len(operators_attack) - 1)
        value = f"**{operators_defense[rOperator]}**"

        for i in range(4):
            rOperator = random.randint(1, len(operators_attack) - 1)
            value += f", **{operators_defense[rOperator]}**"

        return value
    
    elif msg == '/r6 help':
        return f"<@{author}> use: \n- ``attacker`` to get 1 random attacker\n- ``defender`` to get 1 random defender\n- ``attackers`` to get 5 random attackers\n- ``defenders`` to get 5 random defenders"
    
    else:
        return 0