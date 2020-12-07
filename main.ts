input.onButtonPressed(Button.A, function () {
    throwToggle = !(throwToggle)
})
function _throw () {
    if (primed) {
        hummingbird.setPositionServo(FourPort.One, 0)
        basic.pause(1000)
        hummingbird.setPositionServo(FourPort.Two, 180)
        hummingbird.setPositionServo(FourPort.Three, 30)
        hummingbird.setPositionServo(FourPort.Four, 90)
        basic.pause(1000)
        hummingbird.setPositionServo(FourPort.Two, 160)
        hummingbird.setPositionServo(FourPort.Three, 180)
        basic.pause(175)
        hummingbird.setPositionServo(FourPort.Four, 30)
        basic.pause(1000)
        ready()
        primed = false
        basic.pause(500)
    } else {
        ready()
        basic.pause(1000)
        hummingbird.setPositionServo(FourPort.Four, 30)
        basic.pause(700)
        hummingbird.setPositionServo(FourPort.Four, 90)
        primed = true
    }
}
function ready () {
    hummingbird.setPositionServo(FourPort.One, 90)
    hummingbird.setPositionServo(FourPort.Two, 180)
    hummingbird.setPositionServo(FourPort.Three, 180)
    hummingbird.setPositionServo(FourPort.Four, 90)
}
let throwToggle = false
let primed = false
hummingbird.startHummingbird()
primed = false
throwToggle = false
ready()
basic.forever(function () {
    if (hummingbird.getSensor(SensorType.Distance, ThreePort.One) < 30 && throwToggle) {
        _throw()
    }
})
