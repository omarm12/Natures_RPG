# Natures_RPG

## Dependencies
- python3
- node package manager

## Running Tests
- Danielle Dishop* From Linux/Unix terminal, navigate to parent directory of Natures_RPG and run <code>python -m unittest Natures_RPG/test/statTest.py</code>
- Colin Seifer* from Linux/Unix terminal, navigate to parent directory of Natures_RPG and run <code>python3 -m Natures_RPG.test.cstest</code>

###### Changelog:
- Danielle Dishop* added Stats class to TypeAssign
- Danielle Dishop* fixed the mod stat dictionary to be the correct stats
- Danielle Dishop* moved Stats class into its own file per Colin's request and added testing for Stat assignment
- Danielle Dishop* fixed a bug in the testing file
- Danielle Dishop* with help from Colin, moved testing file back into correct directory and fixed import
- colin seifer* added TypeAssign.py
- colin seifer* separated dictionaries into class, phylum, kingdom
- colin seifer* modified type assignment to assign into class first, then phylum, then kingdom
- colin seifer* removed some test requirements since coding stats was moved to *danielle dishop*
- colin seifer* removed some test requirements since battle calculations are out of the scope of this iteration

## Placeholder UI

This UI is used to test displaying content from the iNaturalist API

You can view the current build of the website [Click Me](https://raw.githack.com/omarm12/Natures_RPG/develop/placeholder_ui/build/index.html)

Add an html parameter to specify the user to be shown. 
For example, [example](https://raw.githack.com/omarm12/Natures_RPG/develop/placeholder_ui/build/index.html?username=kai_vilbig)


## Testing the UI

Install node package manager

While in the placeholder_ui directory, run the command <code>npm install</code>

Then, to start testing, run <code>npm test</code>
