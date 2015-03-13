#Documentation regarding the use and implementation of the Python Microformats Parser.

# Implementation #

The way the python microformats parse works is actually quite simple. The base Parser class implements only a few methods: _run\_filters,_add\_filter, _open\_stream and parse. These three functions combine to do all the running of the parser._

The basic idea is that parsing a microformat is running a set of filters on the original html data. In many cases this begins by "xmlizing" the html by brining it into an etree representation (I use lxml). From there one can apply an xsl filter to it, and then further, parse that output in a final filter.

# Extending #

All new parser should extend the Parser class. Then overwrite the init function to add new filters onto the parser.