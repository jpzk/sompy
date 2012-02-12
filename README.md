# sompy

Self-organizing maps in Python. It's not yet ready for use, but you'll be able to create, train and query self-organizing maps via command-line.

## Example

In the following example we create a SOM with 4x4 nodes, weight vectors with five components. 
Each component is initially filled with random_fill (assigns random number between 0 and 1). 

<pre>
from som import SOM
from distance_functions import euclidean
from neighbourhood_functions import mexican_hat_with_sigma
from fill_functions import random_fill

som = SOM(n = 4, dimensions = 5, fill = random_fill)

samples = [[random.gauss(m, 0.1) for e in range(0, 5)] 
    for m in range(0, 20) 
    for sample in range(0,10)]
</pre>

The samples are pseudo random numbers with gauss distribution. We sample 10 times 20 gauss distributions with an 
expected value of 0,1,2...20. Variance is 0.1 for each distribution. 

### Training
We train our SOM by using a for-loop iterating over the samples and train each sample as a target with a given learn-rate, 
distance and neighbourhood function, see files distance_functions and neighbourhood_functions for available functions. 

<pre>
for sample in samples:
    mh = mexican_hat_with_sigma(1.0)
    som.train(target = sample, rate = 1, distance = euclidean, nf = mh)
    
print som.get_matrix()
</pre>

If you want to inspect the weight matrix, you're able to retrieve the weight matrix by calling get_matrix().

### Query

Allright, lets query the trained SOM. The query method needs a given target and distance function to determine the winner
node in the SOM. The returned value is a tuple which consists of i, j indices of the winner node and distance to target.

<pre>
for sample in samples:
    winner = som.query(target = sample, distance = euclidean)
    print winner
</pre>

## License 

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
along with hclu.  If not, see <http://www.gnu.org/licenses/>.


