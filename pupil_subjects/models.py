import sqlalchemy as db
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as base

# Somewhere to start

Base = base.declarative_base()

# A table to link pupils to subjects

pupil_subject = db.Table('pupil_subject',
                         Base.metadata,
                         db.Column('id', db.Integer, primary_key=True),
                         db.Column('pupil_id', db.ForeignKey('pupil.id')),
                         db.Column('subject_id', db.ForeignKey('subject.id')),
                         db.UniqueConstraint('subject_id', 'pupil_id')
                         )


# A Pupil class which is also a pupil table

class Pupil(Base):
    __tablename__ = 'pupil'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    subjects = orm.relationship('Subject',
                                secondary=pupil_subject,
                                back_populates='pupils'
                                )

    def __repr__(self):
        return f'Pupil is {self.last_name}, {self.first_name}'

    def say_hi(self):
        print(f'{self.first_name} says Hello World')


# A subject class which is also a subject table

class Subject(Base):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    shortname = db.Column(db.String, nullable=False)

    pupils = orm.relationship('Pupil',
                              secondary=pupil_subject,
                              back_populates='subjects'
                              )

    def __repr__(self):
        return f'Subject is {self.name}'
