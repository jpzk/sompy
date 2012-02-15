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

# \brief exponentional damping 
# \author Jendrik Poloczek <jendrik.poloczek@uni-oldenburg.de>
# \return value in [start, end] interpolated by t/tmax
def exponentional_damping(start, end, t, tmax):
    return start * ((end / start) ** (t / tmax))
