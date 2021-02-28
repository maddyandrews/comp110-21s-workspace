"""CYOA: Cow Adventures!

Requirement #4 is included with the outdoor and home adventure branches. 
Both add points by changing the global points variable directly.

Requirement #5 is included with the city path. The points are passed as a parameter to the city_1 function.
The points variable is passed through the selected city path, then returned to the main function to add points.

Requirement #9: Game Loop
Upon reaching the end of any of the 3 main adventure paths, the 'goodnight' function is called, which ends the day
and allows for the player to continue to another day of adventures. The player can end their experience here, or they
can stop playing by selecting option 4 in the main function. The 'play' while loop inside the main function allows 
the player to choose the same branch as before, or an entirely new one.

"""

__author__ = "730393750"


points: int = 0
player: str = " "
cow: str = " "

COW_FACE: str = "\U0001F42E"
COW: str = "\U0001F404"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()

    global cow
    cow = str(input("Aw, it looks like this one likes you! What will you call them?: "))

    print(f"\nNow you and {cow} can spend the day together!")
    
    global points
    points = 0

    play: str = "Continue."
    while play == "Continue.":
        print(f"\n{cow} has a few ideas for how you can spend the day together:"
                "\n1. Spend time outdoors."
                    "\n2. Take a trip to the city."
                    "\n3. Relax at home."
                    "\n4. I'm done playing for now.")
        
        choice: int = int(input(f"So, what would you like to do today with {cow}?: "))
        if choice == 1:
            outdoor_1()
        else:
            if choice == 2:
                points += city_1(points)
                goodnight()
            else:
                if choice == 3:
                    home_1()
                else:
                    play = "Stop."

    print(f"\nThanks for playing today, {player}. {cow} will miss you :( Until next time!"
            f"\nAdventure points earned: {points} {COW_FACE}")
    quit()
    return None


def greet() -> None:
    """Greeting message when beginning adventure."""
    SUN: str = "\U0001F324"

    global player
    player = str(input(f"Welcome to Sunshine Meadows {SUN}, where all the happiest cows come to graze. "
            "Before you go off exploring, what is your name?: "))

    welcome: str = str(f"\nNice to meet you, {player}! Now, let's see if we can find a friend to play with today.\n"
                            f"*A baby cow comes up to you and says, \"moo\" {COW_FACE}.*")

    print(welcome)
    return None


def outdoor_1() -> None:
    """First outdoor activity. Adds to points directly based on choice made."""
    print(f"\nWow, a day outdoors - what an adventure it'll be!\n"
            f"\nFirst, you and {cow} decide to catch some bugs!")

    LADYBUG: str = "\U0001F41E"
    BUTTERFLY: str = "\U0001F98B"
    BEE: str = "\U0001F41D"

    search: int = int(input(f"\nWhere should {cow} look?:"
                            "\n1. Under a rock."
                                "\n2. Near the trees."
                                "\n3. By the flowers."
                                "\nSearch: "))

    global points
    if search == 1:
        print(f"\nYou lift up the rock and find a cute little ladybug. Nice job, {player}!{LADYBUG}")
        points += 10
    else:
        if search == 2:
            print(f"\nHiding on the trunk of a tree, {cow} spots a beautiful butterfly!{BUTTERFLY}")
            points += 15
        else:
            print(f"\nYou find a bumblebee! But {cow} gets stung, ouch...{BEE}")
            points += 5
    return outdoor_2()


def outdoor_2() -> None:
    """Second outdoor activity. Adds points based on bait chosen and randomized fishing function."""
    print(f"\nNext, you and {cow} head to the pond. You decide to go fishing!")
    
    bait: int = int(input("\nWhat kind of bait do you use?:"
            "\n1. Worms from a puddle of mud nearby."
            "\n2. A pb&j sandwich you have leftover from lunch."
            "\n3. I don't need bait!"
            "\nBait: "))
    
    global points
    points += fishing(bait)
    
    i: int = 0
    fish: str = str(input("\nTry again? (yes/no): "))
    while fish == "yes" and i < 3:
        if i < 2:
            points += fishing(bait)
            i += 1
            fish = str(input("\nTry again? (yes/no): "))
        else:
            if i == 2:
                i += 1
                points += fishing(bait)
    print(f"{cow} thinks that's enough fishing for today. Onto the next activity!")
    return outdoor_3()


