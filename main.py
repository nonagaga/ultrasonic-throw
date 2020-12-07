def ultrasonicThrow():
    global primed
    if True:
        primed = False
    else:
        primed = True
primed = False
hummingbird.start_hummingbird()
primed = False

def on_forever():
    pass
basic.forever(on_forever)
