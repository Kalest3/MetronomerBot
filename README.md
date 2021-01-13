# MetronomerBot
A Bot that likes to play Metronome Battle in Pokémon Showdown.

Discord: Kaleste#6280 || Pokémon Showdown Nick: Gabriel Gottapok



if you want  contribute to MetronomerBot, you can start by adding new teams;

However, before starting, you must have installed Python version 3.7.7 (since this was the version that MetronomerBot was builded). 
The bot was not tested on different Python version.

You may already be able to edit the code, as long that you have the forked repository, and have cloned it.


## Teams

- The teams are in the "teams.py" file.
- You will see that in the code of this file, there will be only one variable containing a list of teams.
- Teams are separated by commas.

To add a new team, first open your text/code editor, and skip ONE line of code after the last comma. That done, put three double quotes and paste your team.
In the last line of your team (which will probably be written "- Metronome"), put three double quotes again and a comma. Save your file and send a Pull Request!

You will see the code like this:

```python
teams = [
"""Pokemon1 @ YourItem  
Ability: Friend Guard  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Naive Nature  
- Metronome  

Pokemon2 @ YourItem  
Ability: Friend Guard  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Naive Nature  
- Metronome  """, #The next line is skipped because of the comma

"""Pokemon1 @ YourItem  
Ability: Prsim Armor  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Naive Nature  
- Metronome  

Pokemon2 @ YourItem  
Ability: Prism Armor  
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe  
Naive Nature  
- Metronome  """, 
]
```