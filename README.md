Sources:
https://www.montyhallproblem.com/
https://en.wikipedia.org/wiki/Monty_Hall_problem

The Montly Hall problem is based on a game show in which contestants have a chance to win prizes
hidden behind curtains/doors/etc. They do not know which of the three curtains contains the prize.
Contestants are allowed to make an initial guess, at which point one of the other two curtains is revealed
to not contain the prize. At this point, the contestant is offered the choice to change curtains or remain
will their initial guess. What is the choice with the higher chance of success?

This problem initially appears trivial - two options, one win condition, the chance must be the same for both!
However, there was a 1/3 chance the prize was behind the chosen curtain, and a 2/3 chance the prize was behind
a non-chosen curtain. Since one of those two curtains was opened, there is now a 2/3 chance that the remaining
curtain holds the prize.

This is somewhat counterintuitive, and I personally did not feel fully satisfied with theoretical reasoning alone.
This program simulates the monty hall problem and randmizes which curtain the prize is behind. The first pick is and
decision to switch/stay is also randomized. Should the logic hold, the decision to switch should result in a rate of
success approximately double that of the decision to stay.

Usage: py monty_hall.py