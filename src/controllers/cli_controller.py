from flask import Blueprint
from init import db, bcrypt
from datetime import date

from models.states import State
from models.areas import Area
from models.sectors import Sector
from models.problems import Problem
# from models.climbers import Climber
# from models.ascents import Ascent

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_db():

    states = [
        State(
            state_name = "Queensland",
            state_acronym = "QLD",
            created = date.today()
        ),
        State(
            state_name = "New South Wales",
            state_acronym = "NSW",
            created = date.today()
        ),
        State(
            state_name = "Australian Capital Territory",
            state_acronym = "ACT",
            created = date.today()
        ),
        State(
            state_name = "Victoria",
            state_acronym = "VIC",
            created = date.today()
        ),
        State(
            state_name = "South Australia",
            state_acronym = "SA",
            created = date.today()
        ),
        State(
            state_name = "Northern Territory",
            state_acronym = "NT",
            created = date.today()
        ),
        State(
            state_name = "Western Australia",
            state_acronym = "WA",
            created = date.today()
        ),
        State(
            state_name = "Tasmania",
            state_acronym = "TAS",
            created = date.today()
        )
    ]

    db.session.add_all(states)
    db.session.commit()

    areas = [
        Area(
            state = states[0],
            area_name = "Tooheys Forest",
            description = """Located near the heart of Brisbane in bushland, Tooheys Forest has easy access, and amenities such as flushable toilets, water and BBQ facilities at the main carpark, plenty of boulders from V0 -V4, with grades up to V11 available and a current total of 300 problems. The Rock is 380 million year old quartzite, that is coarse and may contain sharp crystals, be mindful of skin care. Features challenging mantle topouts with many slopers. Most landings are flat and easily protected.""",
            ethics = """Local urban nature preserve, a common are of walkers and cyclists, dogs are also allowed on leash. Be courteous to other groups, and keep noise to a minimum, do not climbed damaged or chipped routes and clean up your rubbish. Please also clean chalk and marks on boulders and stick to the given trails if available""",
            access = """Entry to northern area via the car park at Tooheys Picnic Area on google maps, located on Toohey Rd. Lat & Long provided are those of the Picnic Area Main Car Park. Trails provide entry to most sectors which have relatively flat approaches and easy access.""",
            latitude = -27.53691,
            longitude = 153.04170,
            created = date.today()
        ),
        Area(
            state = states[1],
            area_name = "Black Range Bouldering Area",
            description = """Located within the Queanbeyan area near the ACT and NSW borders, located an hour and a half from Canberra in the hills of Tallaganda National Park, within a Eucalypt Forest. Houses over 500 Granite problems of all types and difficulties. The boulders grow moss at a very fast rate, so bring a wire and soft bristle brush on an extension.""",
            ethics = """Located within a National Park, please minimise impact to the nature and wildlife, clean up rubbish, remove chalk marks and respect the area. Please refer to signs located in the park for more info.""",
            access = """Drive out of Queanbeyan towards Bungendore on the Kings Highway and take a right onto Captain's Flat Road. After driving for a while (about 13.5km) turn left onto Briars Sharrow Road (be careful to not miss this). Cross the creek and continue a short distance, taking the next right. Drive to the end of this road and at the T-intersection turn right, to Hoskinstown. Drive through the town and take a left onto a dirt road (Forbes Creek Road). The dirt road continues for some 10km through fairly rough terrain - continue on until you reach a small parking area. Back up the road some five metres and to the right is The Hill, and on the left are the remainder of the areas. Lat, Long is of the General Forbes Creek Area""",
            latitude = -35.42915, 
            longitude = 149.53973,
            created = date.today()           
        )
    ]

    db.session.add_all(areas)
    db.session.commit()

    sectors = [
        Sector(
            area = areas[0],
            sector_name = "Lookout Area",
            description = """A cluster of boulders around Sandstone Lookout, all problems are within V0 - V4 range with nice views towards Brisbane CBD""",
            access = """5 minute walk from Tooheys Picnic Area car park, following the Sandstone Circuit Track. As the track goes up the ridgeline, some larger boudlers will appear on the left, south side of the track.""",
            latitude = -27.53869,
            longitude = 153.04293,
            created = date.today()
        ),
        Sector(
            area = areas[0],
            sector_name = "Main Area",
            description = """Where the densest concentration and highest quality boulders exist here in the forest""",
            access = """7 minute walk from Tooheys Picnic Area car park, following the Toohey Ridge Track for 5 minutes, cross the wooden bridge and pass the intersection with the Sandstone Circuit, soon after you will arrive at a Y intersection. Where the sealed track goes left, with a small amount of bitumen going right then stopping. To reach the majority of boulders, turn right until the track is dirt for 20 metres between two rocks, on the left is the 'Unleash the Dancer' boulder and on the right is the 'Chug/Plum Boulder'.""",
            latitude = -27.53966,
            longitude = 153.04365,
            created = date.today()
        ),
        Sector(
            area = areas[1],
            sector_name = "The Hill",
            description = """This area has some large walls and one very steep wall. Some grades are fairly stiff and difficult, doesn't have regular visitors, alot of moss, bring brushes""",
            access = """Just before the intersection and sign to Tallaganda/car parking spot turn right and head 50 metres up the hill right to the boulders, careful in a low vehicle""",
            latitude = -35.44904,
            longitude = 149.54358,
            created = date.today()
        ),
        Sector(
            area = areas[1],
            sector_name = "Dog Rock",
            description = """Located in the forest a fair while from the intersection of Nth Black range fire trail & Forbes creek Rd, large group of boulders of varying grades, bring brushes""",
            access = """Head up Nth Black range fire trail until theres a little left turn near a small dam and clearing, just before a big blue gravel hill. Park and walk diagonally up and left into the trees for a few hundred metres until boulders are found.""",
            latitude = -35.43220,
            longitude = 149.54003,
            created = date.today()
        )
    ]

    db.session.add_all(sectors)
    db.session.commit()

    problems = [
        Problem(
            sector = sectors[0],
            problem_name = "Snakeskin",
            grade = 1,
            surface_type = "Quartzite rock",
            description = "Standing start on LH side, ascend on side pulls, cobbles and jugs to mantle out",
            access = """Located in the Snakeskin Area of the Lookout Area, roughly 30m up from Sandstone Circuit Track, starts on the left hand side of the lower left boulder, just to the left of a vertical streak of light-coloured rock.""",
            height_metres = 3,
            comments = "fun classic climb",
            created = date.today()
        ),
        Problem(
            sector = sectors[0],
            problem_name = "Hopla",
            grade = 2,
            surface_type = "Quartzite rock",
            description = """Sit start on the right arete of the small boulder, strenuous move off of the ground to reach jugs beneath small roof, top out from there""",
            access = """Located in the Snakeskin Area of the Lookout Area, a small boulder that rests on top of the snakeskin boulder""",
            height_metres = 2,
            comments = "great sit start boulder",
            created = date.today()
        ),
        Problem(
            sector = sectors[1],
            problem_name = "Trapeze Artist",
            grade = 5,
            surface_type = "Quartzite rock",
            description = """Squat start using the undercling underneath the roof feature. Move up to a positive hold on the face and make a big move to hit the sloper on the lip""",
            access = """Located in the Area A boulders in the Main Area, located on the boulder with the prominent cave feature""",
            height_metres = 3,
            comments = "Epic dyno from under a roof",
            created = date.today()
        ),
        Problem(
            sector = sectors[2],
            problem_name = "The Tipsy Bull",
            grade = 8,
            surface_type = "Granite",
            description = """Start matched on the ledge of the left side of the wall, and traverse the edges and slopers on the very top lip of the boulder all the way to the lip sloper and top out""",
            access = """Located in The Hill Sector, large boulder looking from the parking spot""",
            height_metres = 6,
            comments = "Very difficult boulder",
            created = date.today()
        ),
        Problem(
            sector = sectors[3],
            problem_name = "The Full Traverse",
            grade = 4,
            surface_type = "Granite",
            description = """Sit start on right of smaller boulder, full right to left traverse over the top, topping out on the massive boulder""",
            access = """Located in the Dog Rock area, its on the smaller boulder compared to the massive one""",
            height_metres = 5,
            comments = "Cool traverse",
            created = date.today()
        )
    ]

    db.session.add_all(problems)
    db.session.commit()

    # climbers = [
    #     Climber(
    #         user_name = "Jimbo",
    #         password = "mrworldwide123",
    #         first_name = "Jim",
    #         last_name = "Rules",
    #         email_address = "boulderingarchitect@legends.com",
    #         admin = True,
    #         created = date.today()   
    #     ),
    #     Climber(
    #         user_name = "Pyscho",
    #         password = "oneofmyfavourites567",
    #         first_name = "Michael",
    #         last_name = "Bateman",
    #         email_address = "nicecards@fineprint.com",
    #         admin = False,
    #         created = date.today()   
    #     )
    # ]

    # db.session.add_all(climbers)
    # db.session.commit()

    # ascents = [
    #     Ascent(
    #         climber_id = climbers[0],
    #         problem_id = problems[2],
    #         tick_type = "flash", # varchar (create tuples of tick types)
    #         comments = "Lucky catch on the dyno, got it first go",
    #         created = date.today()
    #     )
    # ]

    # db.session.add_all(ascents)
    # db.session.commit()



    print("Tables seeded")