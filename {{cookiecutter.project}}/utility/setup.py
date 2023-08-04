from setuptools import setup,find_packages

setup(
   name='{{cookiecutter.project_slug}}',
   version='1.0',
   description='A useful module to interacting with {{cookiecutter.project}} & related operations.',
   author='Rahul Kumar',
   license='{{cookiecutter.license}}',
   author_email='{{cookiecutter.author_email}}',
   packages=find_packages(include=['utility', 'utility.*']),
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            # 'scripts/cool',
            # 'scripts/skype',
           ]
)

# pip3 install -e .