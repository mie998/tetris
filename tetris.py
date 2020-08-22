#!/usr/bin/python3
import pyxel
from random import randint

BLOCK_SIZE = 8
CANVAS_WIDTH = 14
CANVAS_HEIGHT = 20
FIELD_WIDTH = 10
FIELD_HEIGHT = 18
BOUND_LEFT = 2
BOUND_RIGHT = BOUND_LEFT + FIELD_WIDTH
BOUND_DOWN = CANVAS_HEIGHT - 1 
INITIAL_MINO_POS_X = 40
INITIAL_MINO_POS_Y = 0
YELLOW_POS_X, YELLOW_POS_Y = 25, 0
YELLOW_WIDTH, YELLOW_HEIGHT = 2, 2
RED_POS_X, RED_POS_Y = 28, 0
RED_WIDTH, RED_HEIGHT = 3, 2
BLUE_POS_X, BLUE_POS_Y = 32, 0
BLUE_WIDTH, BLUE_HEIGHT = 3, 2
PINK_POS_X, PINK_POS_Y = 37, 0
PINK_WIDTH, PINK_HEIGHT = 1, 4
GREEN_POS_X, GREEN_POS_Y = 25, 3
GREEN_WIDTH, GREEN_HEIGHT = 3, 2
PURPLE_POS_X, PURPLE_POS_Y = 29, 3
PURPLE_WIDTH, PURPLE_HEIGHT = 3, 2
BROWN_POS_X, BROWN_POS_Y = 33, 3
BROWN_WIDTH, BROWN_HEIGHT = 3, 2


class Tetris:
    def __init__(self):
        pyxel.init(CANVAS_WIDTH * BLOCK_SIZE, CANVAS_HEIGHT *
                   BLOCK_SIZE, caption="Tetris!", fps=10)
        pyxel.load("tetris.pyxres")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.is_active = False
        self.mino_x, self.mino_y = 0, 0
        self.mino_v = BLOCK_SIZE
        self.rand = 1
        self.timer = 0
        self.is_empty = [[True for _ in range(FIELD_HEIGHT)] for _ in range(FIELD_WIDTH)]

    def update(self):
        self.timer += 1
        self.update_mino()

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.reset()

        # if not self.moving_block:
            # generate_block()

    def update_mino(self):
        if self.is_active:
            # needed: immediate drop
            if pyxel.btn(pyxel.KEY_W):
                pass
            elif pyxel.btn(pyxel.KEY_S):
                if self.check_field(self.mino_x, self.mino_y + BLOCK_SIZE):
                    self.mino_y += BLOCK_SIZE
            elif pyxel.btn(pyxel.KEY_A):
                if self.check_field(self.mino_x - BLOCK_SIZE, self.mino_y):
                    self.mino_x -= BLOCK_SIZE 
            elif pyxel.btn(pyxel.KEY_D):
                if self.check_field(self.mino_x + BLOCK_SIZE, self.mino_y):
                    self.mino_x += BLOCK_SIZE

            if self.timer % 5 == 0 and self.check_field(self.mino_x, self.mino_y + self.mino_v):
                self.mino_y += self.mino_v

        else:
            self.generate_new_mino()

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
        self.draw_mino()

    def draw_mino(self):
        if self.rand == 1:
            pyxel.bltm(self.mino_x,self.mino_y,0,RED_POS_X,RED_POS_Y,RED_WIDTH, RED_HEIGHT)
        elif self.rand == 2:
            pyxel.bltm(self.mino_x,self.mino_y,0,BLUE_POS_X,BLUE_POS_Y,BLUE_WIDTH, BLUE_HEIGHT)
        elif self.rand == 3:
            pyxel.bltm(self.mino_x,self.mino_y,0,GREEN_POS_X,GREEN_POS_Y,GREEN_WIDTH, GREEN_HEIGHT)
        elif self.rand == 4:
            pyxel.bltm(self.mino_x,self.mino_y,0,PINK_POS_X,PINK_POS_Y,PINK_WIDTH, PINK_HEIGHT)
        elif self.rand == 5:
            pyxel.bltm(self.mino_x,self.mino_y,0,BROWN_POS_X,BROWN_POS_Y,BROWN_WIDTH, BROWN_HEIGHT)
        elif self.rand == 6:
            pyxel.bltm(self.mino_x,self.mino_y,0,YELLOW_POS_X,YELLOW_POS_Y,YELLOW_WIDTH, YELLOW_HEIGHT)
        else:
            pyxel.bltm(self.mino_x,self.mino_y,0,PURPLE_POS_X,PURPLE_POS_Y,PURPLE_WIDTH, PURPLE_HEIGHT)

    def generate_new_mino(self):
        self.rand = randint(1, 7)
        self.is_active = True
        self.mino_x = INITIAL_MINO_POS_X
        self.mino_y = INITIAL_MINO_POS_Y
        self.mino_v = BLOCK_SIZE
        if self.rand == 1: # red
            self.mino_width, self.mino_height = RED_WIDTH, RED_HEIGHT
        elif self.rand == 2: # blue
            self.mino_width, self.mino_height = BLUE_WIDTH, BLUE_HEIGHT
        elif self.rand == 3: # green 
            self.mino_width, self.mino_height = GREEN_WIDTH, GREEN_HEIGHT
        elif self.rand == 4: # pink
            self.mino_width, self.mino_height = PINK_WIDTH, PINK_HEIGHT
        elif self.rand == 5: # brown
            self.mino_width, self.mino_height = BROWN_WIDTH, BROWN_HEIGHT
        elif self.rand == 6: # yellow
            self.mino_width, self.mino_height = YELLOW_WIDTH, YELLOW_HEIGHT
        else: # purple
            self.mino_width, self.mino_height = PURPLE_WIDTH, PURPLE_HEIGHT


    def check_field(self, x, y):
        lx = x // BLOCK_SIZE
        rx = lx + self.mino_width
        uy = y // BLOCK_SIZE
        dy = uy + self.mino_height
        print(dy)

        if (BOUND_LEFT <= lx and rx <= BOUND_RIGHT
            and 0 <= uy and dy <= BOUND_DOWN
        ):
            ## empty judge
            for i in range(lx - 2, rx - 2):
                for j in range(uy -1, dy-1):
                    if not self.is_empty[i][j]:
                        return False
            return True
        else: 
            return False


Tetris()
