tumblr2hyde
===========

*Images within posts not working yet*. Script for pulling posts out of Tumblr and creating content for Hyde (or presumably Jekyll, but I'm not sure). 

Usage
-----

1. Go to Tumblr and [request an API key](http://www.tumblr.com/oauth/register). 
2. Paste the *OAuth Consumer Key* into the script as `API_KEY`.
3. Enter your site's root Tumblr URL as `TUMBLR_ROOT`.
4. [Optional] Change the `TEXT_ONLY` setting to False if you want more than just your text posts.
5. [Optional] Add/remove tuples from the `CUSTOM_FIELDS` dictionary. [More info](#custom_fields).
6. In the terminal: `python tumblr2hyde.py` -- the directory structure for Hyde will be created wherever the script is run from.

Assumptions
-----------

1. The Tumblr V2 API stil exists.
2. You are using a traditional Hyde structure (eg. /blog/contents/ and /media/images/). If not, the script is easy enough to edit on your own.
3. You don't really care about the `description` field in the posts, since Tumblr doesn't have one (I just re-write the title there).

### <a id="custom_fields"/>Details on custom fields

Many Hyde templates require some extra fields in order to render correctly. [Michael Grosner](http://www.michaelgrosner.com/blog/2011/8/5-installing-hyde.html) covers some of this in his excellent Hyde tutorial (see the _Including Content_ section of the link above for more details). I have that setting pre-populated with the values from Michael's post. They won't hurt anything if you don't need them, but feel free to delete as well. 

------

That should do it. No need really to set up a virtualenv, as there are no requirement modules outside of core Python libraries. 