tumblr2hyde
===========

*Images within posts not working yet*. Script for pulling posts out of Tumblr and creating content for Hyde (or presumably Jekyll, but I'm not sure). 

Usage
-----

1. Go to Tumblr and [request an API key](http://www.tumblr.com/oauth/register). 
2. Paste the *OAuth Consumer Key* into the script as `API_KEY`.
3. Enter your site's root Tumblr URL as `TUMBLR_ROOT`.
4. [Optional] Change the `TEXT_ONLY` setting to False if you want more than just your text posts.
5. [Optional] Add tuples to the dictionary for customer fields. [More info](#custom_fields).
6. In the terminal: `python tumblr2hyde.py` -- the directory structure for Hyde will be created wherever the script is run from.

That should do it. No need really to set up a virtualenv, as there are no requirement modules outside of core Python libraries. 