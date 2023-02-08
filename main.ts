input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    rope += -0.1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    rope += 0.1
})
let rope = 2
basic.forever(function on_forever() {
    basic.clearScreen()
    led.plot(Math.round(rope), 2)
    if (rope < 0) {
        basic.showString("A wins")
    } else if (rope > 4) {
        basic.showString("B wins")
    }
    
})
