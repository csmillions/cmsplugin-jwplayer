from setuptools import setup, find_packages
import cmsplugin_jwplayer

setup(
	name = "cmsplugin-jwplayer",
	version = cmsplugin_jwplayer.__version__,
	packages = find_packages(),

	author = "Chris Modjeska",
	author_email = "kin@remuria.net",
	description = "",
	keywords = "django django-cms",
	url = "https://github.com/csmillions/cmsplugin-jwplayer/",
	include_package_data=True,
	long_description= """
	""",
	install_requires=[
		"django-ordered-model",
		"django",
	],
)