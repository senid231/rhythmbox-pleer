# - encoding: utf8 - 
#
# Copyright © 2013 S2h G
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

import urllib
import urllib.parse
import urllib.request as urllib2

import re


def parse_tracks(html):
	""" Parse HTML to retrieve listed tracks """
	matches = []
	records = re.findall( '<li duration="(.*?)source="default">', html.decode(), re.MULTILINE|re.DOTALL )
	
	for currRecord in records :
		details = {
			'artist': re.findall('singer="(.*?)"', currRecord, re.MULTILINE|re.DOTALL)[0], 
			'song': re.findall('song="(.*?)"', currRecord, re.MULTILINE|re.DOTALL)[0], 
			'duration': re.findall('([0-9]*?)"', currRecord, re.MULTILINE|re.DOTALL)[0], 
			'link': re.findall('link="(.*?)"', currRecord, re.MULTILINE|re.DOTALL)[0]
		}
		matches.append(details)
	
	return(matches)


def getMp3URL(linkId):
	""" Query Pleer API to get MP3 URL for given id"""
	mp3URL = ''
	
	url = 'http://pleer.com/site_api/files/get_url'
	
	userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	header = { 'User-Agent': userAgent }
	
	postData = { 'action': 'play', 'id': linkId }
	
	encodedPost = urllib.parse.urlencode(postData).encode('utf-8')
	httpRequest = urllib2.Request(url, encodedPost, header)
	
	httpResponse = urllib2.urlopen(httpRequest)
	textResponse = httpResponse.read()
	
	matches = re.findall('track_link":"(.*?)"', textResponse.decode(), re.MULTILINE|re.DOTALL)
	
	if len(matches):
		mp3URL = matches[0]
	
	return(mp3URL)

