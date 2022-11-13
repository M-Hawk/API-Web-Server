# Endpoints Documentation for Bouldering API

## User Routes

### **GET Requests**

#### States

**/states/**

* Methods: GET
* Arguments: None
* Description: Allows a climber user to get all states in the database and their respective areas
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example: Will produce a much larger list

``` JSON
{
    "state_id": 4,
    "state_name": "Victoria",
    "state_acronym": "VIC",
    "areas": []
},
{
    "state_id": 5,
    "state_name": "South Australia",
    "state_acronym": "SA",
    "areas": []
},
{
    "state_id": 6,
    "state_name": "Northern Territory",
    "state_acronym": "NT",
    "areas": []
}
```

**/states/int:id/**

* Methods: GET
* Arguments: state_id
* Description: Allows a climber user to get a state by its given ID and its respective areas
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
{
    "state_id": 1,
    "state_name": "Queensland",
    "state_acronym": "QLD",
    "areas": [
        {
            "area_id": 1,
            "area_name": "Tooheys Forest",
            "description": "Located near the heart of Brisbane in bushland, Tooheys Forest has easy access, and amenities such as flushable toilets, water and BBQ facilities at the main carpark, plenty of boulders from V0 -V4, with grades up to V11 available and a current total of 300 problems. The Rock is 380 million year old quartzite, that is coarse and may contain sharp crystals, be mindful of skin care. Features challenging mantle topouts with many slopers. Most landings are flat and easily protected.",
            "ethics": "Local urban nature preserve, a common are of walkers and cyclists, dogs are also allowed on leash. Be courteous to other groups, and keep noise to a minimum, do not climbed damaged or chipped routes and clean up your rubbish. Please also clean chalk and marks on boulders and stick to the given trails if available",
            "access": "Entry to northern area via the car park at Tooheys Picnic Area on google maps, located on Toohey Rd. Lat & Long provided are those of the Picnic Area Main Car Park. Trails provide entry to most sectors which have relatively flat approaches and easy access.",
            "latitude_south": "-27.53691 South",
            "longitude_east": "153.0417 East"
        }
    ]
}
```

#### Areas

**/areas/**

* Methods:  GET
* Arguments: None
* Description: Allows a climber user to get all areas in the database and their respective sectors
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example: Will produce a much larger list

``` JSON
{
    "area_id": 1,
    "area_name": "Tooheys Forest",
    "description": "Located near the heart of Brisbane in bushland, Tooheys Forest has easy access, and amenities such as flushable toilets, water and BBQ facilities at the main carpark, plenty of boulders from V0 -V4, with grades up to V11 available and a current total of 300 problems. The Rock is 380 million year old quartzite, that is coarse and may contain sharp crystals, be mindful of skin care. Features challenging mantle topouts with many slopers. Most landings are flat and easily protected.",
    "ethics": "Local urban nature preserve, a common are of walkers and cyclists, dogs are also allowed on leash. Be courteous to other groups, and keep noise to a minimum, do not climbed damaged or chipped routes and clean up your rubbish. Please also clean chalk and marks on boulders and stick to the given trails if available",
    "access": "Entry to northern area via the car park at Tooheys Picnic Area on google maps, located on Toohey Rd. Lat & Long provided are those of the Picnic Area Main Car Park. Trails provide entry to most sectors which have relatively flat approaches and easy access.",
    "latitude_south": "-27.53691 South",
    "longitude_east": "153.0417 East",
    "state_id": 1,
    "sectors": [
        {
            "sector_id": 1,
            "sector_name": "Lookout Area",
            "description": "A cluster of boulders around Sandstone Lookout, all problems are within V0 - V4 range with nice views towards Brisbane CBD",
            "access": "5 minute walk from Tooheys Picnic Area car park, following the Sandstone Circuit Track. As the track goes up the ridgeline, some larger boudlers will appear on the left, south side of the track.",
            "latitude_south": "-27.53869 South",
            "longitude_east": "153.04292 East",
            "area_id": 1
        },
        {
            "sector_id": 2,
            "sector_name": "Main Area",
            "description": "Where the densest concentration and highest quality boulders exist here in the forest",
            "access": "7 minute walk from Tooheys Picnic Area car park, following the Toohey Ridge Track for 5 minutes, cross the wooden bridge and pass the intersection with the Sandstone Circuit, soon after you will arrive at a Y intersection. Where the sealed track goes left, with a small amount of bitumen going right then stopping. To reach the majority of boulders, turn right until the track is dirt for 20 metres between two rocks, on the left is the \"Unleash the Dancer\" boulder and on the right is the \"Chug/Plum Boulder\".",
            "latitude_south": "-27.53966 South",
            "longitude_east": "153.04366 East",
            "area_id": 1
        }
    ]
}
```

**/areas/int:id/**

* Methods:  GET
* Arguments: area_id
* Description: Allows a climber user to get an area by its given ID and its respective sectors
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
{
    "area_id": 2,
    "area_name": "Black Range Bouldering Area",
    "description": "Located within the Queanbeyan area near the ACT and NSW borders, located an hour and a half from Canberra in the hills of Tallaganda National Park, within a Eucalypt Forest. Houses over 500 Granite problems of all types and difficulties. The boulders grow moss at a very fast rate, so bring a wire and soft bristle brush on an extension.",
    "ethics": "Located within a National Park, please minimise impact to the nature and wildlife, clean up rubbish, remove chalk marks and respect the area. Please refer to signs located in the park for more info.",
    "access": "Drive out of Queanbeyan towards Bungendore on the Kings Highway and take a right onto Captain\"s Flat Road. After driving for a while (about 13.5km) turn left onto Briars Sharrow Road (be careful to not miss this). Cross the creek and continue a short distance, taking the next right. Drive to the end of this road and at the T-intersection turn right, to Hoskinstown. Drive through the town and take a left onto a dirt road (Forbes Creek Road). The dirt road continues for some 10km through fairly rough terrain - continue on until you reach a small parking area. Back up the road some five metres and to the right is The Hill, and on the left are the remainder of the areas. Lat, Long is of the General Forbes Creek Area",
    "latitude_south": "-35.42915 South",
    "longitude_east": "149.53973 East",
    "state_id": 2,
    "sectors": [
        {
            "sector_id": 3,
            "sector_name": "The Hill",
            "description": "This area has some large walls and one very steep wall. Some grades are fairly stiff and difficult, doesn\"t have regular visitors, alot of moss, bring brushes",
            "access": "Just before the intersection and sign to Tallaganda/car parking spot turn right and head 50 metres up the hill right to the boulders, careful in a low vehicle",
            "latitude_south": "-35.44904 South",
            "longitude_east": "149.54358 East",
            "area_id": 2
        },
        {
            "sector_id": 4,
            "sector_name": "Dog Rock",
            "description": "Located in the forest a fair while from the intersection of Nth Black range fire trail & Forbes creek Rd, large group of boulders of varying grades, bring brushes",
            "access": "Head up Nth Black range fire trail until theres a little left turn near a small dam and clearing, just before a big blue gravel hill. Park and walk diagonally up and left into the trees for a few hundred metres until boulders are found.",
            "latitude_south": "-35.4322 South",
            "longitude_east": "149.54002 East",
            "area_id": 2
        }
    ]
}
```

#### Sectors

**/sectors/**

* Methods: GET
* Arguments: None
* Description: Allows a climber user to get all sectors in the database and their respective problems
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example: Will produce a much larger list

``` JSON
{
    "sector_id": 1,
    "sector_name": "Lookout Area",
    "description": "A cluster of boulders around Sandstone Lookout, all problems are within V0 - V4 range with nice views towards Brisbane CBD",
    "access": "5 minute walk from Tooheys Picnic Area car park, following the Sandstone Circuit Track. As the track goes up the ridgeline, some larger boudlers will appear on the left, south side of the track.",
    "latitude_south": "-27.53869 South",
    "longitude_east": "153.04292 East",
    "area_id": 1,
    "problems": [
        {
            "problem_id": 1,
            "problem_name": "Snakeskin",
            "v_grade": "V1",
            "surface_type": "Quartzite rock",
            "description": "Standing start on LH side, ascend on side pulls, cobbles and jugs to mantle out",
            "access": "Located in the Snakeskin Area of the Lookout Area, roughly 30m up from Sandstone Circuit Track, starts on the left hand side of the lower left boulder, just to the left of a vertical streak of light-coloured rock.",
            "height": "3 Metres",
            "comments": "fun classic climb",
            "sector_id": 1
        },
        {
            "problem_id": 2,
            "problem_name": "Hopla",
            "v_grade": "V2",
            "surface_type": "Quartzite rock",
            "description": "Sit start on the right arete of the small boulder, strenuous move off of the ground to reach jugs beneath small roof, top out from there",
            "access": "Located in the Snakeskin Area of the Lookout Area, a small boulder that rests on top of the snakeskin boulder",
            "height": "2 Metres",
            "comments": "great sit start boulder",
            "sector_id": 1
        }
    ]
}
```

**/sectors/int:id/**

* Methods: GET
* Arguments: sector_id
* Description: Allows a climber user to get a sector by its given ID and its respective problems
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
    {
        "sector_id": 4,
        "sector_name": "Dog Rock",
        "description": "Located in the forest a fair while from the intersection of Nth Black range fire trail & Forbes creek Rd, large group of boulders of varying grades, bring brushes",
        "access": "Head up Nth Black range fire trail until theres a little left turn near a small dam and clearing, just before a big blue gravel hill. Park and walk diagonally up and left into the trees for a few hundred metres until boulders are found.",
        "latitude_south": "-35.4322 South",
        "longitude_east": "149.54002 East",
        "area_id": 2,
        "problems": [
            {
                "problem_id": 5,
                "problem_name": "The Full Traverse",
                "v_grade": "V4",
                "surface_type": "Granite",
                "description": "Sit start on right of smaller boulder, full right to left traverse over the top, topping out on the massive boulder",
                "access": "Located in the Dog Rock area, its on the smaller boulder compared to the massive one",
                "height": "5 Metres",
                "comments": "Cool traverse",
                "sector_id": 4
            }
        ]
    }
```

#### Problems

**/problems/**

* Methods: GET
* Arguments: None
* Description: Allows a climber user to get all problems in the database and their respective ascents
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example: Will produce a much larger list

``` JSON
{
    "problem_id": 4,
    "problem_name": "The Tipsy Bull",
    "v_grade": "V8",
    "surface_type": "Granite",
    "description": "Start matched on the ledge of the left side of the wall, and traverse the edges and slopers on the very top lip of the boulder all the way to the lip sloper and top out",
    "access": "Located in The Hill Sector, large boulder looking from the parking spot",
    "height": "6 Metres",
    "comments": "Very difficult boulder",
    "sector_id": 3,
    "ascents": []
},
{
    "problem_id": 5,
    "problem_name": "The Full Traverse",
    "v_grade": "V4",
    "surface_type": "Granite",
    "description": "Sit start on right of smaller boulder, full right to left traverse over the top, topping out on the massive boulder",
    "access": "Located in the Dog Rock area, its on the smaller boulder compared to the massive one",
    "height": "5 Metres",
    "comments": "Cool traverse",
    "sector_id": 4,
    "ascents": []
}
```

**/problems/int:id/**

* Methods: GET
* Arguments: problem_id
* Description: Allows a climber user to get a problem by its given ID and its respective ascents
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
{
    "problem_id": 2,
    "problem_name": "Hopla",
    "v_grade": "V2",
    "surface_type": "Quartzite rock",
    "description": "Sit start on the right arete of the small boulder, strenuous move off of the ground to reach jugs beneath small roof, top out from there",
    "access": "Located in the Snakeskin Area of the Lookout Area, a small boulder that rests on top of the snakeskin boulder",
    "height": "2 Metres",
    "comments": "great sit start boulder",
    "sector_id": 1,
    "ascents": [
        {
            "climber": {
                "climber_id": 2,
                "user_name": "Psycho"
            },
            "tick_type": "redpoint",
            "comments": "Huge arm pump",
            "created": "2022-11-13"
        }
    ]
}
```

**/problems/int:id/ascents/**

* Methods: GET
* Arguments: problem_id
* Description: Allows a climber user to get a problems ascents by its given ID
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
[
    {
        "ascent_id": 2,
        "climber": {
            "climber_id": 2,
            "user_name": "Psycho"
        },
        "tick_type": "redpoint",
        "comments": "Huge arm pump",
        "created": "2022-11-13"
    }
]
```

#### Ascents

**/ascents/**

* Methods: GET
* Arguments: None
* Description: Allows a climber user to get all ascents in the database and their respective climbers and problems they are joined by
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
[
    {
        "ascent_id": 1,
        "climber": {
            "climber_id": 1,
            "user_name": "WaterworldRules"
        },
        "problem": {
            "problem_id": 3,
            "problem_name": "Trapeze Artist",
            "v_grade": "V5"
        },
        "tick_type": "flash",
        "comments": "Lucky catch on the dyno, got it first go",
        "created": "2022-11-13"
    },
    {
        "ascent_id": 2,
        "climber": {
            "climber_id": 2,
            "user_name": "Psycho"
        },
        "problem": {
            "problem_id": 2,
            "problem_name": "Hopla",
            "v_grade": "V2"
        },
        "tick_type": "redpoint",
        "comments": "Huge arm pump",
        "created": "2022-11-13"
    }
]
```

**/ascents/int:id/**

* Methods: GET
* Arguments: ascent_id
* Description: Allows a climber user to get an ascent by its given ID and its respective climbers and problems its joined by
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
{
    "ascent_id": 1,
    "climber": {
        "climber_id": 1,
        "user_name": "WaterworldRules"
    },
    "problem": {
        "problem_id": 3,
        "problem_name": "Trapeze Artist",
        "v_grade": "V5"
    },
    "tick_type": "flash",
    "comments": "Lucky catch on the dyno, got it first go",
    "created": "2022-11-13"
}
```

#### Climbers

**/auth/climbers/**

* Methods: GET
* Arguments: None
* Description: Allows a climber user to get all climbers in the database presenting their climber_id, user_name and their respective ascents
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
[
    {
        "climber_id": 1,
        "user_name": "WaterworldRules",
        "ascents": [
            {
                "ascent_id": 1,
                "problem": {
                    "problem_id": 3,
                    "problem_name": "Trapeze Artist",
                    "v_grade": "V5"
                },
                "tick_type": "flash",
                "comments": "Lucky catch on the dyno, got it first go",
                "created": "2022-11-13"
            }
        ]
    },
    {
        "climber_id": 2,
        "user_name": "Psycho",
        "ascents": [
            {
                "ascent_id": 2,
                "problem": {
                    "problem_id": 2,
                    "problem_name": "Hopla",
                    "v_grade": "V2"
                },
                "tick_type": "redpoint",
                "comments": "Huge arm pump",
                "created": "2022-11-13"
            }
        ]
    }
]
```

### **POST Requests**

**/problems/int:id/ascents/**

* Methods: POST
* Arguments: problem_id
* Description: Allows a climber user to post an ascent based on its problem ID
* Authentication: @jwt_required
* Authorisation: None
* Request Body:

``` JSON
{
    "tick_type": "Send",
    "comments": "Fun climb"
}
```

* Response Example:

``` JSON
{
    "ascent_id": 3,
    "climber": {
        "climber_id": 2,
        "user_name": "Psycho"
    },
    "problem": {
        "problem_id": 1,
        "problem_name": "Snakeskin",
        "v_grade": "V1"
    },
    "tick_type": "Send",
    "comments": "Fun climb",
    "created": "2022-11-13"
}
```

**/auth/register/**

* Methods: POST
* Arguments: None
* Description: Allows a potential user to register a new climber account
* Authentication: None
* Authorisation: None
* Request Body:

``` JSON
{
    "email_address": "newuser@climbersrus.com",
    "user_name": "TomClimbs",
    "password": "tomlovessally",
    "first_name": "Tom",
    "last_name": "Grigg"
}
```

* Response Example:

``` JSON
{
    "climber_id": 3,
    "user_name": "TomClimbs",
    "first_name": "Tom",
    "last_name": "Grigg",
    "email_address": "newuser@climbersrus.com"
}
```

**/auth/login/**

* Methods: POST
* Arguments: None
* Description: Allows a climber with an account to login
* Authentication: @jwt_required
* Authorisation: None
* Request Body:

``` JSON
{
    "email_address": "newuser@climbersrus.com",
    "password": "tomlovessally"
}
```

* Response Example:

``` JSON
{
    "email_address": "newuser@climbersrus.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODMxMzI4MiwianRpIjoiNmQxNTkxOTMtZjE3YS00MDc1LTkyNTktNTg3NGYxOTA2NGMwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2NjgzMTMyODIsImV4cCI6MTY2ODM5OTY4Mn0.KIRTxplQeOKbiAPB2ECrS4oJ_h7sGm5nUPp4-GQj6Ts",
    "admin": false
}
```

### **PUT/PATCH Requests**

**/auth/int:id/**

* Methods: PUT/PATCH
* Arguments: climber_id
* Description: Allows a climber with an account to change their own details
* Authentication: @jwt_required
* Authorisation: None
* Request Body:

``` JSON
{
    "email_address": "boulderinglegend@works.com",
    "user_name": "WaterworldRules",
    "password": "Kevinbestactor",
    "first_name": "Kevin",
    "last_name": "Costner"
}
```

* Response Example:

``` JSON
{
    "climber_id": 1,
    "admin": true,
    "user_name": "WaterworldRules",
    "first_name": "Kevin",
    "last_name": "Costner",
    "email_address": "boulderinglegend@works.com"
}
```

**/ascents/int:id/**

* Methods: PUT/PATCH
* Arguments: ascent_id
* Description: Allows a climber with an ascent to change their ascent details
* Authentication: @jwt_required
* Authorisation: None
* Request Body:

``` JSON
{
    "tick_type": "Dab",
    "comments": "Actually touched the ground on the way up"
}
```

* Response Example:

``` JSON
{
    "ascent_id": 1,
    "climber": {
        "climber_id": 1,
        "user_name": "WaterworldRules"
    },
    "problem": {
        "problem_id": 3,
        "problem_name": "Trapeze Artist",
        "v_grade": "V5"
    },
    "tick_type": "Dab",
    "comments": "Actually touched the ground on the way up",
    "created": "2022-11-13"
}
```

### **DELETE Requests**

**/auth/int:id/**

* Methods: DELETE
* Arguments: climber_id
* Description: Allows a climber with an account to delete their own account
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
{
    "message": "Climber Psycho has been deleted successfully"
}
```

**/ascents/int:id/**

* Methods: DELETE
* Arguments: ascent_id
* Description: Allows a climber with an ascent to delete it
* Authentication: @jwt_required
* Authorisation: None
* Request Body: None
* Response Example:

``` JSON
{
    "message": "Ascent 1 has been deleted successfully"
}
```

## Admin Routes

### **GET Requests**

**/auth/admin/climbers/**

* Methods:  GET
* Arguments: None
* Description: Allows an admin user to get all climber users in the database and all their details excluding password
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body: None
* Response Example:

``` JSON
[
    {
        "climber_id": 1,
        "admin": true,
        "user_name": "WaterworldRules",
        "first_name": "Kevin",
        "last_name": "Costner",
        "email_address": "boulderingarchitect@legends.com",
        "ascents": []
    },
    {
        "climber_id": 2,
        "admin": false,
        "user_name": "Psycho",
        "first_name": "Michael",
        "last_name": "Bateman",
        "email_address": "nicecards@fineprint.com",
        "ascents": [
            {
                "ascent_id": 2,
                "problem": {
                    "problem_id": 2,
                    "problem_name": "Hopla",
                    "v_grade": "V2"
                },
                "tick_type": "redpoint",
                "comments": "Huge arm pump",
                "created": "2022-11-13"
            }
        ]
    }
]
```

### **POST Requests**

**/states/**

* Methods:  POST
* Arguments: None
* Description: Allows an admin user to create a state and add it to the database
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "state_name": "NewFoundState",
    "state_acronym": "NFS"
}
```

* Response Example:

``` JSON
{
    "state_id": 9,
    "state_name": "NewFoundState",
    "state_acronym": "NFS",
    "areas": []
}
```

**/areas/**

* Methods:  POST
* Arguments: None
* Description: Allows an admin user to create an area linked by a state_id and add it to the database
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "state_id": "8",
    "area_name": "NewArea",
    "description": "description of this new area",
    "ethics": "Don't Litter",
    "access": "Drive up the highway",
    "latitude_south": "-27.2132",
    "longitude_east": "6.323221"
}
```

* Response Example:

``` JSON
{
    "area_id": 3,
    "area_name": "NewArea",
    "description": "description of this new area",
    "ethics": "Don't Litter",
    "access": "Drive up the highway",
    "latitude_south": "-27.2132 South",
    "longitude_east": "6.323221 East",
    "state_id": 8,
    "sectors": []
}
```

**/sectors/**

* Methods:  POST
* Arguments: None
* Description: Allows an admin user to create a sector linked by an area_id and add it to the database
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "area_id": "1",
    "sector_name": "NewSector",
    "description": "description of this new sector",
    "access": "Walk along the path",
    "latitude_south": "-27.6532",
    "longitude_east": "6.33221"
}
```

* Response Example:

``` JSON
{
    "sector_id": 6,
    "sector_name": "NewSector",
    "description": "description of this new sector",
    "access": "Walk along the path",
    "latitude_south": "-27.6532 South",
    "longitude_east": "6.33221 East",
    "area_id": 1,
    "problems": []
}
```

**/problems/**

* Methods:  POST
* Arguments: None
* Description: Allows an admin user to create a problem linked by a problem_id and add it to the database
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "sector_id": "1",
    "problem_name": "NewProblemsRus",
    "description": "description of this new problem",
    "surface_type": "Sandstone",
    "access": "The big boulder in the bushes",
    "v_grade": "6",
    "height": "8",
    "comments": "Follow the crack up the edge"
}
```

* Response Example:

``` JSON
{
    "problem_id": 6,
    "problem_name": "NewProblemsRus",
    "v_grade": "V6",
    "surface_type": "Sandstone",
    "description": "description of this new problem",
    "access": "The big boulder in the bushes",
    "height": "8 Metres",
    "comments": "Follow the crack up the edge",
    "sector_id": 1,
    "ascents": []
}
```

**/auth/register/admin/**

* Methods:  POST
* Arguments: None
* Description: Allows an admin user to create a new admin user
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "email_address": "newadmin@madebyadmin.com",
    "user_name": "Snooker",
    "password": "sandraspassword",
    "first_name": "Sandra",
    "last_name": "Markus"
}
```

* Response Example:

``` JSON
{
    "climber_id": 3,
    "admin": true,
    "user_name": "Snooker",
    "first_name": "Sandra",
    "last_name": "Markus",
    "email_address": "newadmin@madebyadmin.com"
}
```

### **PUT/PATCH Requests**

**/states/int:id/**

* Methods:  PUT/PATCH
* Arguments: state_id
* Description: Allows an admin user to modify a states details
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "state_name": "VanDiemansLand",
    "state_acronym": "VDL"
}
```

* Response Example:

``` JSON
{
    "state_id": 8,
    "state_name": "VanDiemansLand",
    "state_acronym": "VDL",
    "areas": [
        {
            "area_id": 3,
            "area_name": "NewArea",
            "description": "description of this new area",
            "ethics": "Don't Litter",
            "access": "Drive up the highway",
            "latitude_south": "-27.2132 South",
            "longitude_east": "6.323221 East"
        }
    ]
}
```

**/areas/int:id/**

* Methods:  PUT/PATCH
* Arguments: area_id
* Description: Allows an admin user to modify an areas details, if area is moved so is its children sectors
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "state_id": "8",
    "area_name": "AreaNameChange",
    "description": "description of this new area",
    "ethics": "Don't park on grass",
    "access": "By Car",
    "latitude_south": "-26.2342",
    "longitude_east": "145.2323"
}
```

* Response Example:

``` JSON
{
    "area_id": 3,
    "area_name": "AreaNameChange",
    "description": "description of this new area",
    "ethics": "Don't park on grass",
    "access": "By Car",
    "latitude_south": "-26.2342 South",
    "longitude_east": "145.2323 East",
    "state_id": 8,
    "sectors": []
}
```

**/sectors/int:id/**

* Methods:  PUT/PATCH
* Arguments: sector_id
* Description: Allows an admin user to modify a sectors details, if sector is moved so is its children problems
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "area_id": "2",
    "sector_name": "SectorNameChange",
    "description": "description change for sector",
    "access": "By Car",
    "latitude_south": "-26.2342",
    "longitude_east": "145.2323"
}
```

* Response Example:

``` JSON
{
    "sector_id": 1,
    "sector_name": "SectorNameChange",
    "description": "description change for sector",
    "access": "By Car",
    "latitude_south": "-26.2342 South",
    "longitude_east": "145.2323 East",
    "area_id": 2,
    "problems": [
        {
            "problem_id": 1,
            "problem_name": "Snakeskin",
            "v_grade": "V1",
            "surface_type": "Quartzite rock",
            "description": "Standing start on LH side, ascend on side pulls, cobbles and jugs to mantle out",
            "access": "Located in the Snakeskin Area of the Lookout Area, roughly 30m up from Sandstone Circuit Track, starts on the left hand side of the lower left boulder, just to the left of a vertical streak of light-coloured rock.",
            "height": "3 Metres",
            "comments": "fun classic climb",
            "sector_id": 1
        },
        {
            "problem_id": 2,
            "problem_name": "Hopla",
            "v_grade": "V2",
            "surface_type": "Quartzite rock",
            "description": "Sit start on the right arete of the small boulder, strenuous move off of the ground to reach jugs beneath small roof, top out from there",
            "access": "Located in the Snakeskin Area of the Lookout Area, a small boulder that rests on top of the snakeskin boulder",
            "height": "2 Metres",
            "comments": "great sit start boulder",
            "sector_id": 1
        },
        {
            "problem_id": 6,
            "problem_name": "NewProblemsRus",
            "v_grade": "V6",
            "surface_type": "Sandstone",
            "description": "description of this new problem",
            "access": "The big boulder in the bushes",
            "height": "8 Metres",
            "comments": "Follow the crack up the edge",
            "sector_id": 1
        }
    ]
}
```

**/problems/int:id/**

* Methods:  PUT/PATCH
* Arguments: problem_id
* Description: Allows an admin user to modify a problems details, if problem is moved so is its children ascents
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:

``` JSON
{
    "sector_id": "1",
    "problem_name": "ChangedProblemName",
    "description": "description of this new problem",
    "surface_type": "Igneous",
    "access": "The big boulder in the bushes",
    "v_grade": "3",
    "height": "4",
    "comments": "Follow the crack up the edge"
}
```

* Response Example:

``` JSON
{
    "problem_id": 1,
    "problem_name": "ChangedProblemName",
    "v_grade": "V3",
    "surface_type": "Igneous",
    "description": "description of this new problem",
    "access": "The big boulder in the bushes",
    "height": "4 Metres",
    "comments": "Follow the crack up the edge",
    "sector_id": 1,
    "ascents": []
}
```

### **DELETE Requests**

**/states/int:id/**

* Methods:  DELETE
* Arguments: state_id
* Description: Allows an admin user to delete a state
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:
* Response Example:

``` JSON
{
    "message": "State, NewFoundState has been deleted successfully"
}
```

**/areas/int:id/**

* Methods:  DELETE
* Arguments: area_id
* Description: Allows an admin user to delete an area
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:
* Response Example:

``` JSON
{
    "message": "Area, AreaNameChange has been deleted successfully"
}
```

**/sectors/int:id/**

* Methods:  DELETE
* Arguments: sector_id
* Description: Allows an admin user to delete a sector
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:
* Response Example:

``` JSON
{
    "message": "Sector, NewSector has been deleted successfully"
}
```

**/problems/int:id/**

* Methods:  DELETE
* Arguments: problem_id
* Description: Allows an admin user to delete a problem
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:
* Response Example:

``` JSON
{
    "message": "Problem, NewProblemsRus has been deleted successfully"
}
```

**/auth/int:id/**

* Methods:  DELETE
* Arguments: climber_id
* Description: Allows an admin user to delete a climber user
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:
* Response Example:

``` JSON
{
    "message": "Climber, Snooker has been deleted successfully"
}
```

**/ascents/admin/int:id/**

* Methods:  DELETE
* Arguments: ascent_id
* Description: Allows an admin user to delete an ascent
* Authentication: @jwt_required
* Authorisation: Admin required
* Request Body:
* Response Example:

``` JSON
{
    "message": "Ascent, 2 has been deleted successfully"
}
```

