import os


# ============================================================
# CLEAR SCREEN
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# DRAW DFA
# ============================================================

def draw_dfa():

    print()
    print("=" * 62)
    print("                     DFA VISUALIZATION")
    print("=" * 62)
    print()

    print("                    ┌─────────┐")
    print("                 1  │         │")
    print("              ┌─────┤    q0   │")
    print("              │     │         │")
    print("              │     └─────────┘")
    print("              │          │")
    print("              │          │ 0")
    print("              │          ▼")
    print("              │     ┌─────────┐")
    print("              │  0  │         │")
    print("              └─────┤    q1   │")
    print("                    │         │")
    print("                    └─────────┘")
    print("                         │")
    print("                         │ 1")
    print("                         ▼")
    print("                    ╔═════════╗")
    print("                    ║         ║")
    print("                    ║   q2    ║")
    print("                    ║  FINAL  ║")
    print("                    ╚═════════╝")
    print("                       ↑   │")
    print("                       │   │")
    print("                       └───┘")
    print("                        0,1")

    print()
    print("=" * 62)
    print("START STATE : q0")
    print("FINAL STATE : q2")

    print("\nTransitions:")
    print("q0 --0--> q1")
    print("q0 --1--> q0")
    print("q1 --0--> q1")
    print("q1 --1--> q2")
    print("q2 --0--> q2")
    print("q2 --1--> q2")

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
# MAIN PROGRAM
# ============================================================

def main():

    input_string = ""
    state = "q0"

    # Clear screen
    clear_screen()

    # Display DFA
    draw_dfa()

    # Get input
    input_string = input("\nEnter a binary string: ")

    # ========================================================
    # INPUT VALIDATION
    # ========================================================

    for symbol in input_string:

        if symbol != '0' and symbol != '1':

            print("\nInvalid input!")
            print("Only 0 and 1 are allowed.")

            return

    # ========================================================
    # START EXECUTION
    # ========================================================

    print("\nStarting DFA execution...")
    input("\nPress ENTER to continue.")

    # ========================================================
    # PROCESS EACH SYMBOL
    # ========================================================

    for symbol in input_string:

        current_state = state

        next_state = get_next_state(
            state,
            symbol
        )

        # Clear screen
        clear_screen()

        # Draw DFA
        draw_dfa()

        print("\n\n" + "=" * 62)
        print("                    DFA EXECUTION")
        print("=" * 62)

        print("\nInput string :", input_string)
        print("Reading      :", symbol)
        print("Current state:", current_state)

        print(
            "Transition   :",
            current_state,
            "--" + symbol + "-->",
            next_state
        )

        print("\nPress ENTER for next transition...")

        # Move to next state
        state = next_state

        input()

    # ========================================================
    # FINAL RESULT
    # ========================================================

    clear_screen()

    draw_dfa()

    print("\n\n" + "=" * 62)
    print("                       RESULT")
    print("=" * 62)

    print("\nInput String :", input_string)
    print("Final State  :", state)

    if state == "q2":

        print("\nRESULT : ACCEPTED")
        print("The DFA reached the final state q2.")

    else:

        print("\nRESULT : REJECTED")
        print("The DFA did not reach the final state q2.")

    print("\n" + "=" * 62)


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()