# snakeAI
Using genetic algorithms to make the ai smarter. the snake game repository has all the code for the basic game.
Sit back and watch your AI become smarter and smarter. Genetic algorithms in action


As shown in the image, the snake can sense 8 directions from it's head,
From each of the directions, the snake can either see an apple, itself or a wall.

Since we want our snake to get to the apple, we will set the value of the direction where the apple is to +1
and obviously, we don't want our snake to run into a wall or itself so we will set the value of these directions to -1
that makes the snake realise that getting to a treat is good and running into itself or a wall is bad.

To start off, we make a "batch" or a generation of snakes that have random brains. we let this generation of snakes play the game one by one and then note the score of each snake in the generation. since we are making them randonly, they might understand what the game is or they might even be so dumb that they want to run into a wall or themselves.


The Genetic Algorithm :


From this "batch" or generation, we take the smartest snakes which will be the top 25% in the scores and we use them again in the next generation too. now, these snakes might be good, but they won't be perfect for sure. that is why we also tweak some values in these smart snakes to try and make them even smarter(this is called mutation) and add hem  to our next generation too which will play the game again.
now, we have 50% of the next generation ready, the other 50% we will make randomly with the hope of getting even smarter snakes than our top 25% and their mutations from the last generation.

We keep repeating this procedure until we see a snake which knows that running into walls and itself is bad but if an apple is near a wall, it should go towards the apple and then turn so as to not die

And there you have it, the snakes have also learned "an apple a day keeps a doctor away".
