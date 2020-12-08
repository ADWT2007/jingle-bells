def on_button_pressed_a():
    for index in range(1):
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    for index2 in range(1):
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
    for index3 in range(1):
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
    for index4 in range(1):
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    for index5 in range(1):
        break
    for index6 in range(1):
        music.play_tone(392, music.beat(BeatFraction.DOUBLE))
    for index7 in range(1):
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    for index8 in range(1):
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    for index9 in range(1):
        break
    for index10 in range(1):
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    for index11 in range(1):
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
    for index12 in range(1):
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
    for index13 in range(1):
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    for index14 in range(1):
        break
    for index15 in range(1):
        music.play_tone(440, music.beat(BeatFraction.BREVE))
    for index16 in range(1):
        break
    for index17 in range(1):
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
    for index18 in range(1):
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
    for index19 in range(1):
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
    for index20 in range(1):
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
    for index21 in range(1):
        break
    for index22 in range(1):
        music.play_tone(494, music.beat(BeatFraction.BREVE))
    for index23 in range(1):
        break
    for index24 in range(1):
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
    for index25 in range(1):
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
    for index26 in range(1):
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
    for index27 in range(1):
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
    for index28 in range(1):
        break
    for index29 in range(1):
        music.play_tone(659, music.beat(BeatFraction.BREVE))
    for index30 in range(1):
        break
    for index31 in range(1):
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    for index32 in range(1):
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
    for index33 in range(1):
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
    for index34 in range(1):
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    for index35 in range(1):
        break
    for index36 in range(1):
        music.play_tone(392, music.beat(BeatFraction.BREVE))
    for index37 in range(1):
        break
    for index38 in range(1):
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    for index39 in range(1):
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
    for index40 in range(1):
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
    for index41 in range(1):
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    for index42 in range(1):
        break
    for index43 in range(1):
        music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    for index44 in range(1):
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
    for index45 in range(1):
        break
    for index46 in range(1):
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
    for index47 in range(1):
        break
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        . . # . .
        . # # # .
        . # # # .
        # # # # #
        # # # # #
        """)
basic.forever(on_forever)
