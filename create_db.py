import sqlalchemy as db
import models

engine = db.create_engine('sqlite:///activities.db', echo=True)
models.Base.metadata.create_all(engine)

