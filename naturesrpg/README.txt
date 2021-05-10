This is v2 of the Nature's RPG Django app.

Included is the actual project directory(natures-rpg/) along with the backend app

To run, type "pip install -r requirements.txt" and then "python manage.py runserver".

Here is a breakdown of the API calls possible through this Django app:
players/
 - Can get all players registered
 - Create new players with necessary info

players/number/
 - Access a certain player based on a numerical id

obs/number
 - Access all of the observations of a certain player based on their id

obs/number/number/
 - Access a certain observation of a certain player based on the id's of the player and observation

The database has two tables: Player and Observation. 

The Player table has the following fields:
- iNat_user_id: the user id of the player's iNaturalist account
- username: the username of the player's iNaturalist account
- num_of_obs: the number of observations associated with the player's iNaturalist account
- team: a JSON that holds the observations chosen by the player to be used in battle

The Observation table holds the iNaturalist information of the observation(taxa, id, name, etc.), its stats and moves for battle,
and a Player object tied to it as a foreign key.

