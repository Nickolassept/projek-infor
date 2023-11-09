# Define player positions for FC Barcelona 2023
player_positions = {
    "Lewandowski": "Striker",
    "Joao Felix": "Left wings",
    "Christensen": "Defender",
    "Raphinha": "Right wings",
    "Frenkie de jong": "Midfielder",
    "Joao Cancelo": "Left backs",
    "Gundogan": "Midfielder",
    "Marc-Andre ter Stegen": "Goalkeeper",
    "Ronald Araujo": "Defender",
    "Pedri": "Midfielder",
    "Alejandro Balde": "Right Backs",
}

def get_player_position(player_name):
    player_name = player_name.title()  
    position = player_positions.get(player_name)
    if position:
        return f"Bot: {player_name} plays as a {position} for FC Barcelona."
    else:
        return "Bot: Player not found. Please enter a valid player's name."

print("Bot: Hello! I can provide you with player positions at FC Barcelona in 2023, I can tell you that how many times FC Barcelona has won the Liga Champions. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").strip().lower()  
    if user_input == "exit":
        print("Bot: Goodbye!")
        break
    elif user_input == "champions league":
        print("Bot: Barcelona has won the Liga Champions 5 times (1992,2006,2009,2011,2015).")
    elif user_input == "real madrid / barcelona ?":
        print("Bot: Real Madrid is the best club ever.")
    elif user_input == "xavi":
        print("Bot: Xavi is a Coach at FC Barcelona.")
    elif user_input == "field":
        print("Bot: Camp Nou.")

    else:
        response = get_player_position(user_input)
        print(response)





