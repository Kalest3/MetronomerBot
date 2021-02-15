# MetronomerBot
A Bot that likes to play Metronome Battle in Pokémon Showdown.

Discord: Kaleste#6280 || Pokémon Showdown Nick: Gabriel Gottapok

if you want contribute to MetronomerBot, you can start by adding new teams:

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

## Running


If you want to use the bot, you must have installed Python version 3.7.7 (since this was the version that MetronomerBot was builded). The bot was not tested on different Python version.

If you already have Python installed, you can now use the bot.

- First, run
```bash
pip install -r requirements.txt
```

You will now have the packages needed for the bot to work.

- Create a file with the name "config.json".
- Copy what's in "config_example.json" to "config.json"
- Inside config.json, in place of My_Username, put the username you want to run the bot code. In My_Password, the password. And My_Avatar, the avatar in PS. In Owner_Username, your username. Save the config.json.
- To finish, run
```bash
python run.py
```

And the bot is working!

## Commands

| Command | Do |
| ------- | --- |
| @spheal | Return "spheal" |
| ------- | ------------------------------------------------------------- |
| @commands | Return the link that contains this table you are viewing xD |
## Bugs/Features

If you want to report a bug that happened during a MetronomerBot battle, contact me on PS (my username is Gabriel Gottapok) or on my Discord (Kaleste#6280).
The same goes for new features that you would like to see in the bot.

Feel free if you also want to contribute to Metronomer by fixing bugs!