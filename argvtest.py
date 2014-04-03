from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like pie, %s?" % user_name
likes = raw_input(prompt)

print "What do you do for work, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r to liking pie.
You are a %r for a living.  Not sure what that is. Sounds hard.
And you have a %r computer.  Nice. 
""" % (likes, lives, computer)