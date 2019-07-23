things=["mozzarella","cinderella","salmonella"]
human_set={"cinderella"}
cheese_set={"mozzarella"}
virus_set={"salmonella"}

#thingsリスト書き換えない版(リスト内包表記)
list = [thing for thing in things if thing not in virus_set]
print(list)

#thingsリスト書き換える版
for thing in things: 
  if thing in virus_set:
    things.remove(thing)
print(things)