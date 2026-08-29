# Automata and Compiler Design – Finite Automata Project
Code explanation video link : https://drive.google.com/file/d/1LCg1FceHT9D2XXJ_Cf2sZgnWS-9wiCjj/view?usp=sharing
Finite Automata are mathematical models used to represent systems that process input strings and determine whether they are accepted or rejected.

This project covers:

* 🔵 **DFA Visualization**
* 🟣 **NFA Visualization**
* 🔄 **NFA to DFA Conversion**
* 🖥️ Console-based representation of automata
* 📊 Transition table generation
* 🖼️ Automata diagram generation
* 🐍 Practical implementation of Automata Theory concepts using Python

---

## ✨ Features

### 1. DFA Visualization

The project demonstrates the structure and working of a **Deterministic Finite Automaton**.

A DFA has:

* A finite set of states
* An input alphabet
* Transition functions
* One initial state
* One or more final states

The program generates a visual representation of the DFA along with its states and transitions.

---

### 2. NFA Visualization

The project demonstrates the structure and working of a **Non-Deterministic Finite Automaton**.

Unlike a DFA, an NFA can have:

* Multiple possible transitions for the same input
* Different possible computation paths
* Multiple destination states for an input symbol

The program generates the NFA transition table and visualization.

---

### 3. NFA to DFA Conversion

The project demonstrates the conversion of an NFA into an equivalent DFA using the **Subset Construction Method**.

The conversion:

* Generates DFA states from sets of NFA states
* Calculates transitions for each input symbol
* Identifies the corresponding final states
* Produces an equivalent DFA

The resulting DFA accepts the same language as the original NFA.

---

## 🗂️ Project Structure

```text
ACD_Project/
│
├── acd.py
├── NFA.png
├── DFA.png
├── NFA_DFA_Conversion.png
├── README.md
```
└── Code Explanation Video
## 🛠️ Technologies Used
Python
Python Standard Library
Automata Theory
Finite Automata
Graphviz
Console-based Visualization
##▶️ How to Run
Prerequisites

Make sure Python is installed on your system.

For example:

Python 3.x
VS Code
Graphviz
Install Required Package
pip install graphviz
Run the Program
python acd.py
The program generates the automata representations and allows binary strings to be tested.
##📊 DFA vs NFA
| Feature                            | DFA         | NFA                    |
| ---------------------------------- | ----------- | ---------------------- |
| Number of transitions for an input | Exactly one | Zero, one, or multiple |
| Multiple paths                     | ❌           | ✅                   |
| ε-transitions                      | ❌           | Possible in ε-NFA     |
| Deterministic                      | ✅           | ❌                   |
| Expressive power                   | Same        | Same                   |

Both DFA and NFA recognize regular languages.
##🎯 Learning Objectives

Through this project, we aim to understand:

The basic structure of finite automata.
How DFA transitions work.
How NFA transitions differ from DFA transitions.
How automata can be represented programmatically.
How NFA can be converted into DFA.
How transition tables are generated.
How automata diagrams can be generated programmatically.
Practical implementation of Automata Theory concepts using Python.
## 🎥 Code Explanation

A video explaining the implementation and working of the programs is available below:

**[▶️ Watch the Code Explanation Video](https://drive.google.com/file/d/1LCg1FceHT9D2XXJ_Cf2sZgnWS-9wiCjj/view?usp=sharing)**

---

## 👩‍💻 Author

**M.Shivani**

B.Tech – Computer Science & Engineering (Data Science)

VNR Vignana Jyothi Institute of Engineering and Technology

GitHub: [@Shiva-3012](https://github.com/Shiva-3012)

---

## ⭐ Acknowledgement

This project was developed as part of the **Automata and Compiler Design (ACD)** coursework to gain practical understanding of finite automata and their implementation in Python.
