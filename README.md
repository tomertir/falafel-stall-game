# Falafel Stall Game 

A time-management cooking game written in Python, built as part of a Introduction to Computer Science in Pythoncourse at Ben-Gurion University.

## Overview

Run a falafel stall where customers arrive with different personalities and moods. Players must serve dishes quickly and correctly before customers lose patience. The game implements advanced OOP concepts including **Strategy Pattern**, **State Pattern**, and dynamic mood systems.

## Game Mechanics

### Objective
Serve customers by creating the exact dish they ordered before they run out of patience. You have **3 lives** — lose a life each time a customer leaves angry.

### Customer System
Each customer has:
-  **Mood** (Calm, Angry, Explosive, Furious) — affects patience depletion rate
-  **Personality** (Type A, Type B, Chill) — determines how mood changes over time
-  **Patience meter** — decreases as they wait
-  **Arrival time** — tracks how long they've been waiting

### Ingredients
Players combine ingredients by entering numbers:
```
0: green salad
1: falafel
2: french fries
3: coleslaw
4: fried eggplants
5: tachina
6: humus
```

## Design Patterns Implemented

### Strategy Pattern
**Purpose:** Flexible order and serving strategies

**Orders Strategy** — controls how customers arrive:
- `FixedOrdersStrategy` — predetermined customer queue
- `RandomOrdersStrategy` — randomized arrivals with constraints

**Serving Strategy** — determines which customer to serve next:
- `ArrivalTimeServingStrategy` — first-come, first-served
- `LongestWaitingTimeServingStrategy` — serve longest-waiting customer
- `LeastPatienceCustomerServingStrategy` — serve most impatient customer

### State Pattern
**Mood transitions:**
```
Calm → Angry → Explosive → Furious
```
Each mood has a different `patience_factor` that controls how quickly patience depletes.

### Personality Types
- **Type A** — impatient, mood deteriorates quickly
- **Type B** — balanced temperament
- **Chill** — patient, stays calm longer

## Project Structure

```
hw5/
├── Game.py                              # Main game loop
├── FalafelStall.py                      # Order management
├── Customer.py                          # Customer class with mood/patience
├── Dish.py                              # Dish representation
├── Personality.py                       # Base personality class
├── TypeA.py, TypeB.py, Chill.py        # Personality implementations
├── Mood.py                              # Base mood class
├── Calm.py, Angry.py, Explosive.py, Furious.py  # Mood states
├── ServingStrategy.py                   # Strategy interface
├── ArrivalTimeServingStrategy.py
├── LongestWaitingTimeServingStrategy.py
├── LeastPatienceCustomerServingStrategy.py
├── OrdersStrategy.py                    # Orders generator interface
├── FixedOrdersStrategy.py
├── RandomOrdersStrategy.py
├── exceptions.py                        # Custom exceptions
├── main.py                              # Entry point
└── test_*.py                            # Unit tests
```

## How to Run

**Requirements:** Python 3.7+

### Run the Game
```bash
python main.py
```

### Run Tests
```bash
python -m pytest test_Game.py
python -m pytest test_Customer.py
# ... run any test file
```

## Example Gameplay

```
Customer:
***************************
* name: Alice             *
* mood: Calm              *
* personality: Type A     *
* patience: 95.5          *
***************************
Dish: {falafel, tachina, humus}

Insert ingredients:
0: green salad
1: falafel
2: french fries
3: coleslaw
4: fried eggplants
5: tachina
6: humus

> 1 5 6

✓ Correct! Customer served.
```

## OOP Concepts Demonstrated

- **Encapsulation** — private attributes, getters/setters
- **Inheritance** — Mood, Personality, Strategy base classes
- **Polymorphism** — different personalities/moods behave differently
- **Strategy Pattern** — pluggable order/serving algorithms
- **State Pattern** — dynamic mood transitions
- **Composition** — Customer contains Mood and Personality
- **Iterator Protocol** — OrdersStrategy uses Python generators
- **Exception Handling** — custom exceptions for game logic
- **Time Management** — real-time patience tracking with `time` module

## Key Features

-  **Real-time gameplay** — patience decreases with actual elapsed time
-  **Randomized orders** — different customer combinations each game
-  **Unit tested** — comprehensive test coverage
-  **Extensible design** — easy to add new moods, personalities, or strategies
-  **Copy semantics** — proper use of `copy` module to prevent state leaks

## Technologies

- Python 3
- Object-Oriented Programming
- Design Patterns (Strategy, State)
- Unit Testing (pytest)
- Time-based game mechanics

## Course

Introduction to Computer Science in Python — Ben-Gurion University of the Negev
