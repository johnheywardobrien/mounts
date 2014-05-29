#!/usr/bin/python

#executes external 'mount' command and parses output

import commands

mount = commands.getoutput('mount -v')
lines = mount.split('\n')
points = map(lambda line: line.split()[2], lines)

print points
