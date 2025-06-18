import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

# Matrix
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)  # 6 rows
keyboard.col_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
                     board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
                     board.GP18, board.GP19, board.GP20, board.GP21)  # 16 cols
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB LED Chain
rgb = RGB(pixel_pin=board.GP30, num_pixels=84, val_limit=100)
keyboard.modules.append(rgb)

# Rotary Encoder
encoders = EncoderHandler()
encoders.pins = ((board.GP24, board.GP25, board.GP26),)  
encoders.map = [
    ((KC.BRIU, KC.BRID, KC.MUTE),),
]
keyboard.modules.append(encoders)

# keymap
keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.NO, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NO, KC.NO, KC.NO,
     KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.INSERT, KC.HOME, KC.PGUP,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE, KC.END, KC.PGDOWN,
     KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.NO ,KC.QUOTE, KC.ENTER, KC.NO, KC.NO, KC.NO,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.RSHIFT, KC.NO, KC.NO, KC.UP, KC.NO,
     KC.LCTRL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RGUI, KC.NO, KC.MENU, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
     ]
]

rgb = RGB(
    pixel_pin=board.GP30,
    num_pixels=84,
    val_limit=100,
    animation_mode=2  # 2 = Rainbow Swirl, 1 = Solid Color, etc.
)

if __name__ == '__main__':
    keyboard.go()
