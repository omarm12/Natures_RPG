# Natures_RPG

## Dependencies
- python3
- node package manager

## Running Tests
- *Danielle Dishop* From Linux/Unix terminal, navigate to parent directory of Natures_RPG and run <code>python -m unittest Natures_RPG/test/statTest.py</code>
- *Colin Seifer* from Linux/Unix terminal, navigate to parent directory of Natures_RPG and run <code>python3 -m Natures_RPG.test.cstest</code>
- *Colin Seifer* to test battle system, from Linux/Unix terminal, navigate to parent directory of Natures_RPG and run <code>python3 -m Natures_RPG.test.battleTest</code>

###### Changelog:
- *Danielle Dishop* added Stats class to TypeAssign
- *Danielle Dishop* fixed the mod stat dictionary to be the correct stats
- *Danielle Dishop* moved Stats class into its own file per Colin's request and added testing for Stat assignment
- *Danielle Dishop* fixed a bug in the testing file
- *Danielle Dishop* with help from Colin, moved testing file back into correct directory and fixed import
- *colin seifer* added TypeAssign.py
- *colin seifer* separated dictionaries into class, phylum, kingdom
- *colin seifer* modified type assignment to assign into class first, then phylum, then kingdom
- *colin seifer* removed some test requirements since coding stats was moved to *danielle dishop*
- *colin seifer* removed some test requirements since battle calculations are out of the scope of this iteration
- *colin seifer* added battle calculations
- *colin seifer* added move dictionaries
- *colin seifer* added move class
- *colin seifer* added observation class
- *colin seifer* added backend battle system
- *colin seifer* fixed issues with battle calc, move class, observation class, and backend battle system
- *Danielle Dishop* added Undefined type stat generation in testing block (Undefined typed objects were already generating stats correctly by default)
- *Danielle Dishop* implemented better quality scores increasing the floor of the stat generation, including tests
- *Danielle Dishop* Added Leveling.py, with an automatic calculation of level from exp

###### TODO:
- *colin seifer* implement battle effects
- *colin seifer* work with *Cameron Miller* to implement front end for battle system


## Django

This is v1 of the Nature's RPG Django app. It has very limited functionality and is a work in progress.

Included is the actual project directory(natures-rpg/) along with two apps(frontend and backend).

To run, type "pip install -r requirements.txt" and then "python manage.py runserver"app.

Once this is done, you can visit http://127.0.0.1:8000/ to view the temporary home page or
http://127.0.0.1:8000/login to view the "login" page.