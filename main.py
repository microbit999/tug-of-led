def on_button_pressed_a():
    global rope
    rope += -0.1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global rope
    rope += 0.1
input.on_button_pressed(Button.B, on_button_pressed_b)

rope = 2

def on_forever():
    basic.clear_screen()
    led.plot(Math.round(rope), 2)
    if rope < 0:
        basic.show_string("A wins")
    elif rope > 4:
        basic.show_string("B wins")
basic.forever(on_forever)
