tumblr2jekyll
=============

Script for pulling posts out of Tumblr and creating content for Jekyll. 

Usage
-----

1. Go to Tumblr and [request an API key](http://www.tumblr.com/oauth/register). 
2. Paste the *OAuth Consumer Key* into the script as `API_KEY`.
3. Enter your site's root Tumblr URL as `TUMBLR_ROOT`.
4. [Optional] Change the `TEXT_ONLY` setting to False if you want more than just your text posts.
5. [Optional] Add/remove tuples from the `CUSTOM_FIELDS` dictionary. [More info](#custom_fields).
6. In the terminal: `python tumblr2jekyll.py` -- the directory structure for Jekyll will be created wherever the script is run from.

Assumptions
-----------

1. The Tumblr V2 API stil exists.
2. You are using a traditional Jekyll structure (eg. `_posts/` and `images/`). If not, the script is easy enough to edit on your own.
3. You don't really care about the `description` field in the posts, since Tumblr doesn't have one (I just re-write the title there).

### <a id="custom_fields"/>Details on custom fields

You can add any custom fields using the `CUSTOM_FIELDS` dictionaty at the beginning of the script. I have that setting pre-populated with the standard `layout: post` as a default. You should always at least specify a `layout` here, and can add whatever other pairs you need or want. 

------

That should do it. No need really to set up a virtualenv, as there are no requirement modules outside of core Python libraries. 
