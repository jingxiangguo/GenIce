# coding: utf-8
"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (22,4,4,8,)
"""

pairs="""
138 34
9 209
168 120
53 71
127 166
31 23
105 122
196 67
143 114
24 171
212 178
115 183
10 188
2 88
1 111
34 49
0 150
174 208
42 195
26 56
197 57
174 142
167 172
41 206
27 98
196 182
20 90
153 123
96 23
39 180
37 175
160 178
29 168
117 186
40 67
197 215
58 139
213 31
187 113
3 132
116 35
80 73
168 154
19 97
2 60
98 44
116 82
145 169
124 189
139 11
13 144
36 50
108 186
157 135
18 12
95 135
127 55
1 118
185 46
119 122
175 63
197 28
205 126
112 169
78 79
128 132
65 28
133 112
177 148
180 110
42 69
143 167
34 103
189 140
64 8
15 190
125 109
130 184
52 67
4 114
87 51
117 103
136 196
202 4
150 65
170 74
9 207
54 186
75 61
131 78
188 27
10 155
54 123
85 86
205 70
151 180
2 172
71 165
59 64
24 94
17 111
57 94
145 157
139 155
51 38
150 113
211 191
77 56
56 102
196 214
10 106
76 147
21 141
26 109
146 66
14 75
18 167
182 79
88 107
164 31
37 134
58 93
84 215
165 209
188 58
30 210
101 102
53 148
130 88
151 116
143 194
136 192
43 101
71 58
183 106
19 113
63 100
60 81
171 138
84 47
65 212
38 123
143 77
51 109
214 92
0 157
134 68
162 152
163 152
124 210
200 49
44 195
187 141
63 39
209 3
54 87
146 45
174 87
206 101
42 172
166 201
15 6
211 114
92 195
186 149
22 38
175 32
199 120
138 121
127 198
181 206
35 179
81 107
200 173
185 173
76 95
21 153
178 215
150 162
37 22
91 108
159 193
158 193
190 27
11 44
88 69
90 176
42 12
137 13
109 208
127 124
106 79
62 113
77 110
207 132
59 161
17 100
41 199
40 198
159 62
43 199
68 161
51 83
32 122
57 204
14 189
129 119
69 147
61 129
182 72
97 182
73 177
160 117
18 202
16 142
25 159
104 6
24 46
20 69
139 169
158 96
89 7
100 122
97 166
87 171
80 131
140 146
0 112
36 33
1 154
161 203
115 53
133 155
176 57
32 23
172 98
61 105
20 92
198 146
10 81
128 191
19 5
7 30
115 44
6 181
181 7
63 86
183 131
54 203
167 118
128 76
145 3
60 27
203 8
134 39
48 62
154 129
189 201
166 99
112 152
128 177
40 62
5 141
89 213
43 68
191 194
93 190
33 210
171 117
195 155
25 149
68 110
66 201
6 154
92 183
104 61
1 179
72 192
83 200
13 184
22 70
53 80
3 184
202 74
18 207
85 126
207 194
173 103
215 95
41 125
37 59
65 185
5 201
14 213
185 187
120 208
22 56
28 144
26 168
165 86
94 121
175 126
135 184
199 142
5 52
212 103
83 16
156 70
176 72
213 210
41 30
125 124
66 67
176 144
70 110
180 194
72 99
205 105
29 77
198 33
55 45
82 148
121 66
94 99
108 153
29 43
133 79
163 52
134 102
73 95
4 102
16 55
82 191
147 84
212 47
151 100
116 85
145 71
130 76
151 205
91 160
211 209
36 140
60 202
170 190
11 148
136 204
74 101
0 78
17 93
165 82
158 75
149 8
160 46
163 131
157 80
111 170
36 75
129 50
136 121
90 106
173 149
83 8
142 203
104 89
138 45
156 123
25 164
24 200
17 35
26 206
40 97
89 32
64 38
137 147
20 204
48 162
156 96
137 12
159 108
15 85
208 140
30 50
74 118
204 84
12 81
162 178
47 192
104 126
161 156
120 50
214 163
14 21
73 152
48 52
133 214
130 211
158 153
19 78
13 107
91 141
197 46
33 193
48 91
2 114
86 93
59 23
11 35
125 16
90 107
29 118
28 135
170 181
115 188
177 169
9 4
137 132
49 55
7 119
192 34
193 31
64 164
144 47
174 45
9 39
25 187
179 98
111 119
15 179
99 49
105 96
21 164
"""

waters="""
0.87352 0.31636 0.64904
0.55954 0.68996 0.27826
0.35802 0.0 0.41702
0.0625 0.31636 0.48547
0.25 0.19136 0.32325
0.75 0.0 0.80746
0.62817 0.0 0.21454
0.64368 0.31004 0.14791
0.14515 0.3032 0.98564
0.12649 0.31636 0.35097
0.5625 0.31636 0.51454
0.75 0.68365 0.43422
0.375 0.5 0.47093
0.25 0.31636 0.56578
0.75 0.0 0.99206
0.67052 0.0 0.2904
0.35485 0.3032 0.98564
0.75 0.5 0.31986
0.328 0.5 0.39034
0.75 0.1782 0.76204
0.43899 0.875 0.60803
0.875 0.0 0.94964
0.12183 0.0 0.14267
0.91882 0.375 0.08679
0.25 0.0 0.83534
0.95618 0.3032 0.90636
0.37817 0.0 0.14267
0.56102 0.125 0.39197
0.12352 0.18504 0.67191
0.35655 0.69681 0.21412
0.58118 0.375 0.08679
0.85485 0.3032 0.01436
0.85632 0.31004 0.14791
0.6875 0.5 0.96797
0.31397 0.5 0.81218
0.75 0.68996 0.35581
0.64515 0.69681 0.01436
0.06081 0.1782 0.16473
0.125 0.0 0.05037
0.06546 0.375 0.28775
0.68897 0.5 0.83179
0.45618 0.3032 0.09364
0.4375 0.68365 0.48547
0.31103 0.5 0.16821
0.6405 0.80865 0.46042
0.41882 0.625 0.91321
0.12817 0.0 0.78546
0.25 0.5 0.68015
0.85655 0.69681 0.78588
0.35632 0.31004 0.85209
0.58118 0.625 0.08679
0.25 0.0 0.00795
0.75 0.82181 0.76204
0.8125 0.0 0.50114
0.14515 0.69681 0.98564
0.41882 0.375 0.91321
0.25 0.0 0.19255
0.32948 0.0 0.7096
0.75 0.31636 0.43422
0.04382 0.3032 0.09364
0.43602 0.19136 0.40536
0.75 0.81496 0.12187
0.81103 0.5 0.83179
0.94046 0.31004 0.27826
0.0625 0.1782 0.02518
0.05954 0.31004 0.72174
0.56081 0.82181 0.83527
0.64346 0.69681 0.78588
0.18897 0.5 0.16821
0.3595 0.80865 0.53959
0.06081 0.82181 0.16473
0.8595 0.19136 0.46042
0.44046 0.31004 0.72174
0.93602 0.80865 0.59464
0.43454 0.375 0.28775
0.75 0.82181 0.03557
0.1405 0.80865 0.53959
0.25 0.82181 0.23797
0.75 0.19136 0.67675
0.62649 0.31636 0.64904
0.85802 0.0 0.58298
0.4375 0.31636 0.48547
0.93899 0.875 0.39197
0.25 0.1782 0.96443
0.25 0.68996 0.64419
0.82948 0.0 0.2904
0.87649 0.18504 0.32809
0.25 0.82181 0.96443
0.3125 0.0 0.49886
0.75 0.18504 0.12187
0.43899 0.125 0.60803
0.9392 0.82181 0.83527
0.56399 0.80865 0.59464
0.75 0.31004 0.35581
0.37183 0.0 0.78546
0.06102 0.875 0.60803
0.91882 0.625 0.08679
0.64346 0.3032 0.78588
0.56102 0.875 0.39197
0.43581 0.18504 0.79934
0.86098 0.5 0.26829
0.35655 0.3032 0.21412
0.25 0.1782 0.23797
0.18603 0.5 0.81218
0.75 0.0 0.16466
0.85632 0.68996 0.14791
0.56399 0.19136 0.59464
0.3595 0.19136 0.53959
0.95618 0.69681 0.90636
0.375 0.0 0.05037
0.14346 0.69681 0.21412
0.63903 0.5 0.26829
0.828 0.5 0.60966
0.85655 0.3032 0.78588
0.25 0.0 0.36311
0.6875 0.0 0.50114
0.87649 0.81496 0.32809
0.14368 0.68996 0.85209
0.43454 0.625 0.28775
0.68603 0.5 0.18782
0.45618 0.69681 0.09364
0.43581 0.81496 0.79934
0.81397 0.5 0.18782
0.0625 0.82181 0.02518
0.5625 0.1782 0.97482
0.4375 0.1782 0.02518
0.87183 0.0 0.21454
0.54382 0.3032 0.90636
0.0625 0.68365 0.48547
0.64368 0.68996 0.14791
0.1875 0.0 0.49886
0.75 0.0 0.63689
0.125 0.5 0.47093
0.672 0.5 0.60966
0.14346 0.3032 0.21412
0.06102 0.125 0.60803
0.44046 0.68996 0.72174
0.25 0.5 0.52332
0.35632 0.68996 0.85209
0.75 0.5 0.47669
0.5625 0.82181 0.97482
0.87817 0.0 0.85734
0.3125 0.5 0.03203
0.25 0.80865 0.32325
0.25 0.31004 0.64419
0.9375 0.31636 0.51454
0.54382 0.69681 0.90636
0.25 0.68365 0.56578
0.8595 0.80865 0.46042
0.08118 0.375 0.91321
0.93454 0.375 0.71226
0.94046 0.68996 0.27826
0.87352 0.68365 0.64904
0.9375 0.82181 0.97482
0.5642 0.81496 0.20067
0.625 0.5 0.52907
0.04382 0.69681 0.09364
0.93602 0.19136 0.59464
0.85485 0.69681 0.01436
0.87353 0.5 0.90239
0.0642 0.81496 0.79934
0.12647 0.5 0.09761
0.93454 0.625 0.71226
0.75 0.80865 0.67675
0.9375 0.1782 0.97482
0.93899 0.125 0.39197
0.56081 0.1782 0.83527
0.37352 0.68365 0.35097
0.4392 0.82181 0.16473
0.875 0.5 0.52907
0.55954 0.31004 0.27826
0.25 0.81496 0.87813
0.43602 0.80865 0.40536
0.14368 0.31004 0.85209
0.35485 0.69681 0.98564
0.93581 0.18504 0.20067
0.37649 0.18504 0.67191
0.9375 0.68365 0.51454
0.05954 0.68996 0.72174
0.62352 0.81496 0.32809
0.06546 0.625 0.28775
0.5642 0.18504 0.20067
0.56546 0.375 0.71226
0.64198 0.0 0.58298
0.1405 0.19136 0.53959
0.0642 0.18504 0.79934
0.08118 0.625 0.91321
0.9392 0.1782 0.83527
0.6405 0.19136 0.46042
0.625 0.0 0.94964
0.62352 0.18504 0.32809
0.06399 0.80865 0.40536
0.36098 0.5 0.73171
0.8125 0.5 0.96797
0.12649 0.68365 0.35097
0.5625 0.68365 0.51454
0.56546 0.625 0.71226
0.17052 0.0 0.7096
0.62647 0.5 0.90239
0.37353 0.5 0.09761
0.25 0.18504 0.87813
0.62183 0.0 0.85734
0.37352 0.31636 0.35097
0.1875 0.5 0.03203
0.37649 0.81496 0.67191
0.93581 0.81496 0.20067
0.4392 0.1782 0.16473
0.172 0.5 0.39034
0.4375 0.82181 0.02518
0.06399 0.19136 0.40536
0.64515 0.3032 0.01436
0.14198 0.0 0.41702
0.13903 0.5 0.73171
0.75 0.1782 0.03557
0.62649 0.68365 0.64904
0.12352 0.81496 0.67191
"""

coord= "relative"

cages="""
12 -0.25 0.0 -0.61171
15 -0.5806 0.0 -0.08484
12 -0.25 0.5 -0.28241
12 0.0 0.0 0.5
12 0.75 0.24015 0.24448
12 0.25 0.0 0.61171
12 0.5 -0.5 0.0
14 -0.25 -0.21278 -0.10073
15 -0.0806 0.0 0.08484
16 0.06793 0.0 0.28436
12 -0.75 -0.24015 -0.24448
12 -0.25 -0.24015 0.24448
12 0.5 0.0 0.5
16 -0.43801 -0.5 -0.60477
16 -0.43207 0.0 -0.28436
12 0.0 0.5 0.0
16 0.43207 0.0 0.28436
12 0.25 -0.26542 0.44186
12 0.49411 -0.5 0.18898
16 -0.06793 0.0 -0.28436
12 -0.25 -0.26542 -0.44186
12 0.25 0.5 0.28241
12 0.00589 0.5 0.18898
12 0.75 0.5 0.07333
16 0.06199 0.5 0.60477
16 0.43801 -0.5 0.60477
12 -0.49411 -0.5 -0.18898
14 0.25 0.21278 0.10073
12 -0.25 0.26542 -0.44186
12 0.25 0.26542 0.44186
12 -0.75 0.24015 -0.24448
15 0.0806 0.0 -0.08484
16 -0.06199 0.5 -0.60477
14 -0.25 0.21278 -0.10073
12 -0.00589 0.5 -0.18898
14 0.25 -0.21278 0.10073
15 0.5806 0.0 0.08484
12 -0.75 0.5 -0.07333
"""

bondlen = 3

celltype = 'rect'

cell = """
22.611830247419306 13.678368557348675 36.90820504451432
"""

density = 0.5655780712548233


