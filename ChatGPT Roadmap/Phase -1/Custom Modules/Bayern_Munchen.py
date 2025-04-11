from random import randint

hq = "Munich, Germany"
founded = "1900"
league_titles = "33 Bundesliga titles"
UCL_winning = "6 titles"
slogan = "Mia San Mia (We are who we are)"

factos = [
  "Bundesliga Dominance : Won 10 consecutive league titles (2013-2023).",
  "Saved Rivals : Helped Borussia Dortmund financially in 2004.",
  "Goalkeeper Legacy – Produced legends like Maier, Kahn, and Neuer."
]  

def funfact():
  x = randint(0,2)
  print(factos[x])

if __name__ == "__main__":
  funfact()
