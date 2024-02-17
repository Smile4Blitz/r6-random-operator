import random

operators_attack = [
    "sledge",
    "thatcher",
    "Ash",
    "Thermite",
    "Twitch",
    "Montagne",
    "Glaz",
    "Fuze",
    "Blitz",
    "IQ",
    "Buck",
    "Blackbeard",
    "Capitao",
    "Hibana",
    "Jackal",
    "Ying",
    "Zofia",
    "Dokkaebi",
    "Lion",
    "Finka",
    "Maverick",
    "Nomad",
    "Gridlock",
    "Nokk",
    "Amaru",
    "Kali",
    "Iana",
    "Ace",
    "Zero",
    "Flores",
    "Osa",
    "Sens",
    "Grim",
    "Brava",
    "Ram"
]

operators_defense = [
    "Smoke",
    "Mute",
    "Castle",
    "Pulse",
    "Doc",
    "Rook",
    "Kapkan",
    "Tachanka",
    "Jager",
    "Bandit",
    "Frost",
    "Valkyrie",
    "Caveira",
    "Echo",
    "Mira",
    "Lesion",
    "Ela",
    "Vigil",
    "Maestro",
    "Alibi",
    "Clash",
    "Kaid",
    "Mozzie",
    "Warden",
    "Goyo",
    "Wamai",
    "Oryx",
    "Melusi",
    "Aruni",
    "Thunderbird",
    "Thorn",
    "Azami",
    "Solis",
    "Fenri"
]

def handleResponse(message, author) -> str:
    p_message = message.lower();

    if p_message == 'attacker':
        return f"<@{author}> **{operators_attack[random.randint(0, len(operators_attack) - 1)]}**"

    if p_message == 'defender':
        return f"<@{author}> **{operators_defense[random.randint(0, len(operators_defense) - 1)]}**"
    
    if p_message == 'attackers':
        value = f"<@{author}> **{operators_attack[random.randint(0, len(operators_attack) - 1)]}**"
        for i in range(4):
            value += f", **{operators_attack[random.randint(0, len(operators_attack) - 1)]}**"
        return value
    
    if p_message == 'defenders':
        value = f"<@{author}> **{operators_defense[random.randint(0, len(operators_defense) - 1)]}**"
        for i in range(4):
            value += f", **{operators_defense[random.randint(0, len(operators_defense) - 1)]}**"
        return value
    
    if p_message == 'help':
        return f"<@{author}> \n- 'attacker(s)' for attacker(s)\n- 'defender(s)' for defender(s)"

    return "Not a valid command."
