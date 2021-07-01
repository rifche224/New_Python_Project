import random
import json
#code pour s'amuser
#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

#def get_rand_number():
#  rand_num = random.randint(0,10)
#  print(rand_num)
# get_rand_number()
print("yoo!!! je me presente cherif sy je viens de commencer la programùmtion en python")
quotes = ["rien n'est plus beau d'aimer et d'etre aimer par celui qu'on aime","seul le travail paye","focused sur ton objectif","ne jamais baisser les bras"]

characters = ["cherif","walid","Mouha","Adeline","Denise","Souleymane","Maimouna","Abdou Aziz","Amina","Anna","Nene"]

def read_data_from_json():
#je déclare une liste vide pour contenir toutes les données contenues dans le fichier json que l'on charged
  value = []
  with open('charaters.json') as f:
   data = json.load(f)
   for entry in data:
    value.append(entry['character'])
   return value        

#definition de ma fonction
def get_random_quote(my_list):
  rand_number = random.randint(0, len(my_list - 1))
  item = my_list[rand_number]
  return item
 
def get_random_character():
  all_values = read_data_from_json()
  return get_random_quote(all_values)

def capitalize(words):
  for word in words:
   word.capitalize()

def message(character,quote):
  capitalize(character)
  capitalize(quote)
  return "{} a dit : {}".format(characters,quotes) 

user_answer = input("tapez entrer si vous voulez connaitre d'autre citations ou B si vous voulez quitter")

while user_answer != "B":
  print(get_random_character())
  user_answer = input("tapez entrer si vous voulez connaitre d'autre citations ou B si vous voulez quitter")
  print(message(get_random_character(characters),get_random_quote(quotes)))
