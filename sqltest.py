import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine(
	'mysql+mysqlconnector://root:P3r$3ph0n3@localhost/PlanterPi',
	echo=False)

# Define the MySQL engine using MySQL Connector/Python
#engine = sqlalchemy.create_engine(
#   'mysql+mysqlconnector://pyuser:Py@pp4Demo@localhost:3306/sqlalchemy',
#    echo=True)

# Define and create the table
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))
    test = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}', test='{3}')>".format(
                            self.name, self.fullname, self.nickname, self.test)



class sensor_data(Base):
	__tablename__='sensor_data'

	log_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	log_time = sqlalchemy.Column(sqlalchemy.DateTime, server_default='log_time')
	planter_id = sqlalchemy.Column(sqlalchemy.Integer)
	temperature = sqlalchemy.Column(sqlalchemy.Integer)
	humidity = sqlalchemy.Column(sqlalchemy.Integer)
	light = sqlalchemy.Column(sqlalchemy.Integer)
	soil_temperature = sqlalchemy.Column(sqlalchemy.Integer)
	soil_moisture = sqlalchemy.Column(sqlalchemy.Integer)

	def __repr__(self):
		return "Log ID: {}, Log Time: {}, Planter ID: {}, Temperature: {}, Humidity: {}, Light: {}, Soil Temperature: {}, Soil Moisture: {}".format(self.log_id, self.log_time, self.planter_id, self.temperature, self.humidity, self.light, self.soil_temperature, self.soil_moisture)

class planter_config(Base):
	__tablename__='planter_config'

	planter_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	cons_days_watered = sqlalchemy.Column(sqlalchemy.Integer)
	run_speed = sqlalchemy.Column(sqlalchemy.Integer)
	run_time = sqlalchemy.Column(sqlalchemy.Integer)
	target_moisture = sqlalchemy.Column(sqlalchemy.Integer)

	def __repr__(self):
		return "Planter ID: {}, Consecutive Days Watered: {}, Run Speed: {}, Run Time: {}, Target Moisture: {}".format(
		self.planter_id, self.cons_days_watered, self.run_speed, self.run_time, self.target_moisture)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Add a user
#jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='🐬', test='1')
#session.add(jwk_user)
#session.commit()

# Query the user
our_user = session.query(User).filter_by(name='jesper').first()

plconfigs = session.query(planter_config).first()
# insert data via insert() construct
#ins = table.insert().values(
#      l_name='Hello',
#      f_name='World')
#conn = engine.connect()
#conn.execute(ins)

#session.add(sensor_insert)
#session.commit()


#print('\nOur User:')
#print(our_user)
#print('Nick name in hex: {0}'.format(our_user.nickname.encode('utf-8')))

#for s in plconfigs:
#	print(s.run_time)
print(plconfigs.cons_days_watered)
