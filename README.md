# (Updated) Starter code - OpenClassrooms WPS | P3

This repository contains the work completed on chess club and tournament management program

Managements are independent front ends for same club/player data:
- `manage_clubs.py`
- `manage_tournaments.py`

### Data files

There are data files provided:
- JSON files for the chess clubs of Springfield and Cornville (`data/clubs/`)
- JSON files for two tournaments: one completed, and one in progress (`data/tournaments/`)

### Utils

This package contains helper functions for read/write list of tournament .json

### Models

This package contains the models used by the application:
* `Player` is a class that represents a chess player containing `name`,`email`,`chess_id`, and `birthday`
* `Club` is a class that represents a chess club (including `Players`)
* `ClubManager` is a manager class that allows to manage all clubs (and create new ones)
* `Tournament` is a class that represents the Tournament event
* `TournamentManager` is a manager that creates tournaments, manages state of in progress tournaments, sorts tournaments 
* `PlayerLookup` is a class that finds players chessid in clubs
* `Round` is a clas that represents the rounds system holding matchup information
* `Match` is a class that represetns the matchup system pairing players, set points winner, draw, lose, and matchup state for completed 

### Screens

This package contains classes that are used by the application to display information from the models on the screen.
Each screen returns a Command instance (= the action to be carried out).

* `MainMenu` is a class that represents Tournament MainMenu, displays in-order tournament list, prompts to create or view specific tournament 
* `Create` is a class that represetns Tournament Create, displays prompt to enter tournament information, data returns to TournamentCreateCmd
* `View` is a class that represetns specific Tournament View, displays specific tournament information, prompts for Tournament Actions
* `RegisterPlayer`is a class that represents Tournament player registration, displays prompt to register player by chessid from /data/clubs if player index match return data to TournamentRegisterPlayerCmd
* `AdvanceRound` is a class that represents Tournament advance rounds, displays specific tournament starting or advanceing, returns data to TournamentAdvanceRoundCmd
* `EnterResults` is a class that represents Tournament entry resuls, displays tournament and current round, sets player (1) and (2), prompts for results of matchup, returns data to TournamentEnterResultCmd
* `Report` is a class that represents Tournament Reports, displays tournament information, each round and matchup information, ordered ranks for players by points

### Commands

This package contains "commands" - instances of classes that are used to perform operations from the program.
They **must** define the `execute` method. When executed, a command returns a context.

* `ListTournaments` recieved oredered tournaments with progress state, 
* `CreateTournament` recieves tournament information, created tournament add to tournament manager list, return context screen to tournament specific view
* `RegisterPlayer` recieves specific tournament and player chessid for registrations, registers player in specific tournamen obj class
* `AdvanceRound` recieves specific tournament obj class starts/advances round
* `EnterResult` recieves specific tournament, specific matchup, to set winner, in tournament class obj


### Main application

The main application is controlled by `manage_clubs.py` for Club Management or `manage_tournaments.py` for Tournament Management. Based on the current Context instance, it instantiates the screens and runs them. The command returned by the screen is then executed to obtain the next context.

The main application is an infinite loop and stops when a context has the attribute `run` set to False.

### 🔧 System Requirements
- Operating System:
    - Windows: Windows10(64-bit) , Windows11(64-bit)
    - Mac(Min): MacOS 10.15 Catalina
    - Linux: any recent distributions compatible with python 3.14.4
- Ram: 
    - Recommended: 8 GB
- Network: 
    - Works Offline - local Storage
    - Works with any reliable internet 
- Space: 
    - project is about 40-42MB

### 📦 Download + Install + flake8 reports
To set up ChessManager, follow these steps:
1. create/set-up project venv 
2. git clone project repo
3. `pip install -r requirements.txt`
4. in terminal to run app `python manage_tournaments.py` 
5. in terminal to run flake8 linter `flake8 --format=html --htmldir=flake8_report`

## Key Features
- Create New Custom Tournaments, register players from existing clubs
- Manage Rounds and Matchups
- Generate Tournament Specific reports
- Point Based Ranking System in Tournaments
- Generated/Updated Tournament .json file 