"""
This file is part of sompy.

somply is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

sompy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with sompy. If not, see <http://www.gnu.org/licenses/>.
"""

from functools import reduce

# \brief This class represents a toolbox for self-organizing maps
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
class SOM:
    """This class represents a toolbox for self-organizing maps (SOM)"""

    # \param n n x n weight matrix
    # \param dimensions dimensions of weight vectors
    # \param fill initial fill function for values of weight vectors
    def __init__(self, n, dimensions, fill):
        self.matrix = self._weightmatrix(n, dimensions, fill)    

    # \brief time complexity: N^2 * D + N^2 * (D + 1) in O(N^2) 
    #        where N is amount of nodes, D is dimension.
    #
    # \param target target to train
    # \param rate learn rate
    # \param distance distance function
    # \param nf neighbourhood function 
    # \return trained weightmatrix
    def train(self, target, rate, distance, nf):  
        winner_node = self._winner(self.matrix, target, distance)
        self.matrix =\
            self._adjust_weights(\
            self.matrix, winner_node, target, rate, nf)    
    
    # \brief query the SOM with a given target
    # \param target query target vector
    # \param distance distance function
    # \return winner node tuple with i, j and distance
    def query(self, target, distance):
        return self._winner(self.matrix, target, distance)

    # \brief retrieve the weight matrix
    def get_matrix(self):
        return self.matrix

    # \brief time complexity: N^2 * D in O(N^2) 
    # \return [[]] n with dim-dimensional entries filled with fill.
    def _weightmatrix(self, n, dim, fill): 
        return [[[fill(i, j) for e in range(0, dim)] 
            for i in range(0, n)] 
            for j in range(0, n)]

    # \brief time complexity: D + 1 in O(D) where D is dimension of node.
    # \return adjusted weight vector
    def _adjust_weight(self, matrix, i, j, winner, target, rate, nf):
        factor = nf(winner[0], winner[1], i, j)
        return [matrix[i][j][c] + rate * factor * (target[c] - matrix[i][j][c])
            for c in range(0, len(matrix[i][j]))]

    # \brief time complexity: N^2 * (D + 1) in O(N^2), 
    #        N is number of node, D is dimension.
    #
    # \return adjusted weight matrix  
    def _adjust_weights(self, matrix, winner, target, rate, nf): 
        return [[self._adjust_weight(\
            matrix, i, j, winner, target, rate, nf)
            for j in range(0, len(matrix))]
            for i in range(0, len(matrix[0]))]

    # \brief time complexity: N^2 * D in O(N^2), N nodes in weightmatrix
    # \return (i, j, distance(value, target))
    def _winner(self, matrix, target, distance):
        return reduce(lambda x, y: x if x[2] < y[2] else y,  
            [(i, j, distance(matrix[i][j], target)) 
                for i in range(0, len(matrix))
                for j in range(0, len(matrix[0]))])

