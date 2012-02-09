# sompy

Self-organizing maps in Python. It's not yet ready for use, but you'll be able to create, train and query self-organizing maps via command-line.

<pre>
from som import SOM
from distance_functions import euclidean
from neighbourhood_functions import mexican_hat_with_sigma
from fill_functions import random_fill

som = SOM(n = 4, dimensions = 5, fill = random_fill)

samples = [[random.gauss(m, 0.1) for e in range(0, 5)] 
    for m in range(0, 20) 
    for sample in range(0,10)]

for sample in samples:
    mh = mexican_hat_with_sigma(1.0)
    som.train(target = sample, rate = 1, distance = euclidean, nf = mh)

print som.get_matrix()
</pre>

## License 

This file is part of hclu.

hclu is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

hclu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with hclu.  If not, see <http://www.gnu.org/licenses/>.


