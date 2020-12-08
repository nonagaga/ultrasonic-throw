def on_button_pressed_a():
    global throwToggle
    throwToggle = not (throwToggle)
input.on_button_pressed(Button.A, on_button_pressed_a)

def _throw():
    global primed
    if primed:
        hummingbird.set_position_servo(FourPort.ONE, 0)
        basic.pause(1000)
        hummingbird.set_position_servo(FourPort.TWO, 180)
        hummingbird.set_position_servo(FourPort.THREE, 30)
        hummingbird.set_position_servo(FourPort.FOUR, 90)
        basic.pause(1000)
        hummingbird.set_position_servo(FourPort.TWO, 160)
        hummingbird.set_position_servo(FourPort.THREE, 180)
        basic.pause(175)
        hummingbird.set_position_servo(FourPort.FOUR, 30)
        basic.pause(1000)
        ready()
        primed = False
        basic.pause(500)
    else:
        ready()
        basic.pause(1000)
        hummingbird.set_position_servo(FourPort.FOUR, 30)
        basic.pause(700)
        hummingbird.set_position_servo(FourPort.FOUR, 90)
        primed = True
def ready():
    hummingbird.set_position_servo(FourPort.ONE, 90)
    hummingbird.set_position_servo(FourPort.TWO, 180)
    hummingbird.set_position_servo(FourPort.THREE, 180)
    hummingbird.set_position_servo(FourPort.FOUR, 90)
throwToggle = False
primed = False
hummingbird.start_hummingbird()
primed = False
throwToggle = False
basic.clear_screen()
ready()

def on_forever():
    if hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) < 30 and throwToggle:
        _throw()
    if throwToggle:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