def outdoor_3() -> None:
    """Last outdoor activity. Adds points based on location chosen."""
    print(f"\nYou and {cow} decide to go on one more adventure. But {cow} can't decide where to go!")
    
    SHELL: str = "\U0001F41A"
    BERRY: str = "\U0001F353"
    MOUNTAIN: str = "\U0001F3D4"

    global points
    location: int = int(input(f"\nWhere should you and {cow} go?:"
                                "\n1. The beach."
                                    "\n2. The forest."
                                    "\n3. The mountains."
                                    "\nLocation: "))

    if location == 1:
        print(f"You and {cow} have a great time collecting shells on the beach!\n{COW_FACE}{SHELL}")
        points += 10
    else:
        if location == 2:
            print(f"{cow} loves the forest, and you find some strawberries to snack on. Yum!\n{COW_FACE}{BERRY}")
            points += 15
        else:
            print(f"You and {cow} climb all the way to the top. The view is breathtaking!\n{COW_FACE}{MOUNTAIN}")
            points += 5
    return goodnight()


def fishing(x: int) -> int:
    """Fishing at the pond; rolls a random integer to assign new points earned on adventure."""
    from random import randint
    y: int = randint(1, 5)

    BOAT: str = "\U000026F5"
    FISHING_POLE: str = "\U0001F3A3"
    FISH: str = "\U0001F420"
    WHALE: str = "\U0001F433"

    input("Press enter to cast your line: ")
    print(f"\n{BOAT}{FISHING_POLE}\n")

    if x == 1:
        if y == 5:
            print(f"Wow, {player}! You caught a big fish!! {WHALE}")
            return 5
        else:
            if y > 2:
                print(f"Nice catch, {player}, you caught a guppy! {FISH}")
                return 3
            else:
                print(f"You caught... a boot. Better luck next time, {player}.")
                return 1
    else:
        if x == 2:
            x += 5
            if y > 2:
                print(f"Wow, {player}! You caught a big fish!! {WHALE}")
                return 5
            else:
                print(f"You caught... a boot. Better luck next time, {player}.")
                return 1
        else:
            if x == 3:
                x += 1
                print(f"You caught... a boot. Better luck next time, {player}.")
                return 1
    return int()


def city_1(x: int) -> int:
    """First city adventure path. Directs player to selected city and returns additional adventure points."""
    print("\nA day in the city - how fun!")

    destination: int = int(input(f"But what city should you and {cow} visit today?:"
        "\n1. Paris"
        "\n2. New York City"
        "\n3. Let's go to the moon instead!"
        "\nDestination: "))

    PLANE: str = "\U00002708"
    CLOUD: str = "\U00002601"

    print(f"\n{CLOUD}{PLANE}{CLOUD}")

    if destination == 1:
        x += 10
        return paris_1(x)
    else:
        if destination == 2:
            x += 10
            return nyc_1(x)
        else:
            if destination == 3:
                x += 15
                return moon_1(x)
    return int()


