https://realpython.com/python-wordle-clone/

https://pypi.org/project/rich/

This project is based on the tutorial by Geir Arne Hjelle and found here: https://realpython.com/python-wordle-clone/

What I've added:

- Development in a Docker container
- Restart the main project on save
- From the Gutenberg Library I call and comple a word list from the The Advebtures of Sherlock Holmes.

There will be another game based on the 1970's Mastermind board game:
https://en.wikipedia.org/wiki/Mastermind_(board_game)

## Install and Run Requirments

You will need Docker or Docker Desk Top running

After cloning this project locally open a terminal in the projects root.

_I use a `makefile` to make life easier, you can copy and paste the instrutions from this file if Maker is not
installed._

### List of commands

`make build` - Build a docker image with docker-compose

`make dev` - Will run the container

`make terminal` - Will open a terminal in to contaner at the corroct location

`make api` - Will generate a word list based on the Adventures Of Sherlock Holmes

`make run` - Will run the Wyrdl clone and restart if there are any changes to the main file `wyrdl.py`

### Example build and run steps

Example, In your console and at the projects root type each of these:

```
make build

make dev

make terminal
```

At this stage the terminal should be open at `/app` inside the container

```
make api

make run
```

Enjoy
