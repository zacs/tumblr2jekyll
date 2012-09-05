"""
tumblr2hyde.py: A script to migrate a tumblr blog into Hyde content.
Author: Zac Schellhardt (zac@z4c.us)
Website: http://github.com/zacs/tumblr2hyde
"""

API_KEY = "YOUR_API_KEY"
TUMBLR_ROOT = "YOUR_ROOT_DOMAIN"
TEXT_ONLY = True
CUSTOM_FIELDS = {"extends": "blog.j2", "default_block": "post", "listable": "true"}

import urllib2
import json
import os
import codecs
import re

def loadTumblr(knownPosts, tumblrUrl, apiKey, 
               perPage=20, offset=0, textOnly=True):
    """Return complete contents of a Tumblr blog (paging-aware)."""
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
                              tumblrUrl, apiKey, perPage, offset + perPage, textOnly)
        else:
            return loadTumblr(knownPosts + data["response"]["posts"],
                              tumblrUrl, apiKey, perPage, offset + perPage, textOnly)
    pass

def initializeDirs():
    """Create Hyde-style dirs if they don't already exist in CWD."""
    dirs = ["content/blog/","content/media/images/"]
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)
	pass

def createSinglePost(tumblrData):
    """Creates a single post's file and saves any images."""
    fileLoc = "content/blog/%s.html" % tumblrData["slug"]
    fileLoc = fileLoc.encode("ASCII")
    f = codecs.open(fileLoc, "w", "utf-8")
    fileContents = "---\n"
    fileContents += "title: %s\n" % tumblrData["title"]
    fileContents += "description: >\n"
    fileContents += "    %s\n" % tumblrData["title"]
    fileContents += "created: !!timestamp '%s'\n" % tumblrData["date"]
    fileContents += "tags:\n"
    for tag in tumblrData["tags"]:
        fileContents += "    - %s\n" % tag
    for key, value in CUSTOM_FIELDS.iteritems():
        fileContents += "%s: %s\n" % (key, value)
    fileContents += "---\n\n"
    body = downloadImages(tumblrData["body"], "content/media/images/", tumblrData["slug"])
    fileContents += body
    f.write(fileContents)
    f.close()
    pass

def downloadImage(url, path):
    """Download a single image to a given path."""
    f = urllib2.urlopen(url)
    img = open(path, 'wb')
    img.write(f.read())
    img.close()
    f.close()
    pass

def downloadImages(body, directory, slug):
    """Downloads any images reference in a post, and returns rewritten body
    text which references the downloaded images using a relative path
    (your /media/images/ path with a subdirectory of the post's stub).
    
    """
    dir = directory + slug
    imgs = re.findall(r'<img [^>]*src="([^"]+)"', body, re.I)
    if imgs:
        if not os.path.exists(dir):
            os.makedirs(dir)
        for img in imgs:
            filename = img.split('/')
            templatesrc = '![]([[!!images/%s/%s]])' % (slug, filename[len(filename)-1])
            filepath = '%s%s/%s' % (directory, slug, filename[len(filename)-1])
            downloadImage(img, filepath)
            body = body.replace(img, templatesrc)
        return body
    else:
        return body
    pass

def main():
    """docstring for main"""
    data = loadTumblr(None, TUMBLR_ROOT, API_KEY, textOnly=TEXT_ONLY)
    initializeDirs()
    for post in data:
        createSinglePost(post)
    pass

if __name__ == '__main__':
    main()