import requests, json, random

# base url for pokemon  api
base_url = f'https://pokeapi.co/api/v2/'

# POKEMON
# generates random pokemon ids
id1 = str(random.randrange(1, 1010))
id2 = str(random.randrange(1, 1010))

# gets specific pokemon url
url_1 = f"{base_url}/pokemon/{id1}"
url_2 = f"{base_url}/pokemon/{id2}"

# gets dict_keys(['base_experience', 'forms', 'id', 'moves', 'name', 'species', 'stats', 'types']
# print(requests.get(f"{base_url}/pokemon/101").json().keys())

# gets pokemon data from the API
response1 = requests.get(url_1).json()
response2 = requests.get(url_2).json()

# gets pokemon names
poke1_name = response1["name"].capitalize()
poke2_name = response2["name"].capitalize()

# print(f"Player 1, your Pokemon is {poke1_name}")
# print(f"Player 2, your Pokemon is {poke2_name}")

# STATS
# get pokemon stats # hp, attack, defense, special attack, special defense, speed
poke1_stats = response1["stats"]
poke2_stats = response2["stats"]

# hp
poke1_hp = int(poke1_stats[0]["base_stat"])
poke2_hp = int(poke2_stats[0]["base_stat"])
# print(f"{poke1_name} has {poke1_hp} HP.")
# print(f"{poke2_name} has {poke2_hp} HP.")

# attack
poke1_atk = int(poke1_stats[1]["base_stat"])
poke2_atk = int(poke2_stats[1]["base_stat"])
# print(f"{poke1_name} has {poke1_atk} ATK.")
# print(f"{poke2_name} has {poke2_atk} ATK.")

# speed
poke1_spd = int(poke1_stats[5]["base_stat"])
poke2_spd = int(poke2_stats[5]["base_stat"])
# print(f"{poke1_name} has {poke1_spd} SPD.")
# print(f"{poke2_name} has {poke2_spd} SPD.")

# MOVES
# gets random move index for specific pokemon # dict_keys(['move', 'version_group_details'])
random_move1 = random.randrange(len(response1["moves"]))
random_move2 = random.randrange(len(response2["moves"]))

# Assigns a move to each pokemon
poke1_move = response1["moves"][random_move1]["move"]["name"].capitalize()
poke2_move = response2["moves"][random_move2]["move"]["name"].capitalize()

