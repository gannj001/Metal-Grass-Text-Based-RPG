from res.location import Location
from entities import *

#Farmstead Location
farmstead = Location()
farmstead.name = "Farmstead"
farmstead.description = """
This is your home.  Well it was, it has since been burned down.
Looks like your old scarecrow is still standing, maybe you could
take out your anger on that?  There might also be something to 
eat in your cupboards."""
farmstead.add_entity(scarecrow)

#Wheat Field Location
wheat_field = Location()
wheat_field.name = "Wheat Field"
wheat_field.description = """
This is one of your bigger wheat fields, it is surrounded by a, 
now broken, stone wall.  You can easily see a trampled trail 
going through the tall, yellow stalks.  Maybe it's best to go 
into town than try and track the Orcs yourself..."""
#print(farmstead.name)

#Stony Path Location
stony_path = Location()
stony_path.name = "Stony Path"
stony_path.description = """
You always meant to clear this stony path of some of the rocks
that were on it but you never did.  Seemed like the weekends 
were always to short.  Two ruts move away from the field towards
town where you used to drive your cart."""

#Rust Grass Meadow Location
rust_grass_meadow = Location()
rust_grass_meadow.name = "Rust Grass Meadow"
rust_grass_meadow.description = """
This meadow is covered in a brown-red grass that chimes in the 
wind.  There are some crushed blades of grass around the edge, 
this must've been where the Orcs came through.  Seems like none
of them were stupid enough to walk into the grass.  In the 
distance you can see smoke rising from a "miner's" hut.  You 
catch a silvery metallic glint from the corner of your eye, 
probably one of picking suits they wear, left out in the sun."""

#Connections
#connections format:
#<first_location>.connect_<direction>(second_location)
#<second_location>.connect_<opposite_direction>(first_location)

wheat_field.connect_north(farmstead)
farmstead.connect_south(wheat_field)

stony_path.connect_west(wheat_field)
wheat_field.connect_east(stony_path)

rust_grass_meadow.connect_north(stony_path)
stony_path.connect_south(rust_grass_meadow)