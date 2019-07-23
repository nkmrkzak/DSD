things=["mozzarella","cinderella","salmonella"]
human_set={"cinderella"}
cheese_set={"mozzarella"}
virus_set={"salmonella"}

#thingsリスト書き換えない版(リスト内包表記)
list = [thing.capitalize() if thing in human_set else thing for thing in things]
print(list)

#thingsリスト書き換える版
for index,thing in enumerate(things):
  if thing in human_set: 
    things[index] = thing.capitalize()
print(things)