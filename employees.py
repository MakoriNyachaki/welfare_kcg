'''A class used for capturing and registering all county law enforment officers
employed under the county law enforcement department of Kisii County'''

class Employees:
	def __init__(self, emp_id, name, dob, emp_date, phone, email, address):
		self.emp_id = emp_id
		self.name = name
		self.dob = dob
		self.emp_date = emp_date
		self.phone = phone
		self.email = email
		self.address = address 
