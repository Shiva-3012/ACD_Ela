import os


# ============================================================
# CLEAR SCREEN
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# DRAW NFA
# ============================================================

def draw_nfa():

    print()
    print("=" * 62)
    print("                     NFA VISUALIZATION")
    print("=" * 62)
    print()

    print("                         1")
    print("                    +---------+")
    print("                    |         |")
    print("                    |         |")
    print("                    +---------+")
    print("                         ^")
    print("                         |")
    print("                         |")
    print("                         |")
    print("                    +---------+")
    print("                 0  |         |  1")
    print("              +---->|    q1   |------+")
    print("              |     |         |      |")
    print("              |     +---------+      |")
    print("              |          |           |")
    print("              |          | 1         |")
    print("              |          v           |")
    print("              |     +===========+    |")
    print("              +-----|    q2      |<--+")
    print("                    |   FINAL    |")
    print("                    +===========+")
    print()

    print("                    +---------+")
    print("              START |    q0   |")
    print("                    +---------+")
    print("                         |")
    print("                         | 0")
    print("                         v")
    print("                        q1")

    print()
    print("=" * 62)
    print("START STATE : q0")
    print("FINAL STATE : q2")

    print("\nNFA Transitions:")
    print("q0 --0--> {q1}")
    print("q0 --1--> {q0}")
    print("q1 --0--> {q1}")
    print("q1 --1--> {q2}")
    print("q2 --0--> {q2}")
    print("q2 --1--> {q2}")

    print("=" * 62)


# ============================================================
# GET NEXT STATE
# ============================================================

def get_next_state(state, input_symbol):

    if state == "q0":

        if input_symbol == '0':
            return "q1"
        else:
            return "q0"

    elif state == "q1":

        if input_symbol == '0':
            return "q1"
        else:
            return "q2"

    elif state == "q2":

        return "q2"

    return "q0"


# ============================================================
# MAIN
# ============================================================

def main():

    input_string = ""
    state = "q0"

    # --------------------------------------------------------
    # Initial screen
    # --------------------------------------------------------

    clear_screen()

    print("=" * 62)
    print("                  DFA TO NFA CONVERSION")
    print("=" * 62)

    print("\nA DFA is already a special type of NFA.")
    print("Each DFA transition is represented as a set containing one state.")

    # --------------------------------------------------------
    # DFA TRANSITION
    # --------------------------------------------------------

    print("\nDFA Transition:")
    print("q0 --0--> q1")
    print("q0 --1--> q0")
    print("q1 --0--> q1")
    print("q1 --1--> q2")
    print("q2 --0--> q2")
    print("q2 --1--> q2")

    # --------------------------------------------------------
    # EQUIVALENT NFA
    # --------------------------------------------------------

    print("\nEquivalent NFA Transition:")
    print("q0 --0--> {q1}")
    print("q0 --1--> {q0}")
    print("q1 --0--> {q1}")
    print("q1 --1--> {q2}")
    print("q2 --0--> {q2}")
    print("q2 --1--> {q2}")

    print("\n" + "=" * 62)

    input("\nPress ENTER to view NFA visualization...")

    # --------------------------------------------------------
    # NFA VISUALIZATION
    # --------------------------------------------------------

    clear_screen()

    draw_nfa()

    # --------------------------------------------------------
    # INPUT
    # --------------------------------------------------------

    input_string = input("\nEnter a binary string: ")

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    for symbol in input_string:

        if symbol != '0' and symbol != '1':

            print("\nInvalid input!")
            print("Only 0 and 1 are allowed.")

            return

    # --------------------------------------------------------
    # START NFA EXECUTION
    # --------------------------------------------------------

    print("\nStarting NFA execution...")
    input("Press ENTER to continue.")

    # --------------------------------------------------------
    # PROCESS EACH INPUT SYMBOL
    # --------------------------------------------------------

    for symbol in input_string:

        current_state = state

        next_state = get_next_state(
            state,
            symbol
        )

        clear_screen()

        draw_nfa()

        print("\n\n" + "=" * 62)
        print("                    NFA EXECUTION")
        print("=" * 62)

        print("\nInput string :", input_string)
        print("Reading      :", symbol)
        print("Current state:", current_state)

        print(
            "Transition   :",
            current_state,
            "--" + symbol + "-->",
            "{" + next_state + "}"
        )

        print(
            "\nNext state set: {" +
            next_state +
            "}"
        )

        print("\nPress ENTER for next transition...")

        state = next_state

        input()

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    clear_screen()

    draw_nfa()

    print("\n\n" + "=" * 62)
    print("                       RESULT")
    print("=" * 62)

    print("\nInput String :", input_string)
    print("Final State  : {" + state + "}")

    if state == "q2":

        print("\nRESULT : ACCEPTED")
        print("The NFA reached the final state q2.")

    else:

        print("\nRESULT : REJECTED")
        print("The NFA did not reach the final state q2.")

    print("\n" + "=" * 62)


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()