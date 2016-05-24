from entities import *
from res.location import Location

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

#Bronze Oak Wood
bronze_oak_wood = Location()
bronze_oak_wood.name = "Bronze Oak Wood"
bronze_oak_wood.description = """
This wood is filled as far as the eye can see with mighty Bronze 
Oaks. The moss-covered ground is springy underfoot and littered 
with tiny Bronze Acorns. You can hear the babbling of a brook 
nearby and hear the birds twittering away high above in the canopy.
You can see huge footprints a head of you, it looks like the Orcs
stomped straight through this beautiful wood."""

#Iron Pine Forest
iron_pine_forest = Location()
iron_pine_forest.name = "Iron Pine Forest"
iron_pine_forest.description = """
A dense forest lies before you. Its dark depths become quickly
impenetrable to your eyes. You can hear a skittering in the darkness
and a heavy flapping of leathery wings. The trees are gnarled and
sharp looking. There is a narrow, overgrown path in front of you and
no sign that the Orcs have disturbed this haunted ground ..."""

#Literary Lake
literary_lake = Location()
literary_lake.name = "Literary Lake"
literary_lake.description = """
The landscape opens up before you to reveal a sparkling blue
lake. You can see into its crystal depths and admire all the 
interesting flora and fauna. A hummingbird sits upon your shoulder
and begins to recite beautiful poetry. The rabbits at your feet are 
performing sonnets and you can hear the muffled voices of the fish 
below the surface. Any creature to drink the water of this lake is 
overwhelmed with urge to recite poetry. Is that a rude limmerick 
you hear coming from the distant edge of the lake? It almost sounds
like a bunch of Orcs stopped for a drink ..."""

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

bronze_oak_wood.connect_north(rust_grass_meadow)
rust_grass_meadow.connect_south(bronze_oak_wood)

farmstead.connect_north(iron_pine_forest)
iron_pine_forest.connect_south(farmstead)

literary_lake.connect_north(wheat_field)
wheat_field.connect_south(literary_lake)

literary_lake.connect_east(rust_grass_meadow)
rust_grass_meadow.connect_west(literary_lake)
