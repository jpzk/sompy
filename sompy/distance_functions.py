"""
This file is part of sompy.

hclu is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

hclu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with sompy. If not, see <http://www.gnu.org/licenses/>.
"""

import math

# \brief euclidean distance time complexity: O(N), N is dimension of x,y.
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
# \return euclidean distance
def euclidean(x, y): 
    return math.sqrt(reduce(lambda x, y: x + y, 
        [(xi - yi) ** 2 for (xi, yi) in zip(x, y)]))

# \brief manhatten distance also known as city-block metric or
#        mannheimer metric. time complexity: O(N), N is dimension of x,y.
#
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
# \return manhatten distance
def manhatten(x, y):
    return reduce(lambda x, y: x + y, 
        [abs(xi - yi) for (xi, yi) in zip(x, y)])

# \brief maximum distance. time complexity: O(N), N is dimension of x,y.
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
# \return maximum distance
def maximum(x, y):
    return reduce(lambda d1, d2: d1 if d1 < d2 else d2,
        [abs(xi - yi) for (xi, yi) in zip(x, y)])