def paris_1(x: int) -> int:
    """Starts adventure in Paris. First activity at bakery, adds points based on order."""
    print(f"\nBonjour, {player} and {cow}, and welcome to Paris!")
    
    CAKE: str = "\U0001F370"
    CROISSANT: str = "\U0001F950"
    BAGUETTE: str = "\U0001F956"
    
    dessert: int = int(input(f"\nFirst, let's head to the bakery! What should you and {cow} order?:"
                                "\n1. Cake."
                                    "\n2. A croissant"
                                    "\n3. A baguette"
                                    "\nYour order: "))
    
    if dessert == 1:
        print(f"\nGreat choice, {player}! Cake is {cow}'s favorite!\n{COW_FACE}{CAKE}")
        x += 5
    else:
        if dessert == 2:
            print(f"\nA croissant - nice choice! {cow} thinks it's pretty good.\n{COW_FACE}{CROISSANT}")
            x += 3
        else:
            if dessert == 3:
                print(f"\nHmm, {cow} isn't a fan of the baguette. More for you then, {player}!\n{COW_FACE}{BAGUETTE}")
                x += 1
    return paris_2(x)


def paris_2(x: int) -> int:
    """Second activity in Paris. Random amount rolled to spend while shopping. Adds item's points * # items bought."""
    print(f"\nNext, you and {cow} decide to go shopping.")

    from random import randint
    budget: int = randint(10, 50)
    quantity: int = round(budget / 10)
    print(f"Looks like you have ${budget} to spend. You have enough to buy {quantity} of any item here!")

    shopping: int = int(input("\nWhat should you buy for Cowy?"
                                "\n1. Shoes!"
                                    "\n2. A nice new bag."
                                    "\n3. A fancy hat."
                                    "\nItem: "))

    SHOE: str = "\U0001F460"
    BAG: str = "\U0001F45B"
    HAT: str = "\U0001F452"

    if shopping == 1:
        print(f"\n{cow} loves the color, but {cow} is a cow, and it's a bit hard to walk...\n{COW_FACE}{SHOE}")
        x += quantity
    else:
        if shopping == 2:
            print(f"\n{cow} feels so chic, and now {cow} can carry extra snacks!\n{COW_FACE}{BAG}")
            x += (3 * quantity)
        else:
            if shopping == 3:
                print(f"\n{cow} feels very fancy in their hat. A perfect fit!\n{COW_FACE}{HAT}")
                x += (5 * quantity)
    return paris_3(x)


def paris_3(x: int) -> int:
    """Final activity in Paris. Adds points based on selection."""
    landmark: int = int(input(f"\nBefore you and {cow} fly home, you have time to go to one last destination:"
                                "\n1. The Louvre."
                                    "\n2. The Arc de Triomphe."
                                    "\n3. The Eiffel Tower"
                                    "\nWhich landmark should you visit?: "))

    if landmark == 1:
        print(f"\nSo many beautiful pieces of artwork! {cow} feels inspired to become an artist one day.")
        x += 10
    else:
        if landmark == 2:
            print(f"\n{cow} feels so immersed in the city as they walk down the Champs-Elysees!")
            x += 5
        else:
            if landmark == 3:
                print(f"\nThe view from the Eiffel Tower is incredible!"
                    f"You're so high up, {cow} mistakes the people below for ants.")
                x += 5

    print("\nWhat a great way to end such a fun day in Paris!")
    return x


def nyc_1(x: int) -> int:
    """Starts adventure in NYC. First activity at Statue of Liberty, adds points based on choice made."""
    APPLE: str = "\U0001F34E"
    STATUE_OF_LIBERTY: str = "\U0001F5FD"
    HEART: str = "\U00002764"
    print(f"\nWelcome to NYC, {player} and {cow}, or as some like to call it, the Big Apple {APPLE}")

    souvenir: int = int(input(f"\nYour first stop is the Statue of Liberty!{STATUE_OF_LIBERTY} "
                                "What kind of souvenir should Cowy buy?:"
                                    "\n1. A mug."
                                    "\n2. A t-shirt."
                                    "\n3. A keychain."
                                    "\nSouvenir: "))

    msg: str = str(f"I {HEART} NYC")

    if souvenir == 1:
        print(f"\n{cow} buys a mug with '{msg}' on it! {cow} will definitely use this a lot at home.")
        x += 5
    else:
        if souvenir == 2:
            print(f"\n{cow} buys a t-shirt with '{msg}' on it! But {cow} is a cow, so it's a bit snug...")
            x += 1
        else:
            if souvenir == 3:
                print(f"\n{cow} buys a keychain with '{msg}' on it! {cow} doesn't have keys, but still likes it.")
                x += 3 
    return nyc_2(x)


