# Demonstration of coroutines.
#
# This example enables us to keep a running tally that can be increased by
# arbitrary values.
#
# The difference between a generator and a coroutine, is that a generator only
# produces values, while a coroutine can also consume values.
#
# A coroutine enables data to be passed in and out at the point where the
# yield statement is executed.


def tally():
    score = 0
    while True:
        # The yield statement causes the coroutine to pause. When send() is
        # called from outside it advances the coroutine (similar to next()),
        # but also allows you to pass in a value that is assigned to the left
        # side of the yield statement. The yield statement returns the value of
        # score when next() or send() is called.
        increment = yield score
        score += increment


# This simple function object can be used by a scoring application for a
# baseball team. Separate tallies could be kept for each team, and their score
# could be incremented by the number of runs accumulated a the end of every
# half-inning.
white_sox = tally()
blue_jays = tally()

# The next() statement causes the coroutine to run until it hits yield. The
# next() function can be replicated by calling i.send(None).
print('next(white_sox) = {}'.format(next(white_sox)))
print('next(blue_jays) = {}'.format(next(blue_jays)))

# The send() statement advances the coroutine and sends in a value which
# is assigned to the left side of the yield statement. The coroutine continues
# processing until it encounters another yield statement.
print('white_sox.send(3) = {}'.format(white_sox.send(3)))
print('blue_jays.send(2) = {}'.format(blue_jays.send(2)))
print('white_sox.send(2) = {}'.format(white_sox.send(2)))
print('blue_lays.send(4) = {}'.format(blue_jays.send(4)))
