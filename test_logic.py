import sys
sys.path.append("/Users/nathanwaggoner/PlanterPi/")
#import pumps as p
#import db as db
from datetime import datetime
from sqltest import session, sensor_data, plconfigs

#Variables for average moisture calc
moisture = 0
m_count = 0

#Sensors contains
sensors = session.query(sensor_data).order_by(sensor_data.log_id.desc()).limit(24)
for s in sensors:
	m_count += 1
	#print(s.soil_moisture)
	moisture += s.soil_moisture
	#print(moisture)

avg_moisture = moisture/m_count
#print(avg_moisture)
#pumps = p.l298n(22, 15, 18,7,12,11)
print(plconfigs.cons_days_watered)

print(datetime.now());

if(avg_moisture < 55):
	run_time = 15
	run_speed = 100
	#pumps.pump1(run_speed, run_time);
	print('    ran pump 1');
	print('    Moisture: ' + str(avg_moisture));
	days_watered = plconfigs.cons_days_watered
	days_watered += 1
	if(days_watered > 2):
		run_time = plconfigs.run_time
		run_time += 5
		plconfigs.run_time = run_time


	plconfigs.cons_days_watered = days_watered
	session.commit()

	# Add a user
	#jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='🐬', test='1')
	#session.add(jwk_user)
	#session.commit()



else:
	print('    did not run pump 1');
	print('    Moisture: ' + str(avg_moisture));
	#days_watered = planter_config
	#demeter_sensors.update_cons_days_watered(0)



#pumps.cleanup()
#pumps.pump1()
