# Concerning the numbers in the variable `cividis`
# ==================================================
# Copyright (c) 2017, Battelle Memorial Institute
# 
# 1.  Battelle Memorial Institute (hereinafter Battelle) hereby grants
# permission to any person or entity lawfully obtaining a copy of this software
# and associated documentation files (hereinafter “the Software”) to
# redistribute and use the Software in source and binary forms, with or without
# modification. Such person or entity may use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and may permit
# others to do so, subject to the following conditions:
# 
# + Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimers.
# 
# + Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# 
# + Other than as used herein, neither the name Battelle Memorial Institute or
# Battelle may be used in any form whatsoever without the express written
# consent of Battelle.
# 
# 2.  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# ===================================================
# Concerning the rest of the code
# ===================================================
# 
# Copyright 2018 Benjamin F. Maier
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np
import matplotlib.pyplot as pl

from matplotlib.colors import LinearSegmentedColormap

def convert_color_array_to_cdict(arr):

    cdict = { 'red' : [],
              'green' : [],
              'blue' : [],
              'alpha': [ (0.0, 1.0, 1.0), (1.0, 1.0, 1.0) ],
            }

    N = arr.shape[0]
    X = np.linspace(0,1,N)

    for x, (r,g,b) in zip(X, arr):
        cdict['red'].append( (x, r, r) )
        cdict['green'].append( (x, g, g) )
        cdict['blue'].append( (x, b, b) )

    for k in cdict.keys():
        cdict[k] = tuple(cdict[k])

    return cdict

cividis = np.array([
    [0.0000,0.1262,0.3015], 
    [0.0000,0.1292,0.3077],
    [0.0000,0.1321,0.3142],
    [0.0000,0.1350,0.3205],
    [0.0000,0.1379,0.3269],
    [0.0000,0.1408,0.3334],
    [0.0000,0.1437,0.3400],
    [0.0000,0.1465,0.3467],
    [0.0000,0.1492,0.3537],
    [0.0000,0.1519,0.3606],
    [0.0000,0.1546,0.3676],
    [0.0000,0.1574,0.3746],
    [0.0000,0.1601,0.3817],
    [0.0000,0.1629,0.3888],
    [0.0000,0.1657,0.3960],
    [0.0000,0.1685,0.4031],
    [0.0000,0.1714,0.4102],
    [0.0000,0.1743,0.4172],
    [0.0000,0.1773,0.4241],
    [0.0000,0.1798,0.4307],
    [0.0000,0.1817,0.4347],
    [0.0000,0.1834,0.4363],
    [0.0000,0.1852,0.4368],
    [0.0000,0.1872,0.4368],
    [0.0000,0.1901,0.4365],
    [0.0000,0.1930,0.4361],
    [0.0000,0.1958,0.4356],
    [0.0000,0.1987,0.4349],
    [0.0000,0.2015,0.4343],
    [0.0000,0.2044,0.4336],
    [0.0000,0.2073,0.4329],
    [0.0055,0.2101,0.4322],
    [0.0236,0.2130,0.4314],
    [0.0416,0.2158,0.4308],
    [0.0576,0.2187,0.4301],
    [0.0710,0.2215,0.4293],
    [0.0827,0.2244,0.4287],
    [0.0932,0.2272,0.4280],
    [0.1030,0.2300,0.4274],
    [0.1120,0.2329,0.4268],
    [0.1204,0.2357,0.4262],
    [0.1283,0.2385,0.4256],
    [0.1359,0.2414,0.4251],
    [0.1431,0.2442,0.4245],
    [0.1500,0.2470,0.4241],
    [0.1566,0.2498,0.4236],
    [0.1630,0.2526,0.4232],
    [0.1692,0.2555,0.4228],
    [0.1752,0.2583,0.4224],
    [0.1811,0.2611,0.4220],
    [0.1868,0.2639,0.4217],
    [0.1923,0.2667,0.4214],
    [0.1977,0.2695,0.4212],
    [0.2030,0.2723,0.4209],
    [0.2082,0.2751,0.4207],
    [0.2133,0.2780,0.4205],
    [0.2183,0.2808,0.4204],
    [0.2232,0.2836,0.4203],
    [0.2281,0.2864,0.4202],
    [0.2328,0.2892,0.4201],
    [0.2375,0.2920,0.4200],
    [0.2421,0.2948,0.4200],
    [0.2466,0.2976,0.4200],
    [0.2511,0.3004,0.4201],
    [0.2556,0.3032,0.4201],
    [0.2599,0.3060,0.4202],
    [0.2643,0.3088,0.4203],
    [0.2686,0.3116,0.4205],
    [0.2728,0.3144,0.4206],
    [0.2770,0.3172,0.4208],
    [0.2811,0.3200,0.4210],
    [0.2853,0.3228,0.4212],
    [0.2894,0.3256,0.4215],
    [0.2934,0.3284,0.4218],
    [0.2974,0.3312,0.4221],
    [0.3014,0.3340,0.4224],
    [0.3054,0.3368,0.4227],
    [0.3093,0.3396,0.4231],
    [0.3132,0.3424,0.4236],
    [0.3170,0.3453,0.4240],
    [0.3209,0.3481,0.4244],
    [0.3247,0.3509,0.4249],
    [0.3285,0.3537,0.4254],
    [0.3323,0.3565,0.4259],
    [0.3361,0.3593,0.4264],
    [0.3398,0.3622,0.4270],
    [0.3435,0.3650,0.4276],
    [0.3472,0.3678,0.4282],
    [0.3509,0.3706,0.4288],
    [0.3546,0.3734,0.4294],
    [0.3582,0.3763,0.4302],
    [0.3619,0.3791,0.4308],
    [0.3655,0.3819,0.4316],
    [0.3691,0.3848,0.4322],
    [0.3727,0.3876,0.4331],
    [0.3763,0.3904,0.4338],
    [0.3798,0.3933,0.4346],
    [0.3834,0.3961,0.4355],
    [0.3869,0.3990,0.4364],
    [0.3905,0.4018,0.4372],
    [0.3940,0.4047,0.4381],
    [0.3975,0.4075,0.4390],
    [0.4010,0.4104,0.4400],
    [0.4045,0.4132,0.4409],
    [0.4080,0.4161,0.4419],
    [0.4114,0.4189,0.4430],
    [0.4149,0.4218,0.4440],
    [0.4183,0.4247,0.4450],
    [0.4218,0.4275,0.4462],
    [0.4252,0.4304,0.4473],
    [0.4286,0.4333,0.4485],
    [0.4320,0.4362,0.4496],
    [0.4354,0.4390,0.4508],
    [0.4388,0.4419,0.4521],
    [0.4422,0.4448,0.4534],
    [0.4456,0.4477,0.4547],
    [0.4489,0.4506,0.4561],
    [0.4523,0.4535,0.4575],
    [0.4556,0.4564,0.4589],
    [0.4589,0.4593,0.4604],
    [0.4622,0.4622,0.4620],
    [0.4656,0.4651,0.4635],
    [0.4689,0.4680,0.4650],
    [0.4722,0.4709,0.4665],
    [0.4756,0.4738,0.4679],
    [0.4790,0.4767,0.4691],
    [0.4825,0.4797,0.4701],
    [0.4861,0.4826,0.4707],
    [0.4897,0.4856,0.4714],
    [0.4934,0.4886,0.4719],
    [0.4971,0.4915,0.4723],
    [0.5008,0.4945,0.4727],
    [0.5045,0.4975,0.4730],
    [0.5083,0.5005,0.4732],
    [0.5121,0.5035,0.4734],
    [0.5158,0.5065,0.4736],
    [0.5196,0.5095,0.4737],
    [0.5234,0.5125,0.4738],
    [0.5272,0.5155,0.4739],
    [0.5310,0.5186,0.4739],
    [0.5349,0.5216,0.4738],
    [0.5387,0.5246,0.4739],
    [0.5425,0.5277,0.4738],
    [0.5464,0.5307,0.4736],
    [0.5502,0.5338,0.4735],
    [0.5541,0.5368,0.4733],
    [0.5579,0.5399,0.4732],
    [0.5618,0.5430,0.4729],
    [0.5657,0.5461,0.4727],
    [0.5696,0.5491,0.4723],
    [0.5735,0.5522,0.4720],
    [0.5774,0.5553,0.4717],
    [0.5813,0.5584,0.4714],
    [0.5852,0.5615,0.4709],
    [0.5892,0.5646,0.4705],
    [0.5931,0.5678,0.4701],
    [0.5970,0.5709,0.4696],
    [0.6010,0.5740,0.4691],
    [0.6050,0.5772,0.4685],
    [0.6089,0.5803,0.4680],
    [0.6129,0.5835,0.4673],
    [0.6168,0.5866,0.4668],
    [0.6208,0.5898,0.4662],
    [0.6248,0.5929,0.4655],
    [0.6288,0.5961,0.4649],
    [0.6328,0.5993,0.4641],
    [0.6368,0.6025,0.4632],
    [0.6408,0.6057,0.4625],
    [0.6449,0.6089,0.4617],
    [0.6489,0.6121,0.4609],
    [0.6529,0.6153,0.4600],
    [0.6570,0.6185,0.4591],
    [0.6610,0.6217,0.4583],
    [0.6651,0.6250,0.4573],
    [0.6691,0.6282,0.4562],
    [0.6732,0.6315,0.4553],
    [0.6773,0.6347,0.4543],
    [0.6813,0.6380,0.4532],
    [0.6854,0.6412,0.4521],
    [0.6895,0.6445,0.4511],
    [0.6936,0.6478,0.4499],
    [0.6977,0.6511,0.4487],
    [0.7018,0.6544,0.4475],
    [0.7060,0.6577,0.4463],
    [0.7101,0.6610,0.4450],
    [0.7142,0.6643,0.4437],
    [0.7184,0.6676,0.4424],
    [0.7225,0.6710,0.4409],
    [0.7267,0.6743,0.4396],
    [0.7308,0.6776,0.4382],
    [0.7350,0.6810,0.4368],
    [0.7392,0.6844,0.4352],
    [0.7434,0.6877,0.4338],
    [0.7476,0.6911,0.4322],
    [0.7518,0.6945,0.4307],
    [0.7560,0.6979,0.4290],
    [0.7602,0.7013,0.4273],
    [0.7644,0.7047,0.4258],
    [0.7686,0.7081,0.4241],
    [0.7729,0.7115,0.4223],
    [0.7771,0.7150,0.4205],
    [0.7814,0.7184,0.4188],
    [0.7856,0.7218,0.4168],
    [0.7899,0.7253,0.4150],
    [0.7942,0.7288,0.4129],
    [0.7985,0.7322,0.4111],
    [0.8027,0.7357,0.4090],
    [0.8070,0.7392,0.4070],
    [0.8114,0.7427,0.4049],
    [0.8157,0.7462,0.4028],
    [0.8200,0.7497,0.4007],
    [0.8243,0.7532,0.3984],
    [0.8287,0.7568,0.3961],
    [0.8330,0.7603,0.3938],
    [0.8374,0.7639,0.3915],
    [0.8417,0.7674,0.3892],
    [0.8461,0.7710,0.3869],
    [0.8505,0.7745,0.3843],
    [0.8548,0.7781,0.3818],
    [0.8592,0.7817,0.3793],
    [0.8636,0.7853,0.3766],
    [0.8681,0.7889,0.3739],
    [0.8725,0.7926,0.3712],
    [0.8769,0.7962,0.3684],
    [0.8813,0.7998,0.3657],
    [0.8858,0.8035,0.3627],
    [0.8902,0.8071,0.3599],
    [0.8947,0.8108,0.3569],
    [0.8992,0.8145,0.3538],
    [0.9037,0.8182,0.3507],
    [0.9082,0.8219,0.3474],
    [0.9127,0.8256,0.3442],
    [0.9172,0.8293,0.3409],
    [0.9217,0.8330,0.3374],
    [0.9262,0.8367,0.3340],
    [0.9308,0.8405,0.3306],
    [0.9353,0.8442,0.3268],
    [0.9399,0.8480,0.3232],
    [0.9444,0.8518,0.3195],
    [0.9490,0.8556,0.3155],
    [0.9536,0.8593,0.3116],
    [0.9582,0.8632,0.3076],
    [0.9628,0.8670,0.3034],
    [0.9674,0.8708,0.2990],
    [0.9721,0.8746,0.2947],
    [0.9767,0.8785,0.2901],
    [0.9814,0.8823,0.2856],
    [0.9860,0.8862,0.2807],
    [0.9907,0.8901,0.2759],
    [0.9954,0.8940,0.2708],
    [1.0000,0.8979,0.2655],
    [1.0000,0.9018,0.2600],
    [1.0000,0.9057,0.2593],
    [1.0000,0.9094,0.2634],
    [1.0000,0.9131,0.2680],
    [1.0000,0.9169,0.2731],
])

cividis_cmap = convert_color_array_to_cdict(cividis)
cividis_linear_segmented = LinearSegmentedColormap('cividis', cividis_cmap)

pl.register_cmap(cmap=cividis_linear_segmented)

def get_colors(N, n_start=0, n_end=255):
    """Get a color array of `N` entries, where the `N` entries
    are taken at equidistance from the `cividis` array between
    `n_start` and `n_end`"""

    indices = np.linspace(n_start, n_end, N)
    indices = np.array(indices, dtype=int)
    return cividis[indices]

def make_default():
    """Tell matplotlib to use cividis as default colormap."""
    mpl.rcParams['image.cmap'] = 'cividis'

if __name__=="__main__":
    print(get_colors(12))

    x = np.arange(0, 2*np.pi, 0.01)
    y = np.arange(0, 2*np.pi, 0.01)
    X, Y = np.meshgrid(x,y)
    Z = np.cos(X) * np.sin(Y) * 20

    pl.imshow(Z,cmap='cividis')
    pl.colorbar()

    pl.show()