def nyc_2(x: int) -> int:
    """Second activity in NYC. Eating at restaurant, points assigned based on choice."""
    print(f"\nNext, you and {cow} decide to get some food.")

    PIZZA: str = "\U0001F355"
    BURGER: str = "\U0001F354"
    HOT_DOG: str = "\U0001F32D"
    FRIES: str = "\U0001F35F"
    PRETZEL: str = "\U0001F968"
    SALAD: str = "\U0001F957"

    order: int = int(input(f"What should you and {cow} order?:"
                        "\n1. Burgers."
                            "\n2. Hot dogs."
                            "\n3. Pizza."
                            "\nOrder: "))

    if order == 1:
        print(f"\n{cow} looks offended, and orders a salad instead...\n{SALAD}{BURGER}")
        x += 1
    else:
        if order == 2:
            print(f"\n{cow} thinks the hot dog is pretty good!\n{COW_FACE}{HOT_DOG}")
            x += 5
        else:
            if order == 3:
                print(f"\nGreat choice, {player}. Pizza is {cow}'s absolute favorite!\n{COW_FACE}{PIZZA}")
                x += 10

    side: int = int(input("\nDid you want to order a side?:"
                        "\n1. Fries!"
                            "\n2. A pretzel!"
                            "\n3. I'm okay, thanks."
                            "\nSide: "))

    if side == 1:
        print(f"{cow} does love fries! {FRIES}")
        x += 10
    else:
        if side == 2:
            print(f"{cow} thinks the pretzel is delicious! {PRETZEL}")
            x += 5
    return nyc_3(x)


def nyc_3(x: int) -> int:
    """Final activity in NYC. Baseball game where score is randomized. Give points based on outcome guess."""
    print(f"\nLastly, you and {cow} decide to go to a baseball game! "
            "Today, the Yankees are playing the Red Sox.")

    BASEBALL: str = "\U000026BE"

    from random import randint
    redsox: int = randint(0, 9)
    yankees: int = randint(0, 9)

    guess: int = int(input(f"\nWho do you think will win, {player}?"
                            "\n1. Red Sox."
                                "\n2. Yankees."
                                "\nMy guess: "))
    
    if redsox > yankees:
        print(f"\nWhat a game! The final score was {redsox} - {yankees}, and the Red Sox won.")
        winner = 1
    else:
        if redsox < yankees:
            print(f"\nWhat a game! The final score was {yankees} - {redsox}, and the Yankees won.")
            winner = 2
        else:
            print(f"\nThe score was {yankees} - {redsox} -- a tie!")
            winner = 0
    
    if guess == winner:
        print(f"\nLooks like your prediction was right, {player}! And {cow} caught a home run. "
        f"What a fun day!\n{COW_FACE}{BASEBALL}")
        x += 15
    else:
        if winner == 0:
            print(f"\nLooks like your prediction was half right, {player}. What a fun day!\n{COW_FACE}{BASEBALL}")
            x += 10
        else:
            if guess != winner:
                print(f"\nAh, too bad, {player}. At least the game was fun!\n{COW_FACE}{BASEBALL}")
                x += 5
    return x


