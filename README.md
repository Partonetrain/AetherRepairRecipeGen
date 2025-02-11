# AetherRepairRecipeGen

Generates repair recipes for the Altar (formerly Enchanter). These can be placed in datapacks to enhance compatibility with The Aether.
[This is necessary since this type of recipe currently does not properly support tags](https://github.com/The-Aether-Team/The-Aether/issues/2546).
Only tested with The Aether on NeoForge 1.21.1. You may be able to modify the script or template for other versions.

# Usage
1. Edit items.csv. Each line represents a material tier, which is used to determine the repair time (and thus the amount of fuel necessary). By default, 1 ambrosium shard burns for 250 ticks, and 1 ambrosium block burns for 2500. The script supports up to post-Netherite tier but can be easily modified to support more.
2. Run AetherRepairRecipeGen.py. It will display what directories and recipe JSONS were created.
3. Place "recipe" folder in datapack.