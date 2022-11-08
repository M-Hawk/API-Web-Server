from flask import Blueprint
from init import db, bcrypt
from datetime import date

from models.states import State
# from models.areas import Area
# from models.problems import Problem
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
            state_name = "QLD"
        ),
        State(
            state_name = "NSW"
        ),
        State(
            state_name = "ACT"
        ),
        State(
            state_name = "VIC"
        ),
        State(
            state_name = "SA"
        ),
        State(
            state_name = "NT"
        ),
        State(
            state_name = "WA"
        ),
        State(
            state_name = "TAS"
        ),
    ]

    db.session.add_all(states)
    db.session.commit()

    # areas = [
    #     Area(

    #     )
    # ]
    # problems = [
    #     Problem(
    #         title = "Start the project",
    #         description = "Stage 1 - Create the database",
    #         status = "To Do",
    #         priority = "High",
    #         date = date.today(),
    #         user = users[0]
    #     ),
    #     Problem(
    #         title = "SQLAlchemy",
    #         description = "Stage 2 - Integrate ORM",
    #         status = "Ongoing",
    #         priority = "High",
    #         date = date.today(),
    #         user = users[0]
    #     )
    # ]

    # db.session.add_all(problems)
    # db.session.commit()





#     users = [
#         User(
#             email='admin@spam.com',
#             password=bcrypt.generate_password_hash('eggs').decode('utf-8'),
#             is_admin=True
#         ),
#         User(
#             name='John Cleese',
#             email='someone@spam.com',
#             password=bcrypt.generate_password_hash('12345').decode('utf-8')
#         )
#     ]

#     db.session.add_all(users)
#     db.session.commit()

#     comments = [
#         Comment(
#             message = 'Comment 1',
#             user = users[1],
#             card = cards[0],
#             date = date.today()
#         ),
#         Comment(
#             message = 'Comment 2',
#             user = users[0],
#             card = cards[0],
#             date = date.today()
#         ),
#         Comment(
#             message = 'Comment 3',
#             user = users[0],
#             card = cards[2],
#             date = date.today()
#         )
#     ]

#     db.session.add_all(comments)
#     db.session.commit()

    print("Tables seeded")