# - encoding: utf8 - 
#
# Copyright © 2010 Alexey Grunichev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class PleerResult:
	def __init__(self, entry):
		# Store the function. This will be called when we are ready to be added to the db.
		self.title = entry['song']
		self.artist = entry['artist']
		self.duration = int(entry['duration'])
		self.url = entry['link'] # /!\ Not a URL at this point of the program execution /!\