def moon_1(x: int) -> int:
    """First activity on the moon. Adds points based on flavor choice; gives random additional points."""
    ROCKET: str = "\U0001F680"
    ICE_CREAM: str = "\U0001f368"

    print(f"\nYou and {cow} blast off to the moon! {ROCKET}\nFirst, you decide to eat some astronaut ice cream.")

    flavor: int = int(input(f"What flavor would you like, {player}?"
                            "\n1. Chocolate."
                                "\n2. Vanilla."
                                "\nFlavor: "))

    if flavor == 1:
        x += 10
    else:
        if flavor == 2:
            x += 5

    from random import randint
    scoops: int = randint(1, 3)
    if scoops == 1:
        print(f"You and {cow} each get 1 scoop of ice cream {ICE_CREAM} Yum!")
        x += 1
    else:
        if scoops == 2:
            print(f"You and {cow} each get 2 scoops of ice cream {ICE_CREAM} Delicious!")
            x += 3
        else:
            if scoops == 3:
                print(f"You and {cow} each get 3 scoops of ice cream {ICE_CREAM} Hurray!")
                x += 5
    return moon_2(x)


def moon_2(x: int) -> int:
    """Second activity on the moon. Adds points based on choice made."""
    print(f"\nNext, you and {cow} go stargazing!")

    STAR: str = "\U0001F320"
    MILKY_WAY: str = "\U0001F30C"
    SATURN: str = "\U0001FA90"
    TELESCOPE: str = "\U0001F52D"

    stargaze: int = int(input(f"\nWhat should {cow} look for in their telescope?:"
                                "\n1. A star."
                                    "\n2. A planet."
                                    "\n3. A galaxy."
                                    "\nLook for: "))

    if stargaze == 1:
        print(f"\n{cow} finds a shooting star!\n{STAR}{TELESCOPE}{COW}")
        x += 10
    else:
        if stargaze == 2:
            print(f"\nLook, {cow} can see Saturn from here!\n{SATURN}{TELESCOPE}{COW}")
            x += 5
        else:
            if stargaze == 3:
                print(f"\n{cow} sees the Milky Way - as a cow, {cow} loves the name.\n{MILKY_WAY}{TELESCOPE}{COW}")
                x += 15
    return moon_3(x)


def moon_3(x: int) -> int:
    """Last activity on the moon."""
    print(f"\nJust as you and {cow} are about to head home, you spot an alien!")

    ALIEN: str = "\U0001F47D"
    PEACE: str = "\U0000270C"
    SPACESHIP: str = "\U0001F6F8"

    greetings: str = str(input("Do you say hello? (yes/no): "))
    if greetings == "yes":
        print(f"\n{cow} and the alien become friends! He offers you both a ride home in his spaceship."
        f"\n{ALIEN}{PEACE}{SPACESHIP}")
        x += 15
    else:
        if greetings == "no":
            print(f"\nThe alien gets frightened by you, and blasts off back into space...\n{ALIEN}{SPACESHIP}")
            x += 5
    return x


def home_1() -> None:
    """First activity at home. Completing chores adds points; can do multiple for additional points in any order."""
    print(f"\nA relaxing day at home sounds perfect to {cow}! First, you decide to get a few chores done.")

    BASKET: str = "\U0001F9FA"
    SOAP: str = "\U0001F9FC"
    LETTER: str = "\U0001F48C"

    laundry: str = str("1. Laundry.")
    dishes: str = str(" 2. Dishes.")
    mail: str = str("3. Get the mail.")

    to_do: list[str] = [laundry, dishes, mail, "4. None."]

    global points
    while len(to_do) > 1:
        chores: int = int(input(f"\n{cow} still has a few things on their to-do list:\n{to_do}"
        "\nWhich one would you like to do?: "))
        if chores == 1:
            print(f"\n{cow} goes to do their laundry, only cows don't have clothes... {BASKET} Chore #1 done!")
            points += 10
            to_do.remove(laundry)
        else:
            if chores == 2:
                print(f"\n{cow} scrubs all the dishes until they sparkle {SOAP} Chore #2 done!")
                points += 10
                to_do.remove(dishes)
            else:
                if chores == 3:
                    print(f"\n{cow} checks the mailbox and finds a letter from their best cow friend {LETTER} "
                        "Chore #3 done!")
                    to_do.remove(mail)
                else:
                    if chores == 4:
                        print(f"\n{cow} is ready for the next activity in store!.")
                        to_do = []
                        home_2()
    
    print(f"\nNice job completing all of {cow}'s chores, {player}! Onto the next activity.")
    points += 15
    return home_2()


