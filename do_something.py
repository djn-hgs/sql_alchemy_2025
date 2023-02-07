import sqlalchemy as db
import sqlalchemy.orm as orm
import models as m

# Create some instances of pupils

ada = m.Pupil(first_name='Ada', last_name='Lovelace')
bob = m.Pupil(first_name='Bob', last_name='Smith')
alan = m.Pupil(first_name='Alan',last_name='Turing')

pupils = [
  bob,
  alan
]

# Now create some instances of subjects

cs = m.Subject(name='Computer Science', shortname='CS')
maths = m.Subject(name='Mathematics', shortname='M')

subjects = [
  cs,
  maths
]

alan.subjects.append(maths)
ada.subjects.append(cs)


engine = db.create_engine('sqlite:///activities.db', echo=True)

with orm.Session(engine) as session:
  session.add(ada)
  session.add_all(pupils)
  session.add_all(subjects)
  session.commit()

  alan.say_hi()
  print(alan.subjects)