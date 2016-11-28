# farmlogger

Simple farm model. 

I generated the initial project with Cookiecutter Django so there's a fair
amount of boilerplate. Most of the logic is in the farmlogger/farm app. 
The script that excercises the API is in utility/test_api.py

## Installation

* Install docker
* Install docker-compose and run docker

```
$ pip install docker-compose
$ make run_docker
```

## Tests

To run the tests: 

    $ make manage_docker MANAGE=test

## Assumptions

* Fields will only be fertilized once. This is true for the sample events, but likely wouldn't be in practice. 
* I'm not actually deleting users on user:delete because I want to maintain the record of which users performed certain actions such as planting or fertilizing. Instead I set a deleted attribute and don't allow them to be used for subsequent actions.
* I am however deleting fields on field:delete. The assumption is you don't care about a field anymore after deleting it.

## Places to improve

* Input validation. At this point I'm mostly assuming the events are valid, but in a production system there would be much more validation and matching tests.
* Authentication. In a real system we'd need to authenticate users and verify that they had permissions to modify a field.
* More tests.
* More ways to filter results.

## utility/test_api.py output

```
Requirement #1 Ingest events
line: 5 code: 400 error: {"non_field_errors":["Field 3 does not exist"]}
line: 9 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 10 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 11 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 2"]}
line: 12 code: 400 error: {"non_field_errors":["Field 7 does not exist"]}
line: 14 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 15 code: 400 error: {"non_field_errors":["Field 3 does not exist"]}
line: 16 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 18 code: 400 error: {"non_field_errors":["Field 7 does not exist"]}
line: 21 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 25 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 26 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 27 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 30 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 31 code: 400 error: {"non_field_errors":["Field 18 does not exist"]}
line: 33 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 2"]}
line: 35 code: 400 error: {"non_field_errors":["Field 21 does not exist"]}
line: 38 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 39 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 41 code: 400 error: {"non_field_errors":["Field 25 does not exist"]}
line: 44 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 45 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 48 code: 400 error: {"non_field_errors":["Field 18 does not exist"]}
line: 49 code: 400 error: {"non_field_errors":["Field 21 does not exist"]}
line: 51 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 53 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 54 code: 400 error: {"non_field_errors":["Field 7 does not exist"]}
line: 55 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 56 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 58 code: 400 error: {"non_field_errors":["Field 36 does not exist"]}
line: 60 code: 400 error: {"non_field_errors":["Field 21 does not exist"]}
line: 61 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 62 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 63 code: 400 error: {"non_field_errors":["Field 41 does not exist"]}
line: 65 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 66 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 67 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 68 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 69 code: 400 error: {"non_field_errors":["Field 18 does not exist"]}
line: 71 code: 400 error: {"non_field_errors":["Field 36 does not exist"]}
line: 73 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 74 code: 400 error: {"non_field_errors":["Field 8 does not exist"]}
line: 75 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 78 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 84 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 85 code: 400 error: {"non_field_errors":["Field 43 does not exist"]}
line: 86 code: 400 error: {"non_field_errors":["Field 25 does not exist"]}
line: 89 code: 400 error: {"non_field_errors":["Field 41 does not exist"]}
line: 91 code: 400 error: {"non_field_errors":["Field 51 does not exist"]}
line: 93 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 94 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 95 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 97 code: 400 error: {"non_field_errors":["Field 56 does not exist"]}
line: 98 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 100 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 101 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 102 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 103 code: 400 error: {"non_field_errors":["Field 61 does not exist"]}
line: 105 code: 400 error: {"non_field_errors":["Field 36 does not exist"]}
line: 106 code: 400 error: {"non_field_errors":["Field 61 does not exist"]}
line: 107 code: 400 error: {"non_field_errors":["Field 41 does not exist"]}
line: 108 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 110 code: 400 error: {"non_field_errors":["Field 56 does not exist"]}
line: 112 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 113 code: 400 error: {"non_field_errors":["Field 61 does not exist"]}
line: 114 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 115 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 116 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 120 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 121 code: 400 error: {"non_field_errors":["Field 61 does not exist"]}
line: 122 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 123 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 124 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 125 code: 400 error: {"non_field_errors":["Field 43 does not exist"]}
line: 128 code: 400 error: {"non_field_errors":["Field 72 does not exist"]}
line: 129 code: 400 error: {"non_field_errors":["Field 73 does not exist"]}
line: 132 code: 400 error: {"non_field_errors":["Field 71 does not exist"]}
line: 133 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 134 code: 400 error: {"non_field_errors":["Field 73 does not exist"]}
line: 136 code: 400 error: {"non_field_errors":["Field 61 does not exist"]}
line: 137 code: 400 error: {"non_field_errors":["Field 71 does not exist"]}
line: 138 code: 400 error: {"non_field_errors":["Field 73 does not exist"]}
line: 139 code: 400 error: {"non_field_errors":["Field 80 does not exist"]}
line: 141 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 2"]}
line: 142 code: 400 error: {"non_field_errors":["Field 61 does not exist"]}
line: 143 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 144 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 145 code: 400 error: {"non_field_errors":["Field 72 does not exist"]}
line: 146 code: 400 error: {"non_field_errors":["Field 86 does not exist"]}
line: 149 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 150 code: 400 error: {"non_field_errors":["Field 87 does not exist"]}
line: 151 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 152 code: 400 error: {"non_field_errors":["Field 80 does not exist"]}
line: 155 code: 400 error: {"non_field_errors":["Field 91 does not exist"]}
line: 158 code: 400 error: {"non_field_errors":["Field 86 does not exist"]}
line: 159 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 160 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 161 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 163 code: 400 error: {"non_field_errors":["Field 87 does not exist"]}
line: 166 code: 400 error: {"non_field_errors":["Field 98 does not exist"]}
line: 168 code: 400 error: {"non_field_errors":["Field 43 does not exist"]}
line: 169 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 170 code: 400 error: {"non_field_errors":["Field 71 does not exist"]}
line: 172 code: 400 error: {"non_field_errors":["Field 87 does not exist"]}
line: 173 code: 400 error: {"non_field_errors":["Field 98 does not exist"]}
line: 175 code: 400 error: {"non_field_errors":["Field 30 does not exist"]}
line: 176 code: 400 error: {"non_field_errors":["Field 91 does not exist"]}
line: 177 code: 400 error: {"non_field_errors":["Field 86 does not exist"]}
line: 178 code: 400 error: {"non_field_errors":["Field 106 does not exist"]}
line: 180 code: 400 error: {"non_field_errors":["Field 25 does not exist"]}
line: 181 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 182 code: 400 error: {"non_field_errors":["Field 113 does not exist"]}
line: 183 code: 400 error: {"non_field_errors":["Field 106 does not exist"]}
line: 184 code: 400 error: {"non_field_errors":["Field 91 does not exist"]}
line: 185 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 186 code: 400 error: {"non_field_errors":["Field 25 does not exist"]}
line: 187 code: 400 error: {"non_field_errors":["Field 113 does not exist"]}
line: 188 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 189 code: 400 error: {"non_field_errors":["Field 98 does not exist"]}
line: 190 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 192 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 193 code: 400 error: {"non_field_errors":["Field 72 does not exist"]}
line: 194 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 196 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 197 code: 400 error: {"non_field_errors":["Field 118 does not exist"]}
line: 198 code: 400 error: {"non_field_errors":["Field 80 does not exist"]}
line: 199 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 200 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 202 code: 400 error: {"non_field_errors":["Field 120 does not exist"]}
line: 204 code: 400 error: {"non_field_errors":["Field 118 does not exist"]}
line: 205 code: 400 error: {"non_field_errors":["Field 113 does not exist"]}
line: 206 code: 400 error: {"non_field_errors":["Field 118 does not exist"]}
line: 207 code: 400 error: {"non_field_errors":["Field 120 does not exist"]}
line: 208 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 210 code: 400 error: {"non_field_errors":["Field 126 does not exist"]}
line: 211 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 213 code: 400 error: {"non_field_errors":["Field 120 does not exist"]}
line: 214 code: 400 error: {"non_field_errors":["Field 126 does not exist"]}
line: 219 code: 400 error: {"non_field_errors":["Field 72 does not exist"]}
line: 220 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 29"]}
line: 221 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 222 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 223 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 104"]}
line: 224 code: 400 error: {"non_field_errors":["Field 126 does not exist"]}
line: 226 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 229 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 230 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 231 code: 400 error: {"non_field_errors":["Field 135 does not exist"]}
line: 232 code: 400 error: {"non_field_errors":["Field 136 does not exist"]}
line: 233 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 104"]}
line: 234 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 236 code: 400 error: {"non_field_errors":["Field 136 does not exist"]}
line: 238 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 240 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 241 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 242 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 96"]}
line: 243 code: 400 error: {"non_field_errors":["Field 142 does not exist"]}
line: 244 code: 400 error: {"non_field_errors":["Field 145 does not exist"]}
line: 245 code: 400 error: {"non_field_errors":["Field 147 does not exist"]}
line: 246 code: 400 error: {"non_field_errors":["Field 135 does not exist"]}
line: 247 code: 400 error: {"non_field_errors":["Field 136 does not exist"]}
line: 250 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 251 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 253 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 254 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 255 code: 400 error: {"non_field_errors":["Field 154 does not exist"]}
line: 256 code: 400 error: {"non_field_errors":["Field 156 does not exist"]}
line: 257 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 96"]}
line: 258 code: 400 error: {"non_field_errors":["Field 142 does not exist"]}
line: 260 code: 400 error: {"non_field_errors":["Field 159 does not exist"]}
line: 262 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 263 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 264 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 117"]}
line: 265 code: 400 error: {"non_field_errors":["Field 156 does not exist"]}
line: 266 code: 400 error: {"non_field_errors":["Field 154 does not exist"]}
line: 267 code: 400 error: {"non_field_errors":["Field 155 does not exist"]}
line: 268 code: 400 error: {"non_field_errors":["Field 156 does not exist"]}
line: 269 code: 400 error: {"non_field_errors":["Field 159 does not exist"]}
line: 270 code: 400 error: {"non_field_errors":["Field 106 does not exist"]}
line: 271 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 272 code: 400 error: {"non_field_errors":["Field 145 does not exist"]}
line: 273 code: 400 error: {"non_field_errors":["Field 146 does not exist"]}
line: 275 code: 400 error: {"non_field_errors":["Field 164 does not exist"]}
line: 276 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 277 code: 400 error: {"non_field_errors":["Field 135 does not exist"]}
line: 279 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 282 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 117"]}
line: 283 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 284 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 285 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 286 code: 400 error: {"non_field_errors":["Field 155 does not exist"]}
line: 287 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 96"]}
line: 288 code: 400 error: {"non_field_errors":["Field 142 does not exist"]}
line: 289 code: 400 error: {"non_field_errors":["Field 146 does not exist"]}
line: 291 code: 400 error: {"non_field_errors":["Field 163 does not exist"]}
line: 292 code: 400 error: {"non_field_errors":["Field 164 does not exist"]}
line: 293 code: 400 error: {"non_field_errors":["Field 181 does not exist"]}
line: 297 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 298 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 2"]}
line: 300 code: 400 error: {"non_field_errors":["Field 189 does not exist"]}
line: 302 code: 400 error: {"non_field_errors":["Field 164 does not exist"]}
line: 303 code: 400 error: {"non_field_errors":["Field 155 does not exist"]}
line: 304 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 305 code: 400 error: {"non_field_errors":["Field 156 does not exist"]}
line: 306 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 96"]}
line: 307 code: 400 error: {"non_field_errors":["Field 142 does not exist"]}
line: 308 code: 400 error: {"non_field_errors":["Field 147 does not exist"]}
line: 310 code: 400 error: {"non_field_errors":["Field 163 does not exist"]}
line: 311 code: 400 error: {"non_field_errors":["Field 178 does not exist"]}
line: 313 code: 400 error: {"non_field_errors":["Field 193 does not exist"]}
line: 315 code: 400 error: {"non_field_errors":["Field 145 does not exist"]}
line: 316 code: 400 error: {"non_field_errors":["Field 189 does not exist"]}
line: 318 code: 400 error: {"non_field_errors":["Field 189 does not exist"]}
line: 320 code: 400 error: {"non_field_errors":["Field 163 does not exist"]}
line: 321 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 322 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 323 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 324 code: 400 error: {"non_field_errors":["Field 194 does not exist"]}
line: 325 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 104"]}
line: 327 code: 400 error: {"non_field_errors":["Field 203 does not exist"]}
line: 328 code: 400 error: {"non_field_errors":["Field 204 does not exist"]}
line: 329 code: 400 error: {"non_field_errors":["Field 205 does not exist"]}
line: 330 code: 400 error: {"non_field_errors":["Field 179 does not exist"]}
line: 331 code: 400 error: {"non_field_errors":["Field 194 does not exist"]}
line: 333 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 336 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 337 code: 400 error: {"non_field_errors":["Field 179 does not exist"]}
line: 338 code: 400 error: {"non_field_errors":["Field 128 does not exist"]}
line: 339 code: 400 error: {"non_field_errors":["Field 147 does not exist"]}
line: 340 code: 400 error: {"non_field_errors":["Field 159 does not exist"]}
line: 341 code: 400 error: {"non_field_errors":["Field 178 does not exist"]}
line: 342 code: 400 error: {"non_field_errors":["Field 200 does not exist"]}
line: 343 code: 400 error: {"non_field_errors":["Field 203 does not exist"]}
line: 344 code: 400 error: {"non_field_errors":["Field 204 does not exist"]}
line: 345 code: 400 error: {"non_field_errors":["Field 179 does not exist"]}
line: 346 code: 400 error: {"non_field_errors":["Field 181 does not exist"]}
line: 347 code: 400 error: {"non_field_errors":["Field 212 does not exist"]}
line: 348 code: 400 error: {"non_field_errors":["Field 214 does not exist"]}
line: 350 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 353 code: 400 error: {"non_field_errors":["Field 164 does not exist"]}
line: 354 code: 400 error: {"non_field_errors":["Field 203 does not exist"]}
line: 355 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 356 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 60"]}
line: 357 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 96"]}
line: 358 code: 400 error: {"non_field_errors":["Field 205 does not exist"]}
line: 360 code: 400 error: {"non_field_errors":["Field 200 does not exist"]}
line: 361 code: 400 error: {"non_field_errors":["Field 205 does not exist"]}
line: 363 code: 400 error: {"non_field_errors":["Field 212 does not exist"]}
line: 364 code: 400 error: {"non_field_errors":["Field 214 does not exist"]}
line: 365 code: 400 error: {"non_field_errors":["Field 226 does not exist"]}
line: 366 code: 400 error: {"non_field_errors":["Field 227 does not exist"]}
line: 367 code: 400 error: {"non_field_errors":["Field 228 does not exist"]}
line: 369 code: 400 error: {"non_field_errors":["Field 224 does not exist"]}
line: 371 code: 400 error: {"non_field_errors":["Field 224 does not exist"]}
line: 373 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 4"]}
line: 375 code: 400 error: {"non_field_errors":["Field 154 does not exist"]}
line: 376 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 377 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 40"]}
line: 378 code: 400 error: {"non_field_errors":["Field 228 does not exist"]}
line: 380 code: 400 error: {"non_field_errors":["Field 213 does not exist"]}
line: 381 code: 400 error: {"non_field_errors":["Field 226 does not exist"]}
line: 382 code: 400 error: {"non_field_errors":["Field 227 does not exist"]}
line: 383 code: 400 error: {"non_field_errors":["Field 240 does not exist"]}
line: 384 code: 400 error: {"non_field_errors":["Field 241 does not exist"]}
line: 386 code: 400 error: {"non_field_errors":["Field 141 does not exist"]}
line: 390 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 2"]}
line: 391 code: 400 error: {"non_field_errors":["Field 240 does not exist"]}
line: 393 code: 400 error: {"non_field_errors":["Field 163 does not exist"]}
line: 394 code: 400 error: {"non_field_errors":["Field 62 does not exist"]}
line: 395 code: 400 error: {"non_field_errors":["Field 241 does not exist"]}
line: 396 code: 400 error: {"non_field_errors":["Field 227 does not exist"]}
line: 397 code: 400 error: {"non_field_errors":["Field 193 does not exist"]}
line: 398 code: 400 error: {"non_field_errors":["Field 213 does not exist"]}
line: 399 code: 400 error: {"non_field_errors":["Field 228 does not exist"]}
line: 400 code: 400 error: {"non_field_errors":["Field 240 does not exist"]}
line: 401 code: 400 error: {"non_field_errors":["Field 250 does not exist"]}
line: 403 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 70"]}
line: 404 code: 400 error: {"non_field_errors":["Field 224 does not exist"]}
line: 405 code: 400 error: {"non_field_errors":["Field 258 does not exist"]}
line: 406 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 2"]}
line: 407 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 9"]}
line: 408 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 117"]}
line: 409 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 17"]}
line: 410 code: 400 error: {"non_field_errors":["Field 226 does not exist"]}
line: 411 code: 400 error: {"non_field_errors":["Field 261 does not exist"]}
line: 412 code: 400 error: {"non_field_errors":["Field 262 does not exist"]}
line: 413 code: 400 error: {"non_field_errors":["Field 264 does not exist"]}
line: 414 code: 400 error: {"non_field_errors":["Attempting to perform action with deleted user id: 96"]}
288 errors found

Requirement #2
All events created by user 162

{'timestamp': '2016-11-01T16:56:54.422029Z', 'id': 3112, 'event': 'field:create', 'entity': {'acres': 195, 'name': 'River Road', 'user_id': 162, 'id': 200}}
{'timestamp': '2016-11-01T16:56:55.434948Z', 'id': 3116, 'event': 'field:delete', 'entity': {'acres': 195, 'name': 'River Road', 'user_id': 162, 'id': 200}}
{'timestamp': '2016-11-01T16:56:58.443963Z', 'id': 3132, 'event': 'field:create', 'entity': {'acres': 230, 'name': 'Rock Pile', 'user_id': 162, 'id': 251}}
{'timestamp': '2016-11-01T16:56:59.450263Z', 'id': 3135, 'event': 'fertilizing:create', 'entity': {'id': 269, 'user_id': 162, 'type': 'Urea', 'field_id': 251}}
{'timestamp': '2016-11-01T16:56:54.422141Z', 'id': 3113, 'event': 'fertilizing:create', 'entity': {'id': 202, 'user_id': 162, 'type': 'Urea', 'field_id': 190}}
{'timestamp': '2016-11-01T16:56:51.412467Z', 'id': 3098, 'event': 'user:create', 'entity': {'email': 'mrs._michaela_lynn@example.com', 'id': 162, 'name': 'Mrs. Michaela Lynn'}}
{'timestamp': '2016-11-01T16:56:57.425791Z', 'id': 3125, 'event': 'fertilizing:create', 'entity': {'id': 239, 'user_id': 162, 'type': 'Anhydrous Amonia', 'field_id': 237}}
{'timestamp': '2016-11-01T16:56:58.428413Z', 'id': 3131, 'event': 'planting:create', 'entity': {'id': 249, 'crop': 'Soy', 'user_id': 162, 'field_id': 247}}

Requirement #3
All users who affected field 176

{'created_by': 175, 'acres': 355, 'planting_time': '2016-11-01T16:56:56.437254Z', 'fertilization_time': '2016-11-01T16:56:52.415168Z', 'fertilizer_type': 'Pig Manure', 'crop': 'Fallow', 'id': 176, 'fertilized_by': 127, 'name': 'Rock Pile', 'last_rainfall': '2016-11-01T16:56:54.417323Z', 'total_rainfall': 3.33615955648575, 'planted_by': 127}
Created by: {'email': 'scott_cunningham@example.com', 'id': 175, 'name': 'Scott Cunningham', 'deleted': False}
Planted by: {'email': 'joseph_wood@example.com', 'id': 127, 'name': 'Joseph Wood', 'deleted': False}
Fertilized by: {'email': 'joseph_wood@example.com', 'id': 127, 'name': 'Joseph Wood', 'deleted': False}

Requirement #4
All events after 2016-11-01T16:56:55.436642 and before 2016-11-01T16:56:56.437836.

{'timestamp': '2016-11-01T16:56:56.437254Z', 'id': 3120, 'event': 'planting:create', 'entity': {'id': 225, 'crop': 'Fallow', 'user_id': 127, 'field_id': 176}}
{'timestamp': '2016-11-01T16:56:56.422073Z', 'id': 3118, 'event': 'rainfall', 'entity': {'fields': [132, 190], 'end': '2016-11-01T16:56:56.422071', 'start': '2016-11-01T15:53:56.422058', 'amount': 7.192408526551577}}
{'timestamp': '2016-11-01T16:56:56.437197Z', 'id': 3119, 'event': 'field:delete', 'entity': {'acres': 255, 'name': 'Game Land', 'user_id': 175, 'id': 213}}

State of all fields that weren't deleted
{'created_by': 4, 'acres': 190, 'planting_time': '2016-11-01T16:56:19.192280Z', 'fertilization_time': '2016-11-01T16:56:18.191243Z', 'fertilizer_type': 'Chicken Manure', 'crop': 'Fallow', 'id': 6, 'fertilized_by': 9, 'name': 'Game Land', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 9}
{'created_by': 9, 'acres': 300, 'planting_time': '2016-11-01T16:56:18.191385Z', 'fertilization_time': '2016-11-01T16:56:24.221557Z', 'fertilizer_type': 'Pig Manure', 'crop': 'Soy', 'id': 13, 'fertilized_by': 29, 'name': 'Home East', 'last_rainfall': '2016-11-01T16:56:21.206147Z', 'total_rainfall': 6.79291759756111, 'planted_by': 9}
{'created_by': 9, 'acres': 325, 'planting_time': '2016-11-01T16:56:22.212851Z', 'fertilization_time': '2016-11-01T16:56:24.221697Z', 'fertilizer_type': 'MiracleGro', 'crop': 'Wheat', 'id': 22, 'fertilized_by': 29, 'name': 'Back 40', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 17}
{'created_by': 17, 'acres': 70, 'planting_time': '2016-11-01T16:56:25.226310Z', 'fertilization_time': '2016-11-01T16:56:23.217146Z', 'fertilizer_type': 'Urea', 'crop': 'Alfalfa', 'id': 26, 'fertilized_by': 17, 'name': "Fred's Land", 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 29}
{'created_by': 9, 'acres': 195, 'planting_time': '2016-11-01T16:56:20.203900Z', 'fertilization_time': '2016-11-01T16:56:28.240042Z', 'fertilizer_type': 'Urea', 'crop': 'Black Beans', 'id': 16, 'fertilized_by': 40, 'name': "Grandpa's Corner", 'last_rainfall': '2016-11-01T16:56:21.206147Z', 'total_rainfall': 6.79291759756111, 'planted_by': 9}
{'created_by': 29, 'acres': 240, 'planting_time': '2016-11-01T16:56:29.243509Z', 'fertilization_time': '2016-11-01T16:56:28.240306Z', 'fertilizer_type': 'MiracleGro', 'crop': 'Clover', 'id': 45, 'fertilized_by': 29, 'name': 'Back Prarie', 'last_rainfall': '2016-11-01T16:56:29.243025Z', 'total_rainfall': 15.3174058074489, 'planted_by': 40}
{'created_by': 29, 'acres': 320, 'planting_time': '2016-11-01T16:56:33.285692Z', 'fertilization_time': '2016-11-01T16:56:28.240352Z', 'fertilizer_type': 'Chicken Manure', 'crop': 'Alfalfa', 'id': 49, 'fertilized_by': 40, 'name': 'North Place', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 60}
{'created_by': 40, 'acres': 370, 'planting_time': '2016-11-01T16:56:33.285740Z', 'fertilization_time': '2016-11-01T16:56:34.290817Z', 'fertilizer_type': 'Anhydrous Amonia', 'crop': 'Black Beans', 'id': 66, 'fertilized_by': 60, 'name': 'Back Prarie', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 60}
{'created_by': 60, 'acres': 380, 'planting_time': '2016-11-01T16:56:37.302540Z', 'fertilization_time': '2016-11-01T16:56:38.305592Z', 'fertilizer_type': 'Urea', 'crop': 'Black Beans', 'id': 81, 'fertilized_by': 96, 'name': 'North Place', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 70}
{'created_by': 70, 'acres': 150, 'planting_time': '2016-11-01T16:56:37.302732Z', 'fertilization_time': '2016-11-01T16:56:38.305669Z', 'fertilizer_type': 'Anhydrous Amonia', 'crop': 'Corn', 'id': 90, 'fertilized_by': 96, 'name': 'North Place', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 70}
{'created_by': 60, 'acres': 385, 'planting_time': '2016-11-01T16:56:34.291011Z', 'fertilization_time': '2016-11-01T16:56:39.313444Z', 'fertilizer_type': 'Pig Manure', 'crop': 'Soy', 'id': 76, 'fertilized_by': 70, 'name': 'Back 40', 'last_rainfall': '2016-11-01T16:56:35.289462Z', 'total_rainfall': 3.07887464900831, 'planted_by': 70}
{'created_by': 70, 'acres': 70, 'planting_time': '2016-11-01T16:56:44.326129Z', 'fertilization_time': '2016-11-01T16:56:38.305740Z', 'fertilizer_type': 'Pig Manure', 'crop': 'Corn', 'id': 97, 'fertilized_by': 96, 'name': 'Rock Pile', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 117}
{'created_by': 175, 'acres': 355, 'planting_time': '2016-11-01T16:56:56.437254Z', 'fertilization_time': '2016-11-01T16:56:52.415168Z', 'fertilizer_type': 'Pig Manure', 'crop': 'Fallow', 'id': 176, 'fertilized_by': 127, 'name': 'Rock Pile', 'last_rainfall': '2016-11-01T16:56:54.417323Z', 'total_rainfall': 3.33615955648575, 'planted_by': 127}
{'created_by': 104, 'acres': 205, 'planting_time': '2016-11-01T16:56:46.336261Z', 'fertilization_time': '2016-11-01T16:56:56.438221Z', 'fertilizer_type': 'Pig Manure', 'crop': 'Wheat', 'id': 129, 'fertilized_by': 127, 'name': 'Game Land', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 104}
{'created_by': 211, 'acres': 365, 'planting_time': '2016-11-01T16:56:58.428331Z', 'fertilization_time': '2016-11-01T16:56:57.425791Z', 'fertilizer_type': 'Anhydrous Amonia', 'crop': 'Fallow', 'id': 237, 'fertilized_by': 162, 'name': 'Home East', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 211}
{'created_by': 211, 'acres': 310, 'planting_time': '2016-11-01T16:56:58.428413Z', 'fertilization_time': None, 'fertilizer_type': '', 'crop': 'Soy', 'id': 247, 'fertilized_by': None, 'name': "Fred's Land", 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': 162}
{'created_by': 162, 'acres': 230, 'planting_time': None, 'fertilization_time': '2016-11-01T16:56:59.450263Z', 'fertilizer_type': 'Urea', 'crop': '', 'id': 251, 'fertilized_by': 162, 'name': 'Rock Pile', 'last_rainfall': None, 'total_rainfall': 0.0, 'planted_by': None}
```
