import sqlalchemy as db
import sqlalchemy.orm as orm
import models as m

# Create some instances of pupils

ada = m.Pupil(first_name='Ada', last_name='Lovelace')
bob = m.Pupil(first_name='Bob', last_name='Smith')
alan = m.Pupil(first_name='Alan', last_name='Turing')

pupils = [
    bob,
    alan
]

# Now create some instances of subjects

cs = m.Subject(name='Computer Science', shortname='CS')
maths = m.Subject(name='Mathematics', shortname='M')
english = m.Subject(name='English', shortname='E')

subjects = [
    cs,
    maths,
    english
]

# Now add some links

alan.subjects.append(maths)
alan.subjects.append(cs)

ada.subjects.append(cs)
ada.subjects.append(english)

# Now push this information to the database

engine = db.create_engine('sqlite:///activities.db', echo=True)

with orm.Session(engine) as session:
    session.add(ada)
    session.add_all(pupils)
    session.add_all(subjects)
    session.commit()

    # Now let's take ba look at our info

    alan.say_hi()

    print(alan.subjects)

    ada.say_hi()

    print(ada.subjects)
