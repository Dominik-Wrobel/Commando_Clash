# Commando_Clash
This is my coursework for Computer Science A-Level. A 2D fighter called "Commando Clash".

By running "main.py" you should be able to run the game.
Make sure you have the pygame package installed by running "pip install pygame" in the terminal.

Apologies for the crappy GUI and very buggy hitboxes; I probably will not be fixing this.
This game has really tested my experience with python and especially pygame.
To be honest, the pygame set of modules is really hard to work with, due to the lack of commands you can use, and how it is a little buggy.

An example of this: comboes.
I tried to make it so that the character would rotate a small amount each time they got hit until they turn 90 degrees clockwise, which would then give them immunity and let them escape the combo.
Instead what it has done, is every time the character rotates, their hitbox slowly gets bigger, and bigger, and bigger, until their hitbox becomes bigger than the map itself. This is really annoying and due to the lack of time (my deadline for submitting the game was approaching), I focused on other aspects of the game which I am actually proud of.
For example, I managed to make it so that you can use as many controllers as you want to play the game, both characters can use the same keyboard (not different keyboards unfortunately). I created this using time that would have otherwise been spent trying to fix the "rotabox bug", as we'll call it.

I added a Basic Attack, Heavy Attack, and each character has their own unqiue "Special Attack" which consumes a part of the gauge at the bottom.
I REALLY wanted to add an "Ultimate Attack", but was unable to due to time constraints. "Etai" (the fire character in the game) was supposed to have a giant fire attack that stretched the whole arena, which I was SUPER excited to do, but python really hates it when you try to do ANYTHING, so I left it.

"Tane" (the speedster) has a cool dash special attack which I am pretty proud of, so we'll leave it at that.

Was also going to add music, a way to fill up the gauge, a way to leave the game mid-match, a way to change your controls, fix all the bugs, improve the quality of maps and characters, add more characters, but couldn't due to time constraints as well as pygame limitations.


I am currently learning C# so I can code games in Unity - I have made a couple so far which I will share at some point.
As simple as pygame was, once I got used to it, it became harder to perform more complex game mechanics. However I managed to figure out how to make characters jump, which I am really proud of.

I advise that you do NOT use this for your own computer science projects as you WILL be penalised for it. If you need it for anything else or to look at how I did certain things, be my guest. I may add more code-comments in the future to explain what my thought process was for certain elements of the code, but for now I am just keeping this as a way to look back at what I managed to do.

Enjoy!
