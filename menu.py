print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts")

from shot_builder import shot_builder
my_scripts.addCommand("Shot Builder", shot_builder)
