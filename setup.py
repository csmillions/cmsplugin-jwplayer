from setuptools import setup, find_packages
import cmsplugin_javascript

setup(
	name = "cmsplugin-javascript",
	version = cmsplugin_javascript.__version__,
	packages = find_packages(),

	author = "Chris Modjeska",
	author_email = "kin@remuria.net",
	description = "",
	keywords = "django django-cms",
	url = "https://github.com/csmillions/cmsplugin-javascript/",
	include_package_data=True,
	long_description= """
	""",
)