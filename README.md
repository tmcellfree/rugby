###################################################################
# Script to calculate trys/conversions/penalties from a rugby match
###################################################################

###################################################################
### In rugby, joining a game late makes it tough to tell wha the 'type' of scores happened

###There is a rugby equation to solve this problem!
### 5x + 7y + 3z = score
###where x = unconverted tries, y = converted tries, z = penalties (or drop goals), score = user input
###x, y, z, score are positive integers
###################################################################

###Using this script you just enter your score and it will tell you the possible combinations! 

###Since there are three different score types it is interesting to look at the possible combinations of scores available for each score:

![Combinations and scores](https://github.com/tmcellfree/rugby/blob/master/rugby_scores.png "Combinations of Tries/Converted/Penalty vs. Score")

<dl>
  <dt>How to use this script</dt>
</dl>

Just Type 
`git clone https://github.com/tmcellfree/rugby.git`

`cd rugby`

`python rugby_scores.py`

Then you should see somthing like: 

```Enter the score: 30
The score is: 30
Trying... 385 permutations
Converted Tries: 0 Tries: 6 Penalties: (or Drop Goals): 0
Converted Tries: 1 Tries: 4 Penalties: (or Drop Goals): 1
Converted Tries: 2 Tries: 2 Penalties: (or Drop Goals): 2
Converted Tries: 3 Tries: 0 Penalties: (or Drop Goals): 3
Converted Tries: 0 Tries: 3 Penalties: (or Drop Goals): 5
Converted Tries: 1 Tries: 1 Penalties: (or Drop Goals): 6
Converted Tries: 0 Tries: 0 Penalties: (or Drop Goals): 10
Total of 7 possible combinations!
Enjoy the game!```
