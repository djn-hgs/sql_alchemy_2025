import sqlalchemy as db
import sqlalchemy.orm as orm
import models as m

# Create a session

engine = db.create_engine('sqlite:///activities.db', echo=True)

with orm.Session(engine) as session:

    # Get all pupils

    pupils = session.query(m.Pupil).all()

    for pupil in pupils:
        print(pupil)
        print(pupil.subjects)

    # Get all subjects

    subjects = session.query(m.Subject).all()

    for subject in subjects:
        print(subject)
        print(subject.pupils)

    # Get a specific pupil

    pupil = session.query(m.Pupil).\
        filter_by(first_name='Ada').\
        filter_by(last_name='Lovelace').\
        all()

    print(pupil)

