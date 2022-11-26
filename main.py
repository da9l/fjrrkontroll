radio.set_group(1337)
def remote_on_forever():
    pass
def receiver_on_forever():
    pass
def on_button_pressed_a_setupremote():
    basic.forever(remote_on_forever)
    input.on_button_pressed
input.on_button_pressed(Button.A, on_button_pressed_a)
basic.forever(remote_on_forever)
