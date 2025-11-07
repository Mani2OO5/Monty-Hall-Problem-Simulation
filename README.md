# 🎯Monty Hall Simulation

This project simulates the **Monty Hall problem**, a famous probability puzzle based on a game show scenario.  
It demonstrates the difference between **staying** with the initial choice and **switching** after one door is revealed.

---

## 📘Description

In the Monty Hall problem: 🐐🚗🚪

1. There are **three doors**: behind one is a **car**, behind the other two are **goats**.  
2. You pick one door.  
3. The host (Monty) opens one of the *other* doors, always revealing a goat.  
4. You can now **stay** with your first choice or **switch** to the remaining closed door.

Mathematically:
- Staying wins **1/3** of the time.
- Switching wins **2/3** of the time.

This simulation confirms that result by running the experiment thousands of times.

---

## 🧠How It Works

The program:
- Randomly assigns prizes behind doors.  
- Simulates both strategies — *staying* and *switching*.  
- Runs the experiment a large number of times (e.g., 100,000).  
- Prints the winning probabilities for both strategies.

### Example output: 

**Winning probability without changing:** 0.33456  
**Winning probability with changing:** 0.66544


---

## ⚙️Usage

Make sure you have **Python 3.x** installed.

Run the simulation:

```bash
python main.py
```
---

## 👨🏻‍💻Author

Created by Mani Arab

---

## ⚖️License

This project is released under the MIT License, so you can freely use, modify, and share it.

If you find this project useful, feel free to ⭐ the repo or fork it!
