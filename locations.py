from res.location import Location
from .entity import *

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

#Murky Marsh
murky_marsh = Location()
murky_marsh.name = "Murky Marsh"
murky_marsh.description = """
The smell of death and decay hits you, the Murky Marsh smells awful 
at this time of year. The ground is soft beneath your feet and you
can see vultures circling high up ahead. The ground looks like it has
been stomped through recently but you can't tell what direction they
were travelling. You might have to look around for some friendly critters
and ask if they have seen those dastardly Orcs."""

#The Pass
the_pass = Location()
the_pass.name = "The Pass"
the_pass.description = """
The Pass is the only way to enter the The Metal Mountains. The lush
green surrounding you quickly turns to grit and rubble. The Pass is a 
rocky and winding path where bandits like to wait in ambush. You can
see the remains of a campsite not too far away. The ashes of the campfire
are still smoldering and there are animal bones strewn around it. Looks
like you have just missed the Orcs. Be careful ..."""

#Chequered Plains
chequered_plains = Location()
chequered_plains.name = Chequered Plains
chequered_plains.description = """ 
The Chequered Plains was planted on the whim of the Old King. He wanted
somewhere to play a giant chess match. Farmers and architects worked
together for months to create this giant black and white playing fields.
Huge game pieces were hewn from finest marble by leading sculpters. On
opening night, a lavish party was thrown and an enourmous game was played.
The King, however, soon grew bored of his new toy and Chequered Plains has
since fallen into disrepair; the once-neat squares are now overgrown and 
the giant playing pieces lay strewn over the "board". There doesn't seem to be 
sign of the Orcs here but it is so run down that you probably wouldn't be 
able to see evidence of their passing."""

#Toadstool Farm
toadstool_farm = Location()
toadstool_farm.name = "Toadstool Farm"
toadstool_farm.description = """ 
The ground is suddenly cast into shadow. Looking up, you see a giant 
toadstool; the stem is pure white and about an armspan wide! It has
a bright read cap covered in tiny white blemishes. Spinning slowly,
you can see that you are surrounded by them. This must be Toadstool
Farm, you can remember listening to that slightly odd man in the tavern
tell you about this place one evening but you hadn't believed it was a 
real thing! Looking closer, you notice some of the toadstools look 
severly damaged - as though hacked at with an axe or halberd. You wouldn't
be surprised if the Orcs had passed through here."""

#

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

murky_marsh.connect_west(iron_pine_forest)
iron_pine_forest.connect_east(murky_marsh)

the_pass.connect_east(farmstead)
farmstead.connect_west(the_pass)

chequered_plains.connect_east(wheat_field)
wheat_field.connect_west(chequered_plains)

chequered_plains.connect_north(the_pass)
the_pass.connect_south(chequered_plains)

toadstool_farm.connect_east(literary_lake)
literary_lake.connect_west(toadstool_farm)

toadstool_farm.connect_north(chequered_plains)
chequered_plains.connect_south(toadstool_farm)
