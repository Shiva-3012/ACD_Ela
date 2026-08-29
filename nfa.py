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

    print("                 0                    1")
    print("        +----------------+    +----------------+")
    print("        |                |    |                |")
    print("        v                |    v                |")
    print("   +---------+           |  +=========+        |")
    print("   |         |           |  ||        ||       |")
    print("   |   q0    |-----------+->||   q1   ||-------+")
    print("   |         |     0        ||        ||   0,1 |")
    print("   +---------+              +=========+        |")
    print("        |                         |             |")
    print("        |                         | 1           |")
    print("        | 1                       v             |")
    print("        |                   +=========+        |")
    print("        +------------------>|   q2    |<-------+")
    print("                            |  FINAL  |")
    print("                            +=========+")
    print()

    print("                    ^")
    print("                    |")
    print("                  START")

    print()
    print("=" * 62)

    print("START STATE : q0")
    print("FINAL STATE : q2")
    print("TYPE        : NON-DETERMINISTIC FINITE AUTOMATON")

    print("=" * 62)

    print("\nTransitions:")
    print("q0 --0--> q0")
    print("q0 --0--> q1")
    print("q0 --1--> q2")
    print("q1 --1--> q2")
    print("q2 --0--> q2")
    print("q2 --1--> q2")

    print("\n" + "=" * 62)


# ============================================================
# MAIN
# ============================================================

def main():

    input_string = ""

    # Clear screen
    clear_screen()

    # Display NFA
    draw_nfa()

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
    # NFA TRANSITION TABLE
    # ========================================================

    print("\nNFA transition table:\n")

    print("State       0             1")
    print("--------------------------------")
    print("q0          {q0,q1}       {q2}")
    print("q1          {}             {q2}")
    print("q2          {q2}           {q2}")

    # ========================================================
    # INPUT INFORMATION
    # ========================================================

    print("\n\nInput String :", input_string)

    print(
        "\nNFA can have MULTIPLE possible states "
        "after reading a symbol."
    )

    print(
        "\nTherefore, unlike a DFA, one state can have "
        "multiple transitions"
    )

    print(
        "\nfor the same input symbol."
    )

    # ========================================================
    # END
    # ========================================================

    print("\n" + "=" * 62)
    print("                   NFA VISUALIZATION END")
    print("=" * 62)


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()