# viewController.py


import pygame as gui


class ViewController( object ):

    rd = ( 249,  35,  56 )
    pk = ( 201, 115, 255 )
    bl = (  28, 118, 188 )
    yw = ( 254, 227,  86 )
    gn = (  83, 213,   4 )
    cy = (  54, 224, 255 )
    og = ( 248, 147,  29 )
    dk = (  39,  40,  33 )
    lg = ( 112, 108,  90 )

    def __init__( self ):

        gui.init( )
        self.screen = gui.display.set_mode( ( 800,700 ) )

        self.abort = False

        self.static = gui.Surface( ( 800, 700 ) )
        self.static.set_colorkey( ( 0, 0, 0 ) )
        for i in range(10):
            gui.draw.line(self.static, self.lg, ( 30*i+50, 50 ), ( 30*i+50, 650 ) )
            gui.draw.line(self.static, self.lg, ( 50, 30*i+50 ), ( 350, 30*i+50 ) )
            gui.draw.line(self.static, self.lg, ( 50, 30*i+380 ), ( 350, 30*i+380 ) )
        gui.draw.line(self.static, self.lg, ( 350, 50 ), ( 350, 650 ) )
        gui.draw.line(self.static, self.lg, ( 50, 350 ), ( 350, 350 ) )

    def eventCheck( self ):
        for event in gui.event.get( ):
            if event.type == gui.QUIT:
                self.abort = True
            if event.type == gui.KEYDOWN:
                if event.key == gui.K_ESCAPE:
                    gui.event.post( gui.event.Event( gui.QUIT ) )

    def update( self ):
        self.screen.fill( self.dk )
        self.screen.blit( self.static, ( 0, 0 ) )
        gui.display.flip()
