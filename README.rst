htwkimn.theme
==============

This is a responsive Diazo Plone Theme. It's build on top of the responsive Diazo `plonetheme.onegov` product and creates beautiful content representations on desktop and mobile devices. 

It was created in a masters thesis about mobile-friendly Plone websites, that could be developed and maintained by small and fast changing dev-teams and was initially used at the faculty `FIMN <http://imn.htwk-leipzig.de>`_ - a part of the largest university of applied sciences in East Germany.

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
- Depending on the version you'll fetch from plonetheme.onegov, you might need to pin ``six = 1.5.2``

Goals and strategy
------------------

The theme aims for an easy maintainable way to develop a responsive, mobile-friendly website with small or fast-changing teams. Therefore
it's build as child-theme, that can't live without but benefits from the continuing development of
its parent-theme `plonetheme.onegov`. 

It has less code than an individual theme. So you can get an overview about its source code faster, which 
makes it easier for new staff to change the look and feel of the resulting website, especially if they are 
unfamiliar with Plone or Diazo.

To reach that goal, the child-theme extends the parent-theme, adds some Diazo rules to modifiy the parents HTML-structure on the fly and registers some custom SCSS files, to overwrite the original CSS styles.

.. image:: https://raw.github.com/lkosubek/htwkimn.theme/master/docs/diazo_parent-theme-model.png

As you can see, the child brings its own Diazo rules.xml to adapt the Diazo html-template of the parent-theme. Furthermore it brings its own CSS styles to adapt the parents layout as well as its styling. 


Features
--------
- Fully responsive design for mobile devices like smartphones or tablets and traditional desktops
- Flexible width, based on a flexible 16-column grid (`deco grid <http://limi.net/deco.gs>`_) and desktop-first design
- Slider and tile-navigation on home page
- Collapsing `SimpleLayout <https://plone.org/products/simplelayout.base>`_ columns in content area
- SCSS based for easy CSS development
- Less code, faster understanding if you're unfamiliar with Diazo or Plone themes
- Includes features of `plonetheme.onegov <https://github.com/OneGov/plonetheme.onegov#Features>`_ 
- Benefits from fixes and upgrades of `plonetheme.onegov <https://github.com/OneGov/plonetheme.onegov#Features>`_ but own implementations won't be overwriten
- SCSS variables for an easy switch to your own corporate design
- Based on Plone 4 best practises


Custom SCSS
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

Live and in action

`HTWK faculty FIMN <http://portal.imn.htwk-leipzig.de/>`_

Desktop

.. image:: https://raw.github.com/lkosubek/htwkimn.theme/master/docs/screenshot-desktop.jpg

Mobile-Landscape

.. image:: https://raw.github.com/lkosubek/htwkimn.theme/master/docs/screenshot-mobile-landscape.jpg


Copyright
---------

This package is copyright by `Lars Kosubek <http://larskosubek.com>`_ and was developed in his master thesis `Webseiten  für  mobile  sowie  konventionelle  Endgeräte  mit dem Content-Management-System Plone, Konzeption und Implementierung eines leicht zu wartenden Themes auf Basis von Diazo und Responsive Webdesign für das CMS einer Fakultät der HTWK-Leipzig <http://larskosubek.com/docs/uni/20150511_MA-Thesis_RwdPloneDiazoThemes_LarsKosubek.pdf>`_. 

``htwkimn.theme`` is licensed under GNU General Public License, version 2.


