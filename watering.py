import sys
sys.path.append("/home/pi/PlanterPi/")
import pumps as p
#import db as db
from planter import planter
from datetime import datetime



#print(demeter.get_planter_header_data(demeter.planter_name))
class water_logic(planter):
	def __init__(self, planter_name):
		planter.__init__(self, planter_name)
		self.moisture_check = self.check_avg_moisture()
		
		
	
	def check_avg_moisture(self):
		if (self.avg_moisture() < int(self.target_moisture)):
			return 1
		else:
			return 0
	
	def update_cons_days(self):
		if (self.moisture_check):
			days_watered = int(self.cons_days_watered) + 1
			self.update_cons_days_watered(days_watered)
			return 1
		else:
			self.update_cons_days_watered(0)
			return 0
			
	def adj_run_time(self):
		if (int(self.cons_days_watered) > 2):
			run_time = int(self.run_time) + 1
			self.update_run_time(run_time)
		
	
		
log = water_logic('Demeter')

#print(log.adj_run_time())
