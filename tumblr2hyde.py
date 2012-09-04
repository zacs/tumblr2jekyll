"""
tumblr2hyde.py: A script to migrate a tumblr blog into Hyde content.
Author: Zac Schellhardt (zac@z4c.us)
Website: http://github.com/zacs/tumblr2hyde
"""

API_KEY = ""
TUMBLR_ROOT = ""

import urllib2
import json

def loadTumblr(knownPosts,
			   tumblrUrl,
			   apiKey,
			   perPage=20,
			   offset=0,
			   textOnly=True):
	""""docstring for loadTumblr"""
	if textOnly==True:
		url = "http://api.tumblr.com/v2/blog/%s/posts/text?api_key=%s&offset=%s&limit=%s" % (tumblrUrl, apiKey, offset, perPage)
	else:
		url = "http://api.tumblr.com/v2/blog/%s/posts?api_key=%s&offset=%s&limit=%s" % (tumblrUrl, apiKey, offset, perPage)
	f = urllib2.urlopen(urllib2.Request(url))
	data = json.load(f)
	f.close()
	if not data["response"]["posts"]:
		return knownPosts
	else:
		if knownPosts==None:
			return loadTumblr(data["response"]["posts"],
							  tumblrUrl, apiKey, perPage, offset+20, textOnly)
		else:
			return loadTumblr(knownPosts+data["response"]["posts"],
							  tumblrUrl, apiKey, perPage, offset+20, textOnly)
	pass

def createSinglePost(tumblrData):
	""""docstring for createSinglePost"""
	pass

def downloadImages(body, directory):
	""""docstring for downloadImages"""
	pass

def main():
	""""docstring for main"""
	data = loadTumblr(None, TUMBLR_ROOT, API_KEY)
	print data
	pass

if __name__ == '__main__':
	main()