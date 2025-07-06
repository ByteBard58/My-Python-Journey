def smart_div(x,y) -> str:
  if x%y == 0:
    return "integer"
  if x%y != 0:
    return "float"

def main() -> None:
  print("Welcome to Aromatic Finder™")
  print("Just input the total number of pi electorns in the compound and the charge state of the compound, this program will do the rest :)")
  print("Info: Input 69 to exit")
  while True:
    try:
      pi_es:int = int(input("Please provide the total number of pi electrons in the molecule (input 69 to exit): "))
    except ValueError:
      print("Please provide a number, not anything else")
      continue
    if pi_es == 69:
      print("Thanks for using Aromatic Finder™. Have a great day !")
      print("Made by Sakib")
      break
    ion = input("Please provide the charge state of the compound (input 'i' if charged, _ if neutral): ")
    if ion not in ["i","I","_"]:
      print("Please provide the state in the following way without space: 'i' or 'I' if the compound is charged, _(underscore) if the compound is neutral")
      continue
    n:str = smart_div(pi_es-2,4)
    if n == "integer" and ion == "i":
      print("The compound is Aromatic")
    elif n == "integer" and ion == "_":
      print("According to the calculation, the compound should be Aromatic. BUT, this program can not determine whether the compound shows resonance or not.")
      print("So, this program is unable to completly find out whether the compound is aromatic or aliphatic.")
    elif n == "float":
      print("The compound is Aliphatic")
    else:
      print("something went wrong")

main()