# Author: Xiangting Li xzl5423@psu.edu
# Collaborator: Jiahui Lan jzl6335@psu.edu
# collaborator: Thomas Huggett tfh5238@psu.edu
# collaborator: Abdullahn Nadeem azn5413@psu.edu

temperature = input("Enter temperature: ")

unit = input("Enter unit in F/f or C/c: ")
if unit =="F" or unit == "f":
  temperature=float(temperature)
  celsius=float(temperature-32)*5/9
  print(str(temperature)+ "°"+ " in Fahrenheit is equivalent to " + str(celsius)+ "°"+ " Celsius.")
elif unit =="C" or unit == "c":
  temperature=float(temperature)
  fahrenheit=float(temperature*9/5+32)
  print(str(temperature) + "°" +" in Celsius is equivalent to "+ str(fahrenheit)+"°"+ " Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
