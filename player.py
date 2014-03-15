class Player(object):
	def __init__(self, data):
		self.name = data['name']['full']

		self.display_position = data['display_position']
		self.eligible_positions = data['eligible_positions']['position']
		self.selected_position = data['selected_position']['position']