import pyttsx3
engine = pyttsx3.init()
 
engine.say("I will speak the following text")
engine.say("this course is design to learn about the python and here you will find some of the awosome programs")
engine.say("now let's play Poem of the Twinkle Twikle")
engine.say(''' 
           Twinkle, Twinkle, Little Star

Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.

Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star,
How I wonder what you are!
           ''')
engine.say("that's, was all about the instalation of external module, and performing opertion on it.")
engine.runAndWait()
