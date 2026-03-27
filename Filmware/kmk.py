from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, MatrixScanner
from kmk.modules.rotary import RotaryEncoder
from kmk.extensions.media_keys import MediaKeys

import board

keyboard = KMKKeyboard()


cols = [board.GP15, board.GP16, board.GP17]
rows = [board.GP13, board.GP12, board.GP11]

scanner = MatrixScanner(
    row_pins=rows,
    col_pins=cols,
    diode_orientation=DiodeOrientation.COL2ROW
)
keyboard.modules.append(scanner)

keyboard.extensions.append(MediaKeys())


encoder = RotaryEncoder(
    pins=(board.GP26, board.GP27),
    clockwise=KC.VOLU,
    counter_clockwise=KC.VOLD,
    button=board.GP28,
    button_key=KC.ENTER
)
keyboard.modules.append(encoder)

keyboard.keymap = [
    [
        [KC.A, KC.B, KC.C],    # ROW1 (GP13)
        [KC.D, KC.E, KC.F],    # ROW2 (GP12)
        [KC.G, KC.H, KC.I],    # ROW3 (GP11)
    ]
]

if __name__ == '__main__':
    keyboard.go()