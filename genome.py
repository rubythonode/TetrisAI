# genome.py


import numpy as np
from random import choice


class Genome( object ):

    def __init__( self, generation ):
        self.identifier           = np.random.random( )
        self.weightRowsCleared    = 0
        self.weightMaxHeight      = 0
        self.weightSumHeight      = 0
        self.weightRelativeHeight = 0
        self.weightAmountHoles    = 0
        self.weightRoughness      = 0
        self.mutationRate         = 0.05
        self.mutationStep         = 0.2
        self.generation           = generation
        self.mum                  = None
        self.dad                  = None

    def __str__( self ):
        output  = '\n\nIdentifier: ' + str( self.identifier ) + '\nGeneration: ' + str( self.generation )
        output += '\nMum       : ' + str( self.mum )
        output += '\nDad       : ' + str( self.dad )
        output += '\n -weightRowsCleared    : ' + str( self.weightRowsCleared    )
        output += '\n -weightMaxHeight      : ' + str( self.weightMaxHeight      )
        output += '\n -weightSumHeight      : ' + str( self.weightSumHeight      )
        output += '\n -weightRelativeHeight : ' + str( self.weightRelativeHeight )
        output += '\n -weightAmountHoles    : ' + str( self.weightAmountHoles    )
        output += '\n -weightRoughness      : ' + str( self.weightRoughness      )
        return output + '\n\n'


    def initialGenome( self ):
        self.weightRowsCleared    = np.random.random( ) - 0.5
        self.weightMaxHeight      = np.random.random( ) - 0.5
        self.weightSumHeight      = np.random.random( ) - 0.5
        self.weightRelativeHeight = np.random.random( ) - 0.5
        self.weightAmountHoles    = np.random.random( ) - 0.5
        self.weightRoughness      = np.random.random( ) - 0.5

    def cross( self, mum, dad ):
        self.weightRowsCleared    = choice( [ mum.weightRowsCleared   , dad.weightRowsCleared    ] )
        self.weightMaxHeight      = choice( [ mum.weightMaxHeight     , dad.weightMaxHeight      ] )
        self.weightSumHeight      = choice( [ mum.weightSumHeight     , dad.weightSumHeight      ] )
        self.weightRelativeHeight = choice( [ mum.weightRelativeHeight, dad.weightRelativeHeight ] )
        self.weightAmountHoles    = choice( [ mum.weightAmountHoles   , dad.weightAmountHoles    ] )
        self.weightRoughness      = choice( [ mum.weightRoughness     , dad.weightRoughness      ] )
        self.mum                  = mum.identifier
        self.dad                  = dad.identifier

    def mutate( self ):
        if np.random.random( ) < self.mutationRate:
            self.weightRowsCleared    = self.weightRowsCleared   + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightMaxHeight      = self.weightMaxHeight     + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightSumHeight      = self.weightSumHeight     + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightRelativeHeight = self.weightRelativeHeight+ self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightAmountHoles    = self.weightAmountHoles   + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightRoughness      = self.weightRoughness     + self.mutationStep * ( 2 * np.random.random( ) - 1 )

    __repr__ = __str__