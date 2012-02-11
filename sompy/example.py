"""
This file is part of sompy.

sompy is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

sompy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with sompy. If not, see <http://www.gnu.org/licenses/>.
"""

import random

from som import SOM
from distance_functions import euclidean
from neighbourhood_functions import mexican_hat_with_sigma
from fill_functions import random_fill

som = SOM(n = 4, dimensions = 5, fill = random_fill)

samples = [[random.gauss(m, 0.1) for e in range(0, 5)] 
    for m in range(0, 20) 
    for sample in range(0,10)]

# training
for sample in samples:
    mh = mexican_hat_with_sigma(1.0)
    som.train(target = sample, rate = 1, distance = euclidean, nf = mh)

# query
for sample in samples:
    winner = som.query(target = sample, distance = euclidean)
    print(winner)


