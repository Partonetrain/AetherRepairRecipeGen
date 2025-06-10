import os
import json
import time
import csv

ITEMS_FILE_NAME = "items.csv"
TEMPLATE_FILE_NAME = "template.json"
RECIPE_DIR = "recipe"
items = [[],[],[],[],[],[],[]] #Number of sublists = number of tiers
start_time = 0


def main():
  print('AetherRepairRecipeGen by Partonetrain')
  start_time = time.perf_counter()
  checkFilesExist()
  ParseItems()
  recipes_generated = FillTemplate()
  end_time = time.perf_counter()
  execution_time = end_time - start_time
  
  print(f"Generated {recipes_generated} recipes in {execution_time:.4f} seconds")

def checkFilesExist():
    if(not (os.path.exists(ITEMS_FILE_NAME) and os.path.exists(TEMPLATE_FILE_NAME)) ):
        print("Necessary files do not exist, exiting...")
        time.sleep(3)
        quit()

def ParseItems():
  with open(ITEMS_FILE_NAME, 'r') as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)

    item_count = 0
    line = 0
    for row in reader:
      for column in row:
        items[line].append(column)
        item_count = item_count + 1
      line = line + 1
    print(f"parsed {item_count} items")
    csv_file.close()

def FillTemplate():
  recipes_generated = 0
  tier = 0
  
  template_data = ""
  with open(TEMPLATE_FILE_NAME, 'r') as json_file:
    template_data = json.load(json_file)

  tryMakeDir(RECIPE_DIR)
  for row in items:
    for item_id in row:
      split_id = item_id.split(":")
      mod_id = split_id[0]
      print("Mod ID: " + mod_id)
      item_name = split_id[1]
      path = RECIPE_DIR + "\\" + mod_id
      tryMakeDir(path)
      recipe_data = template_data

      for entry in recipe_data["neoforge:conditions"]:
        entry["modid"] = mod_id
        assert entry["modid"] == mod_id #previous method wasn't working
        
      for entry in recipe_data["fabric:load_conditions"]:
        entry["values"] = [mod_id]

      recipe_data["group"] = getGroupFromItem(item_name)

      recipe_data["ingredient"]["item"] = item_id

      recipe_data["repairTime"] = getTimeFromTier(tier)
        
      recipe_path = path + "\\" + item_name + ".json"
      with open(recipe_path, "w") as output_file:
        json.dump(recipe_data, output_file)
        print("Generated recipe for " + item_id)
        recipes_generated = recipes_generated + 1
      output_file.close()
    tier = tier + 1
  return recipes_generated

def getTimeFromTier(tier):
    if(tier == 0): # Wood
        return 250
    if(tier == 1): # Gold
        return 300
    if(tier == 2): # Stone
        return 500
    if(tier == 3): # Iron
        return 750
    if(tier == 4): # Diamond
        return 1500
    if(tier == 5): # Netherite
        return 2000
    if(tier > 5): # Anything higher
        return 3000

def getGroupFromItem(itemName):
  if("helmet" in itemName):
    return "altar_helmet_repair"
  if("chestplate" in itemName):
    return "altar_chestplate_repair"
  if("leggings" in itemName):
    return "altar_leggings_repair"
  if("boots" in itemName):
    return "altar_chestplate_repair"
  if("sword" in itemName):
    return "altar_sword_repair"
  if("pickaxe" in itemName):
    return "altar_pickaxe_repair"
  if("shovel" in itemName):
    return "altar_shovel_repair"
  if("axe" in itemName):
    return "altar_axe_repair"
  if("hoe" in itemName):
    return "altar_hoe_repair"
  
  if("gloves" in itemName):
    return "altar_gloves_repair"
  
  if("knife" in itemName):
    return "altar_knife_repair"

  return "altar_misc_repair"

def tryMakeDir(path):
  try:
    os.mkdir(path)
    print(f"created '{path}' directory")
  except FileExistsError:
    #print(f"did not create '{path}' directory")
    pass


if __name__ == '__main__':
  main()