# GAME
# 1 player or 2 player option
while True:
    mode = input("Which game mode do you want to play?\n- Type 1 for Single player\n- Type 2 for Two player:\n")
    if mode == "1":

        print(f"Player 1, your Pokemon is {poke1_name}")
        print(f"Your opponent's Pokemon is {poke2_name}")
        # BATTLE
        # Battle starts
        print("\nBATTLE\n")

        # Battle continues until one pokemon faints/loses all hp
        while poke1_hp > 0 and poke2_hp > 0:

            # SPD used to determine which pokemon goes first
            # pokemon 2 goes first
            if poke1_spd < poke2_spd:

                # Actions for pokemon 2 & results for action
                print(f"{poke2_name} attacks using {poke2_move}")
                print(f"{poke1_name} takes {poke2_atk} damage")

                # pokemon 1 HP after it has been attacked
                poke1_hp = poke1_hp - poke2_atk

                # Battle continues if HP > 0
                if poke1_hp > 0:

                    # HP remaining for pokemon 1 for players to see
                    print(f"{poke1_name} has {poke1_hp} HP")
                    # Actions for pokemon 1 & results for action
                    print(f"{poke1_name} attacks using {poke1_move}")
                    print(f"{poke2_name} takes {poke1_atk} damage")

                    # pokemon 2 HP after it has been attacked
                    poke2_hp = poke2_hp - poke1_atk

                    # Battle continues if HP > 0
                    if poke2_hp > 0:

                        # Remaining HP for pokemon 2
                        print(f"{poke2_name} has {poke2_hp} HP")

                    # Battle ends if pokemon 1 faints
                    else:
                        print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

                # Battle ends if pokemon 2 faints
                else:
                    print(f"{poke1_name} has fainted. Your opponent and {poke2_name} win.")

            # pokemon 1 goes first
            elif poke1_spd > poke2_spd:

                # Actions for pokemon 1 & results for action
                print(f"{poke1_name} attacks using {poke1_move}")
                print(f"{poke2_name} takes {poke1_atk} damage")

                # pokemon 2 HP after it has been attacked
                poke2_hp = poke2_hp - poke1_atk

                # Battle continues if HP > 0
                if poke2_hp > 0:

                    #  HP remaining for pokemon for players to see
                    print(f"{poke2_name} has {poke2_hp} HP")
                    # Actions for pokemon 2 & results for action
                    print(f"{poke2_name} attacks using {poke2_move}")
                    print(f"{poke1_name} takes {poke2_atk} damage")

                    # pokemon 1 HP after it has been attacked
                    poke1_hp = poke1_hp - poke2_atk

                    # Battle continues if HP > 0
                    if poke1_hp > 0:

                        # Remaining HP for pokemon 1
                        print(f"{poke1_name} has {poke1_hp} HP")

                    # Battle ends if pokemon 2 faints
                    else:
                        print(f"{poke1_name} has fainted. Your opponent and {poke2_name} win.")

                # Battle ends if pokemon 2 faints
                else:
                    print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

            # If speed is tied a "coin toss" decides who goes first
            else:

                # Coin Toss result
                coin_toss_poke_winner = random.choice([poke1_name, poke2_name])

                # Pokemon 1 wins coin toss and goes first
                if coin_toss_poke_winner == poke1_name:
                    print(f"{poke1_name} won the coin toss!")

                    # Actions for pokemon 1 & results for action
                    print(f"{poke1_name} attacks using {poke1_move}")
                    print(f"{poke2_name} takes {poke1_atk} damage")

                    # pokemon 2 HP after it has been attacked
                    poke2_hp = poke2_hp - poke1_atk

                    # Battle continues if HP > 0
                    if poke2_hp > 0:

                        #  HP remaining for pokemon for players to see
                        print(f"{poke2_name} has {poke2_hp} HP")
                        # Actions for pokemon 2 & results for action
                        print(f"{poke2_name} attacks using {poke2_move}")
                        print(f"{poke1_name} takes {poke2_atk} damage")

                        # pokemon 1 HP after it has been attacked
                        poke1_hp = poke1_hp - poke2_atk

                        # Battle continues if HP > 0
                        if poke1_hp > 0:

                            # Remaining HP for pokemon 1
                            print(f"{poke1_name} has {poke1_hp} HP")

                        # Battle ends if pokemon 2 faints
                        else:
                            print(f"{poke1_name} has fainted. Your opponent and {poke2_name} win.")

                    # Battle ends if pokemon 2 faints
                    else:
                        print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

                # Pokemon 2 wins coin toss and goes 1st
                else:
                    print(f"{poke2_name} won the coin toss!")

                    # Actions for pokemon 2 & results for action
                    print(f"{poke2_name} attacks using {poke2_move}")
                    print(f"{poke1_name} takes {poke2_atk} damage")

                    # pokemon 1 HP after it has been attacked
                    poke1_hp = poke1_hp - poke2_atk

                    # Battle continues if HP > 0
                    if poke1_hp > 0:

                        # HP remaining for pokemon 1 for players to see
                        print(f"{poke1_name} has {poke1_hp} HP")
                        # Actions for pokemon 1 & results for action
                        print(f"{poke1_name} attacks using {poke1_move}")
                        print(f"{poke2_name} takes {poke1_atk} damage")

                        # pokemon 2 HP after it has been attacked
                        poke2_hp = poke2_hp - poke1_atk

                        # Battle continues if HP > 0
                        if poke2_hp > 0:

                            # Remaining HP for pokemon 2
                            print(f"{poke2_name} has {poke2_hp} HP")

                        # Battle ends if pokemon 1 faints
                        else:
                            print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

                    # Battle ends if pokemon 2 faints
                    else:
                        print(f"{poke1_name} has fainted. Your opponent and {poke2_name} win.")
        break
    elif mode == "2":

        # Tells players what their pokemon is
        print(f"Player 1, your Pokemon is {poke1_name}")
        print(f"Player 2, your Pokemon is {poke2_name}")

        # BATTLE
        # Battle starts
        print("\nBATTLE\n")

        # Battle continues until one pokemon faints/loses all hp
        while poke1_hp > 0 and poke2_hp > 0:

            # SPD used to determine which pokemon goes first
            # pokemon 2 goes first
            if poke1_spd < poke2_spd:

                # Actions for pokemon 2 & results for action
                print(f"{poke2_name} attacks using {poke2_move}")
                print(f"{poke1_name} takes {poke2_atk} damage")

                # pokemon 1 HP after it has been attacked
                poke1_hp = poke1_hp - poke2_atk

                # Battle continues if HP > 0
                if poke1_hp > 0:

                    # HP remaining for pokemon 1 for players to see
                    print(f"{poke1_name} has {poke1_hp} HP")
                    # Actions for pokemon 1 & results for action
                    print(f"{poke1_name} attacks using {poke1_move}")
                    print(f"{poke2_name} takes {poke1_atk} damage")

                    # pokemon 2 HP after it has been attacked
                    poke2_hp = poke2_hp - poke1_atk

                    # Battle continues if HP > 0
                    if poke2_hp > 0:

                        # Remaining HP for pokemon 2
                        print(f"{poke2_name} has {poke2_hp} HP")

                    # Battle ends if pokemon 1 faints
                    else:
                        print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

                # Battle ends if pokemon 2 faints
                else:
                    print(f"{poke1_name} has fainted. Player 2 and {poke2_name} win.")

            # pokemon 1 goes first
            elif poke1_spd > poke2_spd:

                # Actions for pokemon 1 & results for action
                print(f"{poke1_name} attacks using {poke1_move}")
                print(f"{poke2_name} takes {poke1_atk} damage")

                # pokemon 2 HP after it has been attacked
                poke2_hp = poke2_hp - poke1_atk

                # Battle continues if HP > 0
                if poke2_hp > 0:

                    #  HP remaining for pokemon for players to see
                    print(f"{poke2_name} has {poke2_hp} HP")
                    # Actions for pokemon 2 & results for action
                    print(f"{poke2_name} attacks using {poke2_move}")
                    print(f"{poke1_name} takes {poke2_atk} damage")

                    # pokemon 1 HP after it has been attacked
                    poke1_hp = poke1_hp - poke2_atk

                    # Battle continues if HP > 0
                    if poke1_hp > 0:

                        # Remaining HP for pokemon 1
                        print(f"{poke1_name} has {poke1_hp} HP")

                    # Battle ends if pokemon 2 faints
                    else:
                        print(f"{poke1_name} has fainted. Player 2 and {poke2_name} win.")

                # Battle ends if pokemon 2 faints
                else:
                    print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

            # If speed is tied a "coin toss" decides who goes first
            else:

                # Coin Toss result
                coin_toss_poke_winner = random.choice([poke1_name, poke2_name])

                # Pokemon 1 wins coin toss and goes first
                if coin_toss_poke_winner == poke1_name:
                    print(f"{poke1_name} won the coin toss!")

                    # Actions for pokemon 1 & results for action
                    print(f"{poke1_name} attacks using {poke1_move}")
                    print(f"{poke2_name} takes {poke1_atk} damage")

                    # pokemon 2 HP after it has been attacked
                    poke2_hp = poke2_hp - poke1_atk

                    # Battle continues if HP > 0
                    if poke2_hp > 0:

                        #  HP remaining for pokemon for players to see
                        print(f"{poke2_name} has {poke2_hp} HP")
                        # Actions for pokemon 2 & results for action
                        print(f"{poke2_name} attacks using {poke2_move}")
                        print(f"{poke1_name} takes {poke2_atk} damage")

                        # pokemon 1 HP after it has been attacked
                        poke1_hp = poke1_hp - poke2_atk

                        # Battle continues if HP > 0
                        if poke1_hp > 0:

                            # Remaining HP for pokemon 1
                            print(f"{poke1_name} has {poke1_hp} HP")

                        # Battle ends if pokemon 2 faints
                        else:
                            print(f"{poke1_name} has fainted. Player 2 and {poke2_name} win.")

                    # Battle ends if pokemon 2 faints
                    else:
                        print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

                # Pokemon 2 wins coin toss and goes 1st
                else:
                    print(f"{poke2_name} won the coin toss!")

                    # Actions for pokemon 2 & results for action
                    print(f"{poke2_name} attacks using {poke2_move}")
                    print(f"{poke1_name} takes {poke2_atk} damage")

                    # pokemon 1 HP after it has been attacked
                    poke1_hp = poke1_hp - poke2_atk

                    # Battle continues if HP > 0
                    if poke1_hp > 0:

                        # HP remaining for pokemon 1 for players to see
                        print(f"{poke1_name} has {poke1_hp} HP")
                        # Actions for pokemon 1 & results for action
                        print(f"{poke1_name} attacks using {poke1_move}")
                        print(f"{poke2_name} takes {poke1_atk} damage")

                        # pokemon 2 HP after it has been attacked
                        poke2_hp = poke2_hp - poke1_atk

                        # Battle continues if HP > 0
                        if poke2_hp > 0:

                            # Remaining HP for pokemon 2
                            print(f"{poke2_name} has {poke2_hp} HP")

                        # Battle ends if pokemon 1 faints
                        else:
                            print(f"{poke2_name} has fainted. Player 1 and {poke1_name} win.")

                    # Battle ends if pokemon 2 faints
                    else:
                        print(f"{poke1_name} has fainted. Player 2 and {poke2_name} win.")
        break
    else:
        print("Please enter a valid game mode (1 or 2)")
        continue
