# 🌸 Aromatic Finder™

A fun little terminal-based Python program that determines whether a compound is *Aromatic* or *Aliphatic* based on its pi electron count and charge state — using Hückel's Rule!

---

## ⚗️ How It Works

This program applies **Hückel's Rule** (`4n + 2`) to check if the number of π electrons fits aromatic criteria.  
It asks two simple inputs:
- Total number of pi electrons (`π-electrons`)
- Charge state of the compound:
  - `_` → Neutral  
  - `i` / `I` → Charged (Ion)

Based on this input, it returns one of the following:
- **Aromatic** → Fits 4n+2 rule and is charged
- **Possibly Aromatic** → Fits 4n+2 rule but is neutral (resonance check not supported)
- **Aliphatic** → Doesn’t fit the rule

---

## ▶️ Usage

Run the script using any Python 3 interpreter:

```bash
python aromatic_finder.py
```

Then follow the prompts.  
To exit, enter `69` as the number of pi electrons.

---

## 🔐 Example

```
Welcome to Aromatic Finder™
Please provide the total number of pi electrons in the molecule (input 69 to exit): 6
Please provide the charge state of the compound (input 'i' if charged, _ if neutral): i
The compound is Aromatic
```

---

## 📎 Notes
- No external libraries needed.
- Focused on basic logic implementation for beginners.
- Doesn't handle resonance or molecular structure — only pure electron count logic.

---

## 👨‍💻 Made with 💻 by Sakib
