# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Guillaume Chevrot'
SITENAME = u"Guillaume Chevrot"
SITESUBTITLE = u'“Anyone who stops learning is old, anyone who keeps learning stays young."'
SITEURL = 'https://gchevrot.github.io/blog/output'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 10

# Title menu options
MENUITEMS = [('About - Contact', 'https://gchevrot.github.io/home/index.html'),
             ('Archives', 'https://gchevrot.github.io/blog/output/archives.html')]
NEWEST_FIRST_ARCHIVES = False

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.png']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
THEME = 'theme/pelican-octopress-theme/'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'liquid_tags.youtube']

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found."
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Search
SEARCH_BOX = False


# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')



# Sharing
TWITTER_USER = 'gchevrot'
TWITTER_TWEET_BUTTON = True
TWITTER_FOLLOW_BUTTON = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
