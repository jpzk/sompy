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

# \brief time complexity: O(1)
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
# \return mexican hat function value
def mexican_hat(i1, j1, i2, j2, sigma):
    return math.exp(-((abs(i1 - i2) + abs(j1 - j2)) ** 2)/(2 * (sigma ** 2)))

# \brief partial application, time complexity: O(1)
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
# \return mexican hat function value
def mexican_hat_with_sigma(sigma):
    return lambda i1, j1, i2, j2 :\
        math.exp(-((abs(i1 - i2) + abs(j1 -j2) ** 2)/(2 * (sigma **2))))
        
