from setuptools import setup, find_packages
import os

version = '1.0.9'

setup(name='htwkimn.theme',
      version=version,
      description="A responsive Diazo theme for mobile-friendly websites with Plone 4. As child theme, it extends the responsive plonetheme.onegov and aims for easy development with small or fast changing teams - like at the faculty IMN of the University of Applied Sience Leipzig (HTWK), Germany.",
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
        'plonetheme.onegov>=1.5.3',
        'ftw.footer',
        'ftw.mobilenavigation',
        'ftw.contentpage>=1.11.3',
        'ftw.contenttemplates',
        'ftw.contentmenu',
        'six>=1.4.1',
        'simplelayout.base>=4.0.5',
        'ftw.upgrade>=1.14.4'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
