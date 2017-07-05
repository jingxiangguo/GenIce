# coding: utf-8
"""
A continuous random network of Sillium.

Mousseau, N, and G T Barkema. “Fast Bond-Transposition Algorithms for Generating Covalent Amorphous Structures.” Current Opinion in Solid State and Materials … 5.6 (2001): 497–502. Web.
"""

celltype="rect"
cell="""
26.756 26.756 26.756
"""
density=0.96
coord="absolute"
waters="""
-5.51 3.67 -1.94
-3.46 6.63 3.15
-12.4 -7.29 -5.44
-8.61 7.44 -10.37
12.58 -9.28 -1.27
-6.02 7.38 -1.47
5.57 -10.16 12.83
2.53 -11.04 7.38
-0.36 8.94 3.61
-2.53 -4.55 11.11
-12.25 6.24 -9.94
6.78 8.58 -3.28
-11.15 3.75 -5.71
0.25 1.38 7.4
-12.19 -6.3 7.65
-8.75 9.75 -10.67
-3.85 -0.84 11.78
8.55 -7.87 -10.02
-5.01 -6.27 3.92
-10.67 -9.9 -11.24
12.83 7.55 5.3
9.97 8.73 2.9
-5.24 -12.26 -10.32
-1.73 11.82 -10.06
-0.31 -8.57 8.18
11.01 2.98 -11.54
-1.32 3.22 -5.49
8.48 -0.14 0.61
1.65 -10.38 -1.83
12.23 0.4 4.66
1.91 -4.41 13.33
8.82 5.41 3.72
1.47 -5.16 -10.03
-1.86 -2.88 6.11
1.44 -7.82 6.88
-0.24 -0.14 0.25
-0.05 -11.64 1.15
-5.23 -1.4 -5.55
12.23 1.62 -8.49
10.0 2.3 -8.56
4.96 0.12 -5.06
-4.3 -1.98 -1.88
0.28 6.79 -10.85
-8.54 -5.75 -6.05
-6.69 3.09 8.4
7.06 -0.64 4.01
3.65 -5.64 1.78
2.56 -9.45 5.68
-6.95 -10.65 2.51
-2.77 13.1 1.16
1.14 5.57 11.97
12.1 11.48 -1.05
4.75 -5.56 11.57
-7.28 11.06 -11.86
-1.51 7.57 -2.03
-9.12 4.39 -8.49
-3.76 -9.09 -11.51
1.3 6.33 -8.85
5.41 -6.74 5.84
-10.2 -0.15 12.58
-11.03 8.29 12.21
-4.57 -9.11 -2.82
-2.94 7.02 -9.49
11.99 -3.73 8.53
8.62 1.45 -5.51
-4.21 -0.71 4.54
7.46 6.9 -12.88
6.94 -3.85 -6.89
1.61 -11.61 -5.26
11.32 2.22 5.65
11.42 9.03 6.0
9.92 -9.88 -12.96
-2.88 8.19 -5.88
2.14 12.32 8.53
6.45 -10.86 7.73
13.34 11.36 2.53
10.09 -6.74 0.08
2.47 -13.14 6.67
0.26 -4.93 -12.11
9.01 7.75 10.3
-8.67 -12.91 -4.21
10.49 -12.32 -5.58
-2.27 -8.77 -7.31
5.56 10.16 -8.55
6.55 3.26 12.59
11.0 0.05 10.63
3.36 -7.52 -2.98
-7.66 -0.46 6.28
5.36 -12.35 2.05
-10.5 -0.79 8.78
4.8 5.27 -8.83
0.65 7.27 -5.01
1.17 -1.03 12.99
-4.38 5.86 11.78
9.48 -12.38 7.1
2.82 -12.51 -11.76
-11.71 5.05 -0.6
3.89 7.78 -11.35
3.16 4.62 11.49
-1.14 8.34 -4.14
-0.26 -11.29 -1.09
2.62 10.95 -10.3
0.52 -9.4 -9.2
-0.13 9.43 9.11
5.71 11.67 5.47
-3.57 -2.91 -5.23
-9.68 12.57 1.16
9.68 12.83 1.45
-11.33 -11.97 6.19
-8.13 -12.09 -12.88
2.48 2.91 10.0
11.38 -0.25 2.8
-2.32 9.39 -1.03
-6.79 -1.14 1.74
-9.98 0.75 -0.98
-12.28 3.3 0.57
-10.89 13.14 7.93
-8.23 -7.32 -9.6
11.13 9.77 13.17
9.74 -1.14 6.85
-2.65 5.01 0.15
1.77 -8.85 -10.72
9.54 3.25 -6.46
-7.81 4.03 -1.69
4.44 10.02 -11.43
4.21 -8.6 -4.97
3.54 -13.12 -8.14
-0.39 12.64 13.08
-9.41 6.81 -12.17
11.57 -3.73 -9.24
-7.5 10.55 -2.93
1.93 12.81 -2.16
-7.42 12.55 0.97
-8.62 -8.08 4.17
7.49 -4.78 9.56
-1.91 0.02 4.7
5.88 -4.86 4.53
12.95 -9.18 -6.23
-3.2 1.32 -0.36
4.13 -9.08 9.74
6.83 10.37 -1.76
-10.58 -3.15 8.7
-9.65 -6.14 -2.41
4.59 -12.04 -3.5
-10.3 -1.99 -12.99
13.2 -2.84 10.45
-3.91 -11.86 10.64
5.62 -5.41 0.74
-12.68 -12.55 4.31
10.88 5.77 -9.1
-12.1 2.37 10.46
9.64 10.97 -3.95
7.13 1.0 9.13
9.1 -3.33 -6.6
10.49 10.36 4.32
1.57 -1.99 5.37
-5.64 12.16 5.99
-12.94 1.74 -12.86
-0.2 10.5 -4.18
5.01 -5.26 -4.54
4.5 -0.61 7.01
13.1 -3.07 4.46
3.3 7.88 -2.36
-11.47 -3.93 10.72
4.61 4.4 13.37
0.03 9.86 5.7
9.95 -5.58 4.49
-4.84 -4.26 0.96
-2.2 -8.11 7.02
-2.41 2.82 -9.06
-8.08 8.85 1.79
3.72 1.75 -8.23
2.16 6.7 3.54
-7.86 6.06 10.15
7.28 12.8 2.3
-10.82 9.61 6.82
-6.0 -1.32 -7.61
-0.76 4.6 8.76
13.12 5.17 -8.54
-6.16 3.21 -10.96
6.96 -3.49 -1.93
2.15 8.86 9.1
-2.95 1.98 -12.68
-4.06 -11.33 4.87
-5.41 2.25 10.32
-12.46 -12.46 -0.21
-3.85 -4.51 3.11
-11.95 -2.59 -11.62
4.79 11.03 13.37
-6.03 6.25 0.67
-7.57 7.28 13.33
11.37 12.52 -4.52
2.36 -3.2 8.56
5.75 -5.98 -13.08
12.15 7.74 3.06
2.08 -11.83 11.55
-8.03 -0.55 -3.35
-10.98 9.07 -0.66
11.35 -13.24 12.81
-3.55 11.42 -8.52
0.2 6.07 10.05
5.35 1.19 -1.31
-8.03 5.89 -5.09
7.17 9.16 -7.46
12.75 0.12 1.01
9.97 -4.84 -8.11
0.96 5.5 -3.79
-5.5 -12.18 -3.92
-10.89 -1.77 2.1
8.83 0.93 7.59
-10.78 -7.14 12.69
-0.77 1.58 11.15
-8.28 -6.16 8.17
-4.52 -6.89 -2.08
-5.66 2.06 -6.56
11.72 -5.93 9.08
5.44 6.36 -12.1
-0.19 -11.74 4.89
-9.92 -12.77 -6.03
9.68 -3.21 11.91
-7.64 -4.31 11.49
3.27 3.6 -9.53
-1.09 -3.12 -12.05
-4.92 -6.26 -7.39
-0.41 -10.38 -13.2
5.22 1.28 -11.32
2.05 12.5 3.33
9.16 -9.95 11.63
4.45 3.25 -2.22
11.53 11.66 -9.92
-7.08 11.73 9.19
0.13 7.25 -7.26
10.68 9.36 11.01
3.84 8.75 -7.88
10.93 7.85 -6.08
10.59 -8.68 10.47
1.47 2.48 -12.85
-12.01 -5.83 -9.75
-0.64 -4.24 -4.67
4.47 -13.13 5.5
2.16 13.03 -9.94
6.38 -2.76 9.71
9.19 12.92 -13.27
12.08 1.94 -2.22
-3.36 -7.63 1.15
2.47 -9.39 -7.81
-6.47 6.77 -9.96
-8.74 -1.38 3.0
-12.51 -8.75 5.48
-3.78 6.6 1.14
6.37 12.5 9.13
13.1 2.99 11.91
2.55 8.48 -4.45
-1.89 -11.02 -7.46
0.47 -4.52 8.93
7.0 -2.19 -3.62
-6.63 12.04 11.45
2.25 10.2 -8.12
7.9 -8.68 4.42
1.35 -6.45 10.07
-9.2 -9.26 -6.12
-5.12 8.47 5.56
12.86 -5.52 -6.05
-3.89 12.09 2.85
-2.3 8.55 -12.92
2.96 3.85 1.19
0.73 3.42 0.54
12.21 1.42 -6.23
-0.55 -1.85 4.62
-13.31 -5.56 -2.18
-7.6 -6.49 10.48
10.62 0.72 -12.18
-8.5 0.06 8.51
10.81 -9.82 -2.74
-11.54 -9.31 -9.18
-5.47 0.06 6.31
-11.48 -0.07 -2.44
-13.15 -4.39 -8.14
-5.08 -9.18 13.24
-5.45 2.36 6.42
-9.5 -2.73 -7.81
-1.87 -4.56 -1.0
8.42 0.74 -9.48
-3.95 -8.0 3.41
6.35 13.02 -10.91
13.27 5.39 11.78
-4.21 10.36 5.85
-10.93 12.2 -2.33
5.57 4.96 -3.59
10.88 -10.58 7.19
11.56 -6.15 -12.23
-5.16 4.22 -7.02
-8.64 8.83 12.03
0.94 3.24 -6.51
2.28 9.62 5.84
-12.53 3.39 4.26
5.99 -2.51 13.04
12.25 -4.56 -3.96
-3.97 -11.94 -6.91
7.07 -5.38 2.55
-11.78 -4.02 7.03
-6.44 1.75 12.31
2.05 6.05 -1.81
-13.05 -7.0 9.57
0.34 -10.82 8.31
-10.17 -7.25 7.4
-10.7 1.68 1.04
11.2 -10.67 4.88
10.94 -6.4 -6.95
-2.47 -2.06 -3.25
-8.35 -0.85 -7.83
9.98 5.76 7.12
9.57 -7.58 -12.21
-12.94 8.54 -0.07
2.95 3.59 6.4
-5.55 -8.57 8.52
12.14 7.87 -2.86
-0.95 -4.83 6.99
-8.62 -1.82 -11.4
-12.64 1.53 -3.37
-12.4 10.85 -5.8
6.98 9.41 0.45
1.53 -4.49 -5.19
-0.91 -6.83 -12.71
-4.74 -13.32 -8.34
-2.49 -7.26 -11.04
-11.28 5.3 -2.78
3.43 11.57 -3.22
9.89 3.93 -9.93
2.29 0.87 10.53
11.04 -1.5 -9.14
5.25 7.8 0.64
2.8 0.82 -4.49
2.6 12.71 0.06
-2.0 -8.46 4.57
4.43 -6.11 7.84
8.92 10.63 -13.07
-7.19 -7.52 0.67
1.35 -6.23 -6.58
-1.55 -4.99 2.74
-1.97 -12.0 -4.05
-0.88 -1.39 9.57
5.16 -3.47 -0.54
-9.0 4.22 -6.24
-2.13 -6.05 -4.54
-12.03 -9.01 -1.95
5.31 12.21 -7.72
11.45 6.06 -1.63
-0.42 -7.58 -1.57
5.56 -3.96 -12.05
0.09 1.53 1.92
-6.2 11.05 -4.61
6.63 0.81 -6.51
3.57 3.0 -11.83
4.4 -10.99 8.78
12.43 2.21 0.06
-1.23 8.99 7.31
3.09 -5.28 -3.48
1.98 -4.9 0.3
8.99 2.28 5.74
-5.43 2.51 2.27
-5.5 -3.71 6.34
-0.35 10.49 -0.49
-3.44 -9.33 8.16
10.51 -11.93 -1.81
5.44 -2.62 7.5
2.04 10.53 -4.55
6.02 8.65 8.11
-1.69 -0.44 11.41
-0.52 -12.05 -5.82
7.29 -10.75 -6.05
-10.9 -12.08 -11.19
7.6 -0.62 -8.04
5.8 -12.33 12.34
12.71 -2.43 -12.53
-3.16 2.59 6.85
-3.62 7.38 10.13
-7.45 -8.54 -13.2
2.95 -1.06 -12.49
-10.77 -10.22 1.81
-2.95 10.48 -6.36
-12.71 3.19 8.45
-12.12 9.42 10.59
5.71 -10.22 -4.44
7.77 5.38 0.04
-3.04 -9.75 0.27
-1.89 1.58 3.14
-7.88 6.36 6.45
-7.34 -13.37 -11.13
-7.38 5.41 4.31
7.18 3.18 10.2
11.09 -10.13 -5.07
8.2 1.4 3.73
3.0 -3.99 -1.6
-8.4 -10.04 -11.77
8.58 7.32 -3.08
5.76 2.39 -7.76
-8.97 0.33 4.42
8.81 -11.06 -11.18
8.3 -3.66 2.04
-6.95 10.68 -7.95
6.95 -3.43 6.12
8.33 8.68 8.18
10.16 -8.0 1.82
12.32 6.32 9.87
-7.42 -9.42 -9.76
8.01 -0.11 12.57
-4.96 -5.84 6.13
-8.97 -3.52 -9.9
-2.16 -11.41 1.72
8.32 10.2 -11.04
4.24 5.88 9.93
4.99 -3.39 11.25
12.51 -0.11 -12.08
-6.94 -9.83 0.36
-3.77 3.39 -10.96
8.37 -12.61 -4.95
0.24 2.72 9.27
-2.28 -1.23 7.81
-3.16 8.91 1.03
-5.67 5.79 -5.26
-11.47 0.31 7.15
6.35 -10.94 -8.3
12.74 -11.04 0.58
-7.21 -6.66 2.91
3.77 4.7 -0.71
-3.25 10.07 7.87
1.46 -2.29 -2.09
3.47 -9.78 11.8
7.49 -7.64 6.29
-2.93 4.15 8.69
8.64 -6.96 3.13
-2.14 -10.82 -11.6
9.66 -1.32 -7.41
10.93 -7.15 7.43
-10.32 6.09 6.46
-10.81 -4.49 -10.98
-9.03 -10.81 -2.97
-11.31 -10.75 -3.28
-8.47 0.02 -9.99
-8.37 -0.71 -1.14
9.73 0.95 2.18
4.14 -1.84 -6.15
-9.01 10.19 -8.59
5.6 -3.25 -5.23
-8.21 7.44 -1.94
-0.09 12.75 -6.92
-4.96 -11.98 8.51
12.24 -7.85 2.7
8.4 4.51 5.88
10.39 -11.06 -9.49
-12.01 12.18 4.16
-10.31 -11.98 0.55
12.14 -1.56 -0.31
-7.12 -8.77 5.6
7.56 -8.94 8.07
-7.96 -9.09 -4.15
11.27 12.16 3.16
12.0 -3.35 12.3
11.74 9.98 7.93
12.71 11.71 13.27
-2.8 0.54 -8.5
-1.13 -11.9 7.03
-1.95 -6.74 11.86
2.81 -10.41 0.21
-5.25 -2.93 -9.05
2.06 -0.07 -10.65
9.01 -2.74 -11.49
11.92 -11.01 -13.08
-8.75 -3.47 -5.79
-13.15 -7.04 1.02
6.04 -11.37 5.62
7.02 -6.16 -7.2
-9.93 3.14 10.73
12.85 -10.8 8.46
5.42 10.85 7.66
-11.93 11.05 -10.27
1.95 11.76 -6.51
7.67 12.51 4.68
-12.86 -12.71 -8.06
4.52 3.95 4.88
-11.84 -2.41 -7.75
-6.58 10.39 0.8
-11.05 8.89 -3.05
12.2 13.3 -2.6
-9.07 -10.07 3.34
9.2 -2.81 -4.47
-7.72 4.54 0.36
12.21 5.62 6.32
-9.34 4.29 3.85
0.49 1.49 -11.13
-7.14 8.57 6.6
5.08 11.69 -1.75
-1.91 -1.56 1.14
3.7 -4.16 7.33
-3.19 12.13 8.43
-1.58 -8.19 -5.17
3.55 -12.61 3.62
9.74 11.35 10.04
6.69 -13.2 -8.79
5.02 -6.89 -6.34
-0.73 -3.37 -2.51
-5.14 -6.53 0.08
6.18 8.03 4.21
11.21 3.93 -3.02
13.13 -0.64 10.18
-10.56 5.85 2.62
-11.11 1.7 -6.75
8.11 -12.16 5.18
6.79 2.17 -9.95
9.57 -3.38 3.85
-10.99 11.32 -0.22
10.44 1.79 9.02
-7.13 -3.06 9.68
-10.56 -3.86 5.04
-7.88 -6.71 -3.93
-9.3 7.87 0.03
3.5 7.06 -9.14
-3.93 -8.1 11.62
4.19 7.86 -5.82
-0.85 -9.9 11.3
-6.96 -4.29 -9.67
-7.86 -0.17 12.17
-2.05 0.96 -5.14
-11.98 -8.57 -12.8
-0.8 -1.18 -13.29
-4.78 10.07 2.03
-6.8 9.43 8.81
2.23 6.61 8.88
4.32 -1.98 -8.6
1.03 -12.26 -13.23
5.92 -9.63 4.06
8.42 -4.41 7.63
12.92 -3.12 6.58
-12.97 9.3 -9.25
8.23 -2.21 13.27
7.13 -9.7 -10.24
-5.14 10.03 -9.33
0.72 -8.52 -12.63
12.35 -10.87 -10.76
-13.05 3.13 -9.23
-12.02 11.58 6.58
8.52 7.62 4.25
-9.97 8.3 -7.4
7.57 11.65 10.76
-11.8 -7.05 -3.14
-0.88 11.69 1.25
-7.94 -11.72 9.85
0.15 9.49 -7.9
-11.19 -8.37 0.27
-13.25 4.95 -6.35
3.44 -2.41 2.57
-3.79 10.8 -2.09
-8.86 -8.18 11.65
13.05 -8.79 -9.87
-9.39 -6.87 -0.03
-9.29 -11.49 5.24
-5.43 1.67 -3.05
2.19 -9.56 -5.81
-7.84 2.14 -5.79
6.74 2.62 2.42
-4.46 -8.61 -7.8
6.99 10.26 12.38
5.9 11.56 -5.54
9.57 -1.72 10.18
10.41 4.35 -13.17
-1.39 7.16 3.97
-11.9 -3.74 -1.29
0.89 12.95 1.51
8.47 -13.19 -11.51
1.51 -2.88 1.39
10.0 11.15 -0.21
-6.73 5.56 12.15
-11.61 7.85 5.5
-8.7 9.96 5.76
12.08 12.89 -7.97
-3.02 12.8 10.59
-12.3 -1.8 -5.53
6.0 10.95 1.7
-9.64 -10.15 10.37
2.3 4.26 -4.95
5.2 10.16 3.75
9.13 -9.24 -6.25
1.82 7.86 -12.05
6.25 1.03 -13.28
9.54 3.62 10.13
-5.68 3.74 4.36
-8.21 -10.34 6.86
-2.34 3.34 4.7
-9.5 3.21 13.16
-5.48 -9.65 4.08
-12.01 0.18 1.88
-10.75 2.53 7.32
1.0 -7.9 2.17
3.0 -6.91 -10.11
-10.72 4.0 5.58
-3.86 5.0 4.49
1.86 -2.21 -5.69
-5.25 12.74 8.01
2.39 -4.25 5.35
-12.48 1.06 3.98
-5.49 -0.45 -11.81
-12.48 4.61 2.45
2.47 2.65 -3.22
8.72 -6.43 -3.72
-1.5 -9.52 -1.4
-5.2 -9.75 -9.87
-10.67 1.44 -12.64
6.33 -8.23 9.84
6.44 5.79 -9.99
0.35 2.83 -1.84
-11.34 12.59 -6.98
-6.41 1.0 -10.28
8.79 -8.46 -2.57
2.93 -13.24 -6.22
-8.87 2.32 8.79
-9.98 -5.27 1.66
-3.6 3.74 10.87
-0.53 -3.37 10.46
0.68 -8.11 -5.14
-12.64 5.03 -11.83
4.81 -12.88 10.22
5.31 -9.5 -11.73
13.29 3.14 -11.32
-5.33 -7.04 10.16
-4.47 0.89 -4.95
10.09 0.85 12.49
-5.86 -9.92 -4.42
-9.8 5.76 0.6
8.72 12.66 -8.39
7.57 -0.83 10.41
8.61 3.39 -0.46
0.18 -11.59 10.38
13.36 7.15 -5.86
-0.35 -7.85 10.43
12.63 12.02 7.57
1.68 -1.1 -0.19
-0.83 13.02 10.85
10.88 9.83 -7.09
-5.41 9.96 -11.62
7.72 -10.05 0.48
-0.31 3.23 -9.95
-4.96 0.24 -1.33
-8.52 8.09 -5.6
-6.71 4.58 -9.13
0.69 -5.92 5.64
-12.0 -1.03 -9.7
-12.66 0.63 -5.54
9.9 -9.09 -8.47
-8.01 -2.98 -1.14
4.2 -8.28 4.57
-5.9 9.77 -1.4
-11.34 -3.72 0.86
11.41 -2.45 3.09
-2.74 4.28 -7.18
1.09 -1.64 -9.36
-13.33 -7.21 -11.27
2.66 -8.01 13.09
9.54 -0.67 -10.72
10.87 -13.34 10.56
-7.2 3.53 -13.26
8.01 -5.8 -9.18
8.59 8.08 -10.91
10.68 -6.43 10.89
-9.94 -3.83 -2.33
2.9 -0.81 3.95
-10.28 -12.69 -13.29
7.84 -6.77 13.01
5.66 6.1 -0.64
-6.9 -12.44 11.96
-8.5 -3.82 8.07
9.35 6.95 -0.82
-2.4 12.36 -12.29
12.29 -5.67 12.4
-4.58 9.34 9.7
-0.63 9.91 -10.04
12.48 8.75 9.83
1.77 1.09 3.41
4.48 12.88 -4.67
0.41 -6.68 0.32
-12.89 -12.55 -10.39
-6.85 7.15 2.63
-4.17 -1.87 -10.83
-8.62 13.02 8.38
0.75 10.73 13.08
-6.67 5.37 8.31
4.3 -8.97 0.71
9.43 12.0 -10.3
3.83 0.1 0.22
-2.57 5.61 -2.22
10.72 7.74 -10.46
-1.42 -13.05 -2.17
1.33 -0.92 -3.83
12.24 11.44 -6.19
-7.12 -5.97 -8.03
-3.92 -5.43 -11.02
2.34 -11.88 -3.16
-1.68 -3.99 -8.28
2.23 -1.33 7.36
-12.04 -13.33 10.12
7.12 7.99 11.78
-11.06 -5.66 3.79
-1.7 9.99 2.55
3.68 5.29 3.01
-8.19 10.96 12.7
5.46 6.57 2.53
-4.96 -10.32 -0.83
3.12 10.43 7.79
2.98 12.95 10.6
-0.22 5.39 6.74
-2.02 6.58 -7.47
1.26 8.85 0.35
8.77 10.82 -7.17
11.6 9.55 -9.19
10.61 -11.87 0.59
1.03 -0.17 8.73
9.89 -8.94 8.29
4.78 -0.45 12.87
-8.39 8.35 9.92
-4.98 7.8 -6.3
5.61 4.38 8.74
-3.92 -5.18 9.32
0.75 13.13 5.01
-12.55 7.17 -3.71
8.9 -7.03 -5.89
1.27 2.36 5.48
3.37 -3.29 -11.86
9.01 -11.96 10.52
1.29 -8.25 -2.85
1.22 4.11 -8.64
1.65 8.72 2.6
3.98 -0.3 10.64
1.3 -2.84 11.84
7.22 -3.85 -10.39
-7.38 -13.14 -0.97
9.93 -1.17 -0.99
-0.85 11.78 5.52
-2.43 -9.72 -3.49
-3.66 10.51 -13.07
-10.06 6.51 -8.95
10.06 5.78 9.49
8.69 11.67 -2.02
12.21 2.06 7.77
2.9 10.32 3.73
-10.59 5.1 -12.93
8.15 4.63 -12.93
-1.92 3.06 12.32
-10.38 11.87 -8.86
-8.43 -12.39 -7.83
7.83 -13.17 11.93
8.55 -12.73 -2.51
-10.91 -10.77 -5.62
13.11 6.3 -0.13
-1.62 7.07 6.27
7.86 -12.49 8.56
-2.91 -9.88 10.42
-1.54 8.24 -10.72
-9.98 11.96 3.27
-4.63 0.69 13.33
1.84 -10.83 4.04
-0.26 4.06 4.93
-5.05 -13.33 4.15
2.9 7.33 5.7
5.84 4.55 -7.05
-1.45 -0.48 -6.79
-0.93 4.26 -3.31
3.98 2.8 8.34
-3.93 -2.94 4.88
12.89 -7.2 6.26
-10.11 -9.45 8.14
-6.78 13.19 -5.07
10.82 -1.19 -4.24
-10.28 -7.21 -6.59
-4.42 11.1 11.49
0.36 6.91 -0.53
3.49 -10.52 -10.81
12.24 5.88 -13.14
8.28 -7.89 -0.55
-8.92 8.87 -3.53
-11.18 3.29 -3.51
-0.89 10.96 -6.3
2.95 10.97 11.99
-10.63 8.63 8.94
-3.21 -3.53 -12.16
-13.01 12.14 0.44
3.31 -7.62 2.4
8.14 4.96 -6.29
3.45 1.78 2.03
-1.77 -2.81 -6.31
-9.32 0.51 -6.19
4.05 -10.9 -8.58
-11.14 8.42 -12.47
5.18 7.86 10.39
-4.17 3.28 0.2
-6.93 0.34 0.05
9.22 -6.1 6.51
-13.17 -4.79 1.46
7.21 4.98 2.24
-7.6 1.53 -3.69
-7.37 2.4 1.31
11.18 -3.89 -11.37
7.77 4.11 -10.67
10.02 -4.53 -3.28
-8.84 5.66 -2.89
-8.53 13.34 4.45
-12.14 11.53 11.64
11.94 7.89 -12.26
-7.23 -0.86 10.13
-7.88 12.18 6.22
12.84 -9.17 10.27
-4.29 5.98 8.31
12.41 5.84 1.98
-2.91 -6.02 7.37
-12.82 8.02 -11.03
-5.13 -3.28 8.55
3.24 -7.14 -7.82
-0.01 11.77 9.12
12.93 9.7 -1.91
4.0 0.13 -9.72
-10.02 5.28 10.19
-5.51 -10.11 -6.6
12.24 -7.06 -0.74
9.26 8.99 0.61
5.36 6.97 -2.57
-5.04 0.1 2.64
-0.95 -2.41 -9.89
4.03 -12.36 0.24
6.45 -2.53 -8.69
10.71 2.95 11.93
-7.71 -10.28 -7.67
-0.09 11.85 -2.35
-0.41 -6.84 3.8
10.94 12.92 6.34
-6.69 -10.61 8.49
-10.59 10.37 -11.83
-9.32 9.72 3.49
-1.11 1.03 -1.5
3.15 -2.45 10.5
1.53 7.64 12.56
1.17 1.01 12.23
-3.96 11.42 -4.44
8.83 -5.3 11.36
-5.17 0.64 -8.3
-6.49 -7.2 7.01
-12.8 -10.87 2.61
8.36 -2.02 5.22
6.69 -5.59 -2.92
-10.51 -7.33 -8.8
-5.8 -5.58 -3.44
-2.36 -0.73 -10.16
5.0 -1.76 1.01
-11.13 -0.16 5.11
-6.92 -3.3 0.95
-3.0 5.43 -11.24
-1.12 -7.69 -8.99
0.84 -0.74 -7.22
12.14 3.95 4.76
1.99 5.76 6.91
12.7 -0.2 -9.72
-10.4 -2.73 -4.46
11.81 -3.44 1.03
10.85 4.57 2.81
-11.63 0.1 10.68
6.33 -6.71 -0.94
12.15 -6.29 4.33
9.43 7.78 6.42
-0.58 -2.86 2.54
13.24 12.2 -11.23
-3.77 6.72 -12.95
9.36 11.42 5.8
-0.08 4.19 13.28
2.82 -7.45 8.59
-7.02 -2.24 -4.49
4.33 -7.43 -11.95
2.59 -6.08 11.95
-11.06 8.15 3.35
-0.74 4.95 -11.5
-7.84 -6.6 -11.9
6.09 4.99 6.43
13.15 0.04 7.91
-1.17 7.98 10.41
4.38 5.38 -5.5
5.31 7.25 6.2
-0.9 -11.25 -9.49
-4.93 7.82 -8.71
-3.1 0.27 1.7
-13.02 9.08 2.2
-4.42 -1.08 8.21
-1.58 -5.93 0.79
-9.06 2.15 2.79
-3.85 -4.71 -8.79
-8.57 -3.32 4.31
-6.87 -12.93 2.89
4.87 13.27 -12.63
12.93 -9.5 3.87
-9.77 -3.81 12.39
10.42 0.06 -5.91
3.41 8.97 -0.34
12.05 -1.07 6.4
10.45 2.93 1.1
-3.83 6.58 6.28
6.05 9.16 -5.43
-13.18 5.42 8.23
-9.93 -0.67 -4.17
-0.12 13.32 -9.24
7.14 -1.6 1.84
-10.28 11.78 13.09
-9.85 -5.54 -12.78
-1.07 -0.18 -3.49
-12.16 8.81 -7.06
9.15 -10.55 3.95
-4.92 -11.55 12.61
-10.8 2.57 -8.84
-1.99 -10.77 3.92
-6.61 9.39 -6.08
11.83 -12.87 4.6
9.79 -4.43 0.45
7.87 5.15 -3.93
-3.29 -3.02 -0.18
6.7 -9.59 -2.58
-6.14 -5.22 -11.7
-10.53 -7.46 5.09
-4.26 -5.27 -5.23
4.13 11.09 0.17
3.84 -4.31 3.64
-12.32 -5.99 11.35
-11.1 6.32 8.48
9.2 -3.42 -1.41
7.78 7.41 -8.85
-12.06 -10.25 7.18
-6.16 -3.72 13.13
-3.41 -11.2 7.06
-5.27 -12.47 -1.63
-7.02 -1.65 -12.87
-0.09 -5.72 -8.33
4.99 -8.24 -1.4
-8.07 -4.59 2.53
10.26 8.54 -4.08
2.67 -3.29 -9.63
-11.69 -2.16 4.17
8.92 3.44 -2.72
10.34 0.23 -2.64
-1.42 0.46 -11.83
-9.25 -13.09 -9.77
-12.34 -12.7 -2.42
-3.7 -12.46 -12.19
6.38 0.02 -3.15
12.81 -2.34 -4.05
-7.57 -2.88 6.14
-12.1 10.58 -3.45
6.2 10.68 -10.55
-8.56 -11.18 -0.76
-6.2 -3.34 -2.66
8.42 1.32 -3.4
4.97 0.71 8.7
12.72 -13.04 9.25
2.01 1.25 -6.69
11.65 3.64 -5.42
4.98 2.06 3.68
-1.85 0.77 6.85
7.21 -8.78 11.83
-2.27 -6.26 -2.31
1.25 -10.11 1.95
-11.27 6.04 11.9
-12.34 -10.58 -7.29
7.14 1.73 0.19
5.93 -10.17 1.86
9.46 6.47 -7.43
-9.17 2.46 -2.39
5.37 -12.72 -1.49
8.09 11.88 -5.37
-8.68 12.45 -2.57
-5.04 -0.04 9.99
-3.43 12.95 -1.08
1.11 10.03 -11.54
-3.99 -3.2 12.49
-13.15 -5.01 3.62
-2.63 11.13 4.27
-12.98 -1.83 -1.95
7.16 -11.47 -1.32
-13.07 -10.04 12.37
-6.73 12.96 -7.34
5.82 -6.18 9.66
-10.42 0.82 -10.3
-5.09 8.26 3.47
-5.79 7.63 -12.02
9.46 -10.27 1.69
11.81 -8.18 -8.04
0.08 5.61 3.28
9.48 10.61 7.99
-0.46 5.22 0.98
-4.82 5.72 -2.94
4.94 -0.0 4.8
-11.29 -11.51 11.57
-0.47 8.8 12.39
-1.34 12.64 7.48
-3.75 -12.96 -4.82
9.9 -2.78 8.32
10.34 -12.63 -7.82
3.13 8.9 11.11
"""
pairs="""
0 991
0 793
0 557
0 123
1 249
1 566
1 984
1 596
2 772
2 137
2 262
2 545
3 246
3 15
3 128
3 739
4 821
4 423
4 345
4 273
5 991
5 445
5 651
5 189
6 960
6 373
6 622
6 428
7 77
7 47
7 354
7 304
8 702
8 730
8 165
8 566
9 463
9 618
9 975
9 721
10 178
10 739
10 620
10 813
11 823
11 140
11 395
11 901
12 507
12 779
12 550
12 343
13 417
13 715
13 959
13 725
14 305
14 303
14 300
14 768
15 53
15 443
15 834
16 368
16 758
16 975
16 972
17 312
17 648
17 661
17 536
18 407
18 283
18 424
18 186
19 524
19 274
19 394
19 371
20 70
20 194
20 488
20 573
21 194
21 822
21 154
21 542
22 945
22 388
22 324
22 606
23 672
23 199
23 904
23 675
24 168
24 304
24 634
24 34
25 623
25 565
25 328
25 271
26 523
26 293
26 765
26 654
27 735
27 905
27 965
27 441
28 464
28 696
28 728
28 100
29 898
29 69
29 111
29 600
30 732
30 78
30 874
30 726
31 542
31 797
31 449
31 861
32 78
32 594
32 938
32 934
33 268
33 418
33 767
33 317
34 47
34 645
34 871
35 636
35 350
35 836
35 493
36 568
36 962
36 409
36 100
37 105
37 872
37 625
37 176
38 39
38 540
38 858
38 267
39 328
39 282
39 122
40 332
40 442
40 352
40 946
41 309
41 642
41 952
41 918
42 57
42 876
42 583
42 756
43 469
43 515
43 694
43 772
44 184
44 615
44 279
44 685
45 845
45 992
45 392
45 905
46 924
46 358
46 785
46 147
47 759
47 650
48 485
48 590
48 892
48 414
49 546
49 973
49 263
49 409
50 200
50 838
50 870
50 98
51 784
51 571
51 484
51 817
52 193
52 874
52 412
52 982
53 388
53 704
53 639
54 774
54 99
54 112
54 689
55 343
55 912
55 644
55 739
56 432
56 325
56 278
56 606
57 729
57 517
57 231
58 429
58 335
58 136
58 650
59 607
59 522
59 862
59 144
60 963
60 791
60 292
60 382
61 213
61 706
61 627
61 737
62 884
62 853
62 710
62 756
63 997
63 215
63 533
63 145
64 352
64 122
64 953
64 896
65 135
65 767
65 275
65 824
66 745
66 662
66 700
66 216
67 153
67 472
67 444
67 827
68 696
68 614
68 558
68 369
69 856
69 742
69 359
70 459
70 865
70 154
71 227
71 398
71 312
71 468
72 719
72 380
72 710
72 99
73 708
73 816
73 707
73 77
74 354
74 754
74 455
74 471
75 784
75 457
75 886
75 451
76 777
76 916
76 821
76 403
77 239
77 722
78 323
78 222
79 232
79 700
79 740
79 402
80 218
80 770
80 437
80 971
81 416
81 998
81 191
81 391
82 253
82 561
82 496
82 854
83 346
83 233
83 950
83 203
84 745
84 164
84 390
84 584
85 512
85 564
85 626
85 505
86 357
86 935
86 125
86 728
87 272
87 948
87 275
87 397
88 966
88 174
88 826
88 497
89 421
89 272
89 862
89 141
90 221
90 517
90 763
90 609
91 99
91 206
91 252
91 231
92 732
92 839
92 525
92 378
93 617
93 868
93 572
93 376
94 754
94 832
94 508
94 289
95 530
95 240
95 893
95 775
96 326
96 752
96 628
96 115
97 583
97 124
97 216
97 517
98 110
98 411
98 164
99 158
100 691
100 605
101 240
101 974
101 124
101 257
102 245
102 121
102 883
102 854
103 816
103 356
103 181
103 880
104 581
104 475
104 239
104 478
105 309
105 788
105 922
106 452
106 757
106 511
106 132
107 174
107 714
107 571
107 457
108 929
108 556
108 148
108 116
109 388
109 669
109 394
109 666
110 329
110 417
110 766
111 441
111 204
111 653
112 419
112 552
112 362
113 794
113 824
113 852
113 247
114 276
114 306
114 440
114 968
115 306
115 602
115 355
116 683
116 541
116 699
117 694
117 877
117 847
117 405
118 232
118 806
118 336
118 460
119 209
119 898
119 997
119 845
120 249
120 793
120 990
120 689
121 594
121 538
121 775
122 786
122 957
123 803
123 968
123 487
124 950
124 188
125 558
125 500
125 383
126 240
126 614
126 790
126 346
127 684
127 530
127 637
127 672
128 744
128 190
128 791
129 277
129 205
129 800
129 330
130 971
130 778
130 651
130 351
131 333
131 830
131 327
131 696
132 892
132 482
132 734
133 485
133 424
133 454
133 921
134 532
134 982
134 241
134 841
135 959
135 268
135 386
136 401
136 924
136 299
137 964
137 987
137 391
138 642
138 836
138 885
138 793
139 608
139 428
139 871
139 354
140 321
140 741
140 492
141 670
141 163
141 300
142 545
142 515
142 664
142 555
143 383
143 678
143 969
143 696
144 187
144 895
144 318
145 505
145 163
145 458
146 755
146 911
146 576
146 447
147 299
147 863
147 342
148 451
148 915
148 844
149 690
149 178
149 328
149 967
150 473
150 381
150 251
150 862
151 741
151 191
151 937
151 970
152 954
152 390
152 209
152 630
153 486
153 433
153 205
154 869
154 457
155 268
155 665
155 599
155 698
156 808
156 286
156 598
156 761
157 251
157 413
157 623
157 607
158 366
158 780
158 830
159 444
159 846
159 500
159 357
160 992
160 365
160 698
160 954
161 939
161 653
161 976
161 533
162 897
162 302
162 252
162 823
163 925
163 895
164 216
164 353
165 356
165 736
165 294
166 795
166 864
166 431
166 510
167 502
167 186
167 918
167 852
168 363
168 334
168 812
169 641
169 415
169 654
169 461
170 835
170 516
170 482
170 681
171 396
171 818
171 221
171 956
172 762
172 703
172 988
172 730
173 819
173 685
173 572
173 718
174 578
174 478
175 574
175 573
175 782
175 541
176 310
176 842
176 465
177 709
177 200
177 430
177 417
178 550
178 540
179 660
179 612
179 415
179 644
180 846
180 255
180 342
180 927
181 999
181 528
181 707
182 746
182 942
182 415
182 758
183 931
183 913
183 590
183 761
184 301
184 972
184 617
185 944
185 452
185 423
185 784
186 767
186 339
187 374
187 646
187 436
188 893
188 562
188 781
189 249
189 487
189 681
190 985
190 292
190 572
191 693
191 484
192 837
192 698
192 254
192 494
193 667
193 349
193 873
194 886
194 811
195 530
195 428
195 708
195 632
196 440
196 872
196 903
196 798
197 511
197 313
197 483
197 516
198 460
198 468
198 659
198 242
199 537
199 324
199 380
200 528
200 880
201 946
201 228
201 965
201 688
202 420
202 643
202 343
202 803
203 712
203 901
203 928
204 591
204 453
204 355
205 661
205 308
206 580
206 765
206 302
207 932
207 996
207 627
207 770
208 591
208 247
208 652
208 939
209 512
209 359
210 925
210 907
210 524
210 553
211 417
211 368
211 746
211 839
212 270
212 670
212 305
212 843
213 502
213 848
213 961
214 291
214 842
214 559
214 625
215 434
215 663
215 303
216 609
217 722
217 759
217 913
217 462
218 748
218 611
218 751
219 841
219 535
219 564
219 458
220 270
220 930
220 513
220 895
221 729
221 353
222 525
222 783
222 825
223 561
223 890
223 922
223 694
224 432
224 530
224 538
224 520
225 353
225 509
225 818
225 584
226 568
226 743
226 497
226 722
227 960
227 235
227 727
228 425
228 603
228 288
229 575
229 687
229 867
229 713
230 598
230 527
230 256
230 683
231 710
231 548
232 498
232 676
233 517
233 257
233 519
234 967
234 633
234 638
234 937
235 663
235 716
235 809
236 839
236 353
236 490
236 870
237 436
237 277
237 656
237 847
238 501
238 344
238 322
238 788
239 471
239 497
240 904
241 365
241 412
241 630
242 749
242 569
242 336
243 504
243 319
243 941
243 355
244 283
244 502
244 888
244 385
245 558
245 815
245 790
246 644
246 884
246 985
247 891
247 397
248 929
248 921
248 768
248 894
249 419
250 475
250 544
250 621
250 754
251 285
251 828
252 519
252 366
253 883
253 369
253 298
254 618
254 259
254 317
255 946
255 486
255 444
256 704
256 773
256 669
257 477
257 548
258 910
258 429
258 531
258 431
259 874
259 871
259 634
260 772
260 456
260 829
260 751
261 491
261 286
261 900
261 984
262 277
262 297
262 308
263 977
263 761
263 526
264 868
264 994
264 756
264 738
265 787
265 425
265 703
265 266
266 610
266 990
266 350
267 957
267 896
267 647
268 866
269 297
269 821
269 567
269 545
270 624
270 553
271 413
271 626
271 658
272 807
272 615
273 364
273 391
273 613
274 554
274 847
274 964
275 279
275 887
276 319
276 978
276 903
277 481
278 911
278 518
278 377
279 375
279 586
280 408
280 481
280 469
280 310
281 961
281 888
281 501
281 918
282 509
282 372
282 658
283 334
283 590
284 499
284 950
284 569
284 893
285 776
285 963
285 404
286 977
286 426
287 944
287 971
287 949
287 511
288 823
288 881
288 917
289 716
289 474
289 307
290 800
290 673
290 312
290 656
291 654
291 420
291 644
292 704
292 718
293 729
293 956
293 580
294 707
294 743
294 762
295 856
295 600
295 595
295 602
296 412
296 535
296 349
296 717
297 947
297 802
298 996
298 324
298 820
299 399
299 431
300 514
300 533
301 522
301 660
301 758
302 774
302 425
303 925
303 809
304 462
304 632
305 769
305 921
306 889
306 591
307 910
307 915
307 894
308 987
308 724
309 908
309 501
310 439
310 789
311 740
311 865
311 449
311 488
312 667
313 752
313 886
313 817
314 766
314 725
314 480
314 857
315 843
315 833
315 363
315 624
316 347
316 723
316 937
316 817
317 812
317 645
318 933
318 439
318 408
319 647
319 779
320 693
320 611
320 949
320 909
321 822
321 331
321 578
322 357
322 338
322 597
323 463
323 325
323 538
324 981
325 854
325 695
326 779
326 723
326 803
327 678
327 492
327 366
328 801
329 731
329 839
329 715
330 658
330 433
330 858
331 668
331 897
331 705
332 692
332 603
332 956
333 568
333 923
333 826
334 913
334 831
335 494
335 982
335 871
336 410
336 562
337 414
337 555
337 502
337 424
338 815
338 619
338 934
339 888
339 831
339 866
340 369
340 737
340 691
340 996
341 418
341 618
341 715
341 368
342 850
342 393
343 559
344 961
344 922
344 496
345 549
345 438
345 545
346 563
346 499
347 752
347 504
347 671
348 605
348 961
348 679
348 728
349 726
349 733
350 386
350 677
351 770
351 914
351 840
352 372
352 396
354 621
355 899
356 753
356 426
357 393
358 679
358 570
358 393
359 392
359 449
360 824
360 793
360 799
360 586
361 948
361 407
361 767
361 814
362 711
362 830
362 546
363 755
363 931
364 484
364 714
364 750
365 401
365 494
366 477
367 882
367 402
367 792
367 475
368 525
369 446
370 582
370 383
370 422
370 416
371 680
371 943
371 666
372 433
372 827
373 749
373 893
373 621
374 800
374 458
374 413
375 959
375 588
375 430
376 810
376 880
376 674
377 553
377 877
377 394
378 717
378 466
378 726
379 549
379 844
379 452
379 485
380 840
380 780
381 902
381 592
381 742
382 676
382 805
382 782
383 919
384 631
384 668
384 797
384 671
385 605
385 409
385 706
386 588
386 885
387 491
387 685
387 435
387 389
388 943
389 586
389 681
389 489
390 720
390 585
391 582
392 560
392 441
393 427
394 405
395 917
395 671
395 937
396 509
396 763
397 889
397 851
398 569
398 450
398 536
399 905
399 916
399 510
400 537
400 981
400 443
400 914
401 532
401 845
402 989
402 865
403 431
403 986
403 448
404 740
404 902
404 676
405 606
405 829
406 630
406 535
406 626
406 584
407 812
407 843
408 436
408 521
409 913
410 662
410 687
410 950
411 792
411 720
411 528
412 837
413 858
414 951
414 706
415 853
416 750
416 970
418 959
418 887
419 526
419 702
420 719
420 991
421 851
421 879
421 592
422 790
422 499
422 536
423 844
423 714
424 936
425 668
426 495
426 674
427 501
427 692
427 636
428 657
429 795
429 455
430 617
430 810
432 945
432 883
433 896
434 795
434 716
434 768
435 595
435 926
435 573
436 907
437 438
437 456
437 951
438 751
438 944
439 612
439 983
440 794
440 649
441 899
442 597
442 529
442 444
443 747
443 543
445 778
445 516
445 803
446 780
446 904
446 477
447 598
447 833
447 931
448 894
448 864
448 470
449 878
450 998
450 648
450 539
451 757
451 541
452 951
453 860
453 735
453 978
454 843
454 587
454 590
455 608
455 716
456 515
456 627
457 915
458 673
459 989
459 676
459 635
460 805
460 867
461 842
461 764
461 849
462 995
462 931
463 634
463 518
464 962
464 826
464 686
465 682
465 521
465 890
466 818
466 655
466 490
467 535
467 733
467 658
467 800
468 539
468 980
469 872
469 859
470 821
470 796
470 549
471 531
471 508
472 724
472 500
472 661
473 819
473 615
473 589
474 955
474 929
474 809
475 707
476 534
476 747
476 834
476 867
477 614
478 869
478 508
479 964
479 575
479 611
479 680
480 878
480 703
480 958
481 577
481 646
482 651
482 526
483 949
483 723
483 778
484 944
485 556
486 771
486 802
487 799
487 628
488 902
488 856
489 889
489 595
489 506
490 641
490 942
491 527
491 574
492 923
492 969
493 918
493 885
493 866
494 599
495 576
495 995
495 598
496 619
496 737
497 759
498 989
498 544
498 659
499 629
500 815
503 882
503 581
503 705
503 542
504 940
504 957
505 879
505 862
506 628
506 602
506 875
507 789
507 912
507 647
508 910
509 801
510 653
510 845
511 784
512 742
512 585
513 807
513 814
513 670
514 701
514 939
514 891
515 848
516 628
518 624
518 755
519 881
519 901
520 755
520 634
520 632
521 920
521 694
522 933
522 807
523 908
523 625
523 764
524 656
524 980
525 942
526 984
527 674
527 718
528 857
529 827
529 818
529 938
531 650
531 966
532 997
532 795
533 898
534 713
534 813
534 909
536 622
537 639
537 884
538 657
539 680
539 554
540 623
540 912
541 635
542 865
543 909
543 739
543 643
544 562
544 749
546 568
546 702
547 669
547 579
547 683
547 833
548 675
548 780
549 555
550 957
550 633
551 924
551 850
551 665
551 570
552 973
552 840
552 651
553 579
554 987
554 656
555 616
556 587
556 804
557 625
557 798
557 642
558 619
559 798
559 789
560 965
560 958
560 797
561 606
561 820
562 700
563 678
563 901
563 970
564 997
564 630
565 745
565 828
565 776
566 988
566 753
567 664
567 652
567 978
569 687
570 636
570 866
571 741
571 822
572 660
573 875
574 835
574 808
575 998
575 693
576 637
576 773
577 859
577 947
577 647
578 581
578 923
579 769
579 993
580 881
580 603
581 743
582 724
582 648
583 974
583 838
584 717
585 740
585 828
586 596
587 769
587 833
588 596
588 760
589 660
589 744
589 607
591 600
592 595
592 615
593 785
593 831
593 679
593 962
594 815
594 873
596 900
597 855
597 692
599 924
599 645
600 851
601 758
601 612
601 682
601 933
602 811
603 610
604 846
604 802
604 613
604 724
605 737
607 983
608 960
608 982
609 801
609 928
610 765
610 836
611 747
612 842
613 777
613 919
614 678
616 652
616 936
616 701
617 746
618 732
619 728
620 744
620 623
620 776
621 708
622 873
622 775
624 721
626 828
627 820
629 712
629 687
629 998
631 940
631 899
631 965
632 637
633 909
633 723
635 955
635 832
636 688
637 816
638 712
638 713
638 693
639 738
639 985
640 777
640 986
640 966
640 979
641 876
641 729
642 794
643 778
643 914
645 831
646 983
646 858
648 987
649 664
649 952
649 852
650 785
652 796
653 860
654 710
655 938
655 855
655 825
657 874
657 873
659 955
659 727
661 733
662 690
662 928
663 841
663 673
664 859
665 992
665 677
666 993
666 906
667 841
667 960
668 823
669 911
670 948
671 822
672 945
672 738
673 925
674 773
675 974
675 756
677 787
677 725
679 888
680 867
681 984
682 783
682 849
683 808
684 994
684 781
684 974
685 810
686 785
686 966
686 935
688 787
688 850
689 991
689 765
690 806
690 713
691 973
691 830
692 908
695 920
695 890
695 783
697 934
697 788
697 825
697 890
698 715
699 955
699 805
699 993
700 792
701 976
701 921
702 977
703 705
704 906
705 797
706 932
708 781
709 857
709 753
709 760
711 897
711 774
711 730
712 970
714 986
717 731
718 782
719 884
719 914
720 766
720 878
721 812
721 814
722 736
725 760
726 938
727 749
727 754
730 743
731 837
731 954
732 837
733 827
734 951
734 932
734 971
735 941
735 927
736 995
736 977
738 773
741 750
742 879
744 963
745 801
746 870
747 943
748 981
748 943
748 829
750 979
751 964
752 811
753 900
757 835
757 804
759 962
760 988
761 892
762 857
762 882
763 881
763 786
764 788
764 855
766 954
768 864
769 929
770 981
771 896
771 941
771 947
772 847
774 990
775 790
776 806
777 863
779 968
781 999
782 926
783 975
786 917
786 967
787 958
789 903
791 813
791 834
792 999
794 799
796 860
796 976
798 968
799 889
802 927
804 892
804 808
805 906
806 813
807 972
809 980
810 900
811 861
814 887
816 995
817 949
819 963
819 926
820 829
824 885
825 849
826 969
832 869
832 915
834 906
835 875
836 908
838 994
838 999
840 996
844 894
846 863
848 922
848 952
849 942
850 905
851 939
852 936
853 876
853 868
854 934
855 956
856 861
859 903
860 916
861 899
863 935
864 976
868 985
869 989
870 876
872 952
875 886
877 907
877 920
878 882
879 898
880 994
883 904
887 972
891 948
891 936
895 907
897 923
902 926
910 986
911 945
912 983
916 927
917 940
919 979
919 935
920 930
928 967
930 975
930 933
932 973
940 953
941 953
946 953
947 978
958 992
969 979
980 993
988 990
"""

