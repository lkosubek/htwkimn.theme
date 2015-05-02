from setuptools import setup, find_packages
import os

version = '1.0.2'

setup(name='htwkimn.theme',
      version=version,
      description="A diazo child theme product, that inherits extends the responsive diazo theme plonetheme.onegov, for the faculty IMN of the University of Applied Since Leipzig (HTWK), Germany.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='theme, responsive, diazo, plonetheme.onegov, university',
      author='Lars Kosubek',
      author_email='post@larskosubek.com',
      url='https://github.com/lkosubek/htwkimn.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['htwkimn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Plone>=4.3.3',
        'plonetheme.onegov==1.5',
        'ftw.footer',
        'ftw.mobilenavigation',
        'ftw.contentpage==1.9',
        'ftw.contenttemplates',
        'ftw.contentmenu',
        'six==1.4.1',
        'simplelayout.base==4.0.4',
        'ftw.upgrade==1.12'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
