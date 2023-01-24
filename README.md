# Dungeons, Dice, & Danger Calculator

I wrote this little program to help crunch numbers for the game Dungeons, Dice & Danger by Richard Garfield.

https://boardgamegeek.com/boardgame/349463/dungeons-dice-danger

## The Game Mechanics

The base mechanics of the game involve every turn rolling five six-sided dice and trying to add the results together into two pairs you use during the game to move around and achieve objectives. Only four of the five dice are usually available at a time - the fifth "black" die is under the control of the "active player" of that round, though you can spend limited resources to also gain access to the fifth die if you would benefit from the option.

### Example

Let's presume the five dice might come up (1, 3, 6, 5 | 5)

You could pair the 1 and 3, and the 6 and 5 to have the numbers 4 and 11, you could pair the 3 and 6, and the 1 and 5 to produce 9 and 6, and so on. If you're able to use the black die, perhaps you could pair both 5s because you need a 10, or a double (both die the same value).

I've always had an intuitive eye for probability in games, but in this game things get tricky. Some of my friends aren't proficient at this game find themselves holding their breath for a 12 like it's bound to happen quickly. If we were only rolling 2d6 I could clearly demonstrate the odds as 1/36. But with four (five?) dice in the mix, things get complicated.

## How This Program Works

To activate the program, simply run the code.

This calculator as it stands simply asks the question, "If I am really desperate to end up with a certain number, what are my chances of being able to make that number one of my two pairs for the turn?"

For instance, if I badly need the number 8 to progress me past a choke point, of all the possible ways that 4d6 can land, you are capable of making an 8 at 56.1% (727 out of 1296 possible throws)

Rolling 5d6 (I'm willing to pay for the use of a black die or I'm the active player) that shoots up to 72.35% (5626 times out of 7776).

Really shows how impactful that fifth die us, huh?

### Doubles and exact doubles

At the bottom of both sets of calculations are the chance to make any pair of "doubles" - 1 and 1, 2 and 2, so on, which sometimes come up in the game. What interested me is that, with 2d6, the chances of doubles are the same as the chances of a 7 - 6/36 or 1 in 6 chance. You'll see that in four dice it's noticeably more likely, and with five it's near guaranteed. THis confused me for a moment until I realized what I was looking at what a simplified version of the Birthday Problem. https://en.wikipedia.org/wiki/Birthday_problem

Keep in mind however, if you need exact doubles (like a 4 made out of 2 and 2), which is a feature of the very first game map, that has the exact same likelihood as a 2 or 12 in the calculator (13.19% on four dice, 19.62% on five).


## Limitations and Future Features

For now this program only tells you what ONE of your pairs will be, but in this game it's extremely important to get value out of both rolls every turn. As it stands this program will not tell you what you're likely to be left with. This is a feature I'd like to add at some point, but I lack the gumption to do it right away. For now, use your imagination (if you're looking for an 11, the chances are high your partner is going to be a lower number).

## Conclusion

Thanks for checking this out. If you have any ideas, suggestions, or feedback, you can reach me at geo.c.blanchard@gmail.com
