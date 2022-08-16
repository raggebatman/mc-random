# mc-util

*Easily randomise resource/datapacks for Minecraft*

## Purpose

The main purpose of this software is enabling users to easily and "dynamically" generate resource packs and/or data packs for Minecraft. 
This includes randomising assets to create unique experiences.

My plan is for it to be highly configurable. I might distribute executables in the future when everything is done, especially if I make a GUI.

## Setup

I recommend creating a virtual environment rather than installing all the dependencies on your system directly. 

### Instructions for Unix (and the like)

1. `git clone https://github.com/raggebatman/mc-util`

2. `cd mc-util`

3. `python3 -m venv .venv`

4. `source .venv/bin/activate`

5. `python3 -m pip install -r requirements.txt`

### Instructions for Windows

1. `git clone https://github.com/raggebatman/mc-util`

2. `cd mc-util`

3. `py -m venv .venv`

4. `.venv/Scripts/activate`

5. `py -m pip install -r requirements.txt`

Once this is done, simply run `deactivate` to exit the virtual environment. If you want to enter it again, repeat step 4.

The use of the name ".venv" is entirely arbitrary. However, note that you should gitignore said directory when committing.

These instructions are prone to change. If they do not work, I urge you to take a look at [venv](https://docs.python.org/3/library/venv.html) and [installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/).

## Usage

TODO

By default, terminal output is silent in order to have a nicer experience with scripting and imports.

## Licensing

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.