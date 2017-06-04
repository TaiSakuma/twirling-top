# twirling-top
experimental interface to alphatwirl

## quick instructions

Check out this repo
```bash
git clone --recursive git@github.com:TaiSakuma/twirling-top.git
```

Update PYTHONPATH
```bash
export PYTHONPATH=$PWD/twirling-top/alphatwirl:$PYTHONPATH
```

Edit the path to the ROOT file in `example.py`:
```bash
emacs twirling-top/example.py 
```

Execute
```bash
./twirling-top/example.py
```
This will loop over the events in the ROOT file, create 2 pandas data frames as configured in `example.py`, and print the data frames as string on the screen as follows.

```
      jet_pt      n   nvar
   19.952623      2      2
   25.118864     19     19
   31.622777    128    128
   39.810717    858    858
   50.118723   3647   3647
   63.095734   9223   9223
   79.432823  13697  13697
  100.000000  13278  13278
  125.892541   9984   9984
  158.489319   6199   6199
  199.526231   3226   3226
  251.188643   1627   1627
  316.227766    849    849
  398.107171    423    423
  501.187234    211    211
  630.957344     81     81
  794.328235     28     28
 1000.000000      6      6
 1258.925412      2      2
 1584.893192      0      0

      muon_pt     n  nvar
    10.000000  1916  1916
    12.589254  2157  2157
    15.848932  2486  2486
    19.952623  2990  2990
    25.118864  4798  4798
    31.622777  5072  5072
    39.810717  4756  4756
    50.118723  4318  4318
    63.095734  3443  3443
    79.432823  2369  2369
   100.000000  1473  1473
   125.892541   792   792
   158.489319   376   376
   199.526231   169   169
   251.188643    60    60
   316.227766    24    24
   398.107171    12    12
   501.187234     9     9
   630.957344     4     4
   794.328235     4     4
  1000.000000     7     7
  1258.925412     3     3
  1584.893192     2     2
  1995.262315     2     2
  2511.886432     1     1
  3162.277660     0     0
  6309.573445     1     1
  7943.282347     0     0
 15848.931925     2     2
 19952.623150     1     1
 25118.864315     0     0