def home_2() -> None:
    """Second activity at home. Adds points based on hobby, certain hobbies give additional points based on choices."""
    print(f"\nNext, {cow} decides to try a new hobby!")

    hobby: int = int(input(f"\nWhat hobby should {cow} try?: "
                            "\n1. Baking."
                                "\n2. Gardening."
                                "\n3. Painting."
                                "\nHobby: "))

    COOKIE: str = "\U0001F36A"
    PIE: str = "\U0001F967"
    CUPCAKE: str = "\U0001F9C1"
    SUNFLOWER: str = "\U0001F33B"
    TULIP: str = "\U0001F337"
    ROSE: str = "\U0001F339"
    PAINT: str = "\U0001F3A8"

    global points
    if hobby == 1:
        points += 10
        bake: int = int(input(f"\nWhat would you like to bake, {player}?: "
                            "\n1. Cookies"
                                "\n2. Pie."
                                "\n3. Cupcakes."
                                "\nBake: "))

        if bake == 1:
            print(f"\nYou and {cow} make some delicious chocolate chip cookies!"
                f"\n{COW_FACE}{COOKIE}")
            points += 10
        else:
            if bake == 2:
                print(f"\n{cow} is not the biggest fan of pie, but you make blueberry pie - {cow}'s favorite!"
                    f"\n{COW_FACE}{PIE}")
                points += 5
            else:
                if bake == 3:
                    print(f"\n{cow} loves any kind of cake, especially cupcakes!"
                        f"\n{COW_FACE}{CUPCAKE}")
                    points += 15
    
    if hobby == 2:
        points += 10
        flower: int = int(input(f"\nWhat kind of flowers should {cow} plant?:"
                                "\n1. Sunflowers."
                                    "\n2. Tulips."
                                    "\n3. Roses."
                                    "\nFlower: "))

        if flower == 1:
            print(f"\n{cow}'s garden looks so cheeful with the bright yellow sunflowers {SUNFLOWER}")
            points += 15
        else:
            if flower == 2:
                print(f"The tulips look so pretty in {cow}'s garden {TULIP}")
                points += 10
            else:
                if flower == 3:
                    print(f"{cow} thinks the red roses look so beautiful {ROSE}")
                    points += 10

    if hobby == 3:
        points += 20
        print(f"\n{cow} paints a beautiful painting of their latest adventures."
                f"They are quite the artist.\n{COW_FACE}{PAINT}")

    return goodnight()


def goodnight() -> None:
    """3 main adventure paths converge, loop back to the beginning."""
    print(f"\nAfter a long day, you and {cow} decide it's time for a good night's rest. ")
    BED: str = "\U0001F6CF"
    WINDOW: str = "\U0001FA9F"
    MIRROR: str = "\U0001FA9E"
    DOOR: str = "\U0001F6AA"

    roof: str = str(f"  ____||__\n //\\\\     \\\n//{MIRROR} \\\\_____\\")
    house: str = str(f"|{BED} | {WINDOW}  {WINDOW}  |\n|{DOOR}|       |")

    print(str(f"{roof}\n{house}"))

    SLEEP: str = "\U0001F4A4"
    MOON: str = "\U0001F319"

    print(f"{cow} had such a fun day, and hopes to see you again soon, {player}!\n"
            f"\n*Goodnight {cow}, and sweet dreams!*\n{COW_FACE}{SLEEP}{MOON}"
                f"\nAdventure points: {points}")

    play: str = input("\nContinue? (yes/no): ")
    if play == "yes":
        print(f"Good morning, {player}. Another fun day is in store for you and {cow}!")
    else:
        print(f"\nThanks for playing today, {player}. {cow} will miss you :( Until next time!"
                f"\nAdventure points earned: {points} {COW_FACE}")
        quit()
    return None


if __name__ == "__main__":
    main()