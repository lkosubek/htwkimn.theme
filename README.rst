htwkimn.theme
=================

This is a responsive Diazo Plone theme. It's build on top of the product plonetheme.onegov and was
initialy developed for the Plone4 website of the faculty FIMN (http://imn.htwk-leipzig.de), which is
part of the largest university of applied sciences in East Germany, HTWK Leipzig (http://www.htwk-leipzig.de).

**Important** this package doesn't work with python 2.6, it requires at least python 2.7


Usage
-----

- Add ``htwkimn.theme`` to your buildout configuration:

::

    [instance]
    eggs +=
        htwkimn.theme

- Install/Activate the generic import profile via extension setup in your site configuration
- Have a look for the resources/dummy-content folder for some content examples

Goals
------

The main goal of the theme is easy maintainability. So it's build as child-theme that can't live 
without but benefits from the continuing development of it's parent plonetheme.onegov. 

It has less code than an own theme. So you can get an overview about the source code faster, which 
makes it easy for future staff to change the look of the faculty website, especially if they are 
unfamiliar with Plone.

To reach that goal, the child extends the parents rules.xml, adds some rules to modifiy the 
parent template on the fly and registers some custom scss files, to overwrite the neccessary css 
styles. 


Features
--------
- Fully responsive design
- Slider and tile-navigation on home page
- Collapsing simple layout columns in content area
- SCSS based
- Less code, faster understanding if you're unfamiliar with Diazo themes
- Includes features of plonetheme.onegov (https://github.com/OneGov/plonetheme.onegov#Features)
- Benefits from fixes and upgrades of plonetheme.onegov but adapations won't be overwriten
- Variables to easily adapt to corporate design of faculty and university


Additional SCSS
---------------

@see https://github.com/OneGov/plonetheme.onegov#additional-scss


Utilizes following add-ons for comfort of content editors
---------------------------------------------------------
- ftw.contentpage
- ftw.contenttemplates
- ftw.contentmenu
- ftw.footer
- ftw.upgrade
- ftw.mobilenavigation


Examples
--------

Desktop

.. image:: https://raw.github.com/lkosubek/htwkimn.theme/master/docs/screenshot-desktop.jpg

Mobile-Landscape

.. image:: https://raw.github.com/lkosubek/htwkimn.theme/master/docs/screenshot-mobile-landscape.jpg


Copyright
---------

This package is copyright by `Lars Kosubek <http://larskosubek.com>`_.

``htwkimn.theme`` is licensed under GNU General Public License, version 2.
