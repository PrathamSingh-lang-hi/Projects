import random
import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("🌌 Welcome to Galactic Quest: The Lost Star 🌌")
    slow_print("You are Captain Nova, leading a crew through the Andromeda Expanse.")
    slow_print("Your mission: investigate a mysterious signal from an uncharted planet.")
    return "start"

def choose_path():
    slow_print("\nYou arrive at the edge of the system. Two paths lie ahead:")
    slow_print("1. Land on the planet emitting the signal.")
    slow_print("2. Explore the nearby asteroid belt for resources.")
    choice = input("Choose your path (1 or 2): ")
    return "planet" if choice == "1" else "asteroid"

def planet_scene():
    slow_print("\n🌍 You descend onto the planet. It's eerily quiet.")
    slow_print("Suddenly, an alien guardian appears!")
    return battle_scene()

def asteroid_scene():
    slow_print("\n🪨 You navigate the asteroid belt and discover a derelict ship.")
    slow_print("Inside, you find a healing pod and mysterious coordinates.")
    return "healed"

def battle_scene():
    player_hp = 30
    alien_hp = 25

    slow_print("\n⚔️ Battle Begins! You vs Alien Guardian ⚔️")
    while player_hp > 0 and alien_hp > 0:
        slow_print(f"\nYour HP: {player_hp} | Alien HP: {alien_hp}")
        slow_print("Choose your move:")
        slow_print("1. Attack")
        slow_print("2. Block")
        slow_print("3. Heal")
        move = input("Enter 1, 2, or 3: ")

        alien_move = random.choice(["attack", "block"])

        if move == "1":
            if alien_move == "block":
                slow_print("Alien blocks your attack!")
            else:
                damage = random.randint(5, 10)
                alien_hp -= damage
                slow_print(f"You strike the alien for {damage} damage!")
        elif move == "2":
            if alien_move == "attack":
                damage = random.randint(5, 10) // 2
                player_hp -= damage
                slow_print(f"You block! Alien hits you for {damage} damage.")
            else:
                slow_print("Both of you block. Nothing happens.")
        elif move == "3":
            heal = random.randint(5, 10)
            player_hp += heal
            slow_print(f"You heal for {heal} HP.")

        if alien_hp > 0 and alien_move == "attack" and move != "2":
            damage = random.randint(5, 10)
            player_hp -= damage
            slow_print(f"Alien attacks! You take {damage} damage.")

    if player_hp <= 0:
        slow_print("\n💀 You have been defeated. The galaxy mourns your loss.")
        return "end"
    else:
        slow_print("\n🎉 Victory! The alien guardian vanishes, revealing a hidden temple.")
        return "temple"

def temple_scene():
    slow_print("\n🏛️ Inside the temple, you find the source of the signal: a glowing star fragment.")
    slow_print("It pulses with energy. You must decide:")
    slow_print("1. Take the fragment.")
    slow_print("2. Leave it undisturbed.")
    choice = input("Choose your action (1 or 2): ")
    if choice == "1":
        slow_print("\n🌟 The fragment merges with your ship's core. You gain warp capabilities!")
        slow_print("You chart a new course to explore deeper galaxies.")
    else:
        slow_print("\n🧘 You leave the fragment. Peace returns to the planet.")
        slow_print("Your crew respects your wisdom.")
    return "end"

def healed_scene():
    slow_print("\n❤️ You feel rejuvenated. With new coordinates, you head to the mysterious planet.")
    return planet_scene()

def main():
    scene = intro()
    while scene != "end":
        if scene == "start":
            scene = choose_path()
        elif scene == "planet":
            scene = planet_scene()
        elif scene == "asteroid":
            scene = asteroid_scene()
        elif scene == "healed":
            scene = healed_scene()
        elif scene == "temple":
            scene = temple_scene()

    slow_print("\n🚀 Thanks for playing Galactic Quest! Until next time, Captain Nova.")

if __name__ == "__main__":
    main()
