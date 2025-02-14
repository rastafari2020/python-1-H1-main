# SOCIAL OPLESK

# ALUMNO: ALBERTO TOLEDO 

<br/>

* 1) Para validar los hacks
  pytest test_hack.py -v (ejecuta todos los test)
  pytest test_hack.py::test_hack_1 (ejecuta un test en específico)
  pytest test_hack.py::test_hack_3 -v (ejecuta un test en específico)

  ✔ NOTA: en caso de no reconocer el comando "pytest"
          ejecutar el pytest así: python -m pytest test_hack.py -v

<br/>

|Hacks | Details | 
|----------|---------|
| H-1      | "FOOZIMAN"|
| H-2      | "fooziman" |
| H-3      | "Fooziman" | 
| H-4      | "foozimaN" |
| H-5      | "f00z1m@n" |
| H-6      | [0,1,2,3,4,5] |
| H-7      | [5,4,3,2,1,0] | 
| H-8      | [3,5,7] |
| H-9      | [1,'@',2,'@',3,'@'] |
| H-10      | ["F","0","0","Z","1","M","@","N"] | 

<br/> 

|Hacks | Details | 
|-----------|-------------------------------------|
| 🏆 H-1 | text: "fooziman" output => "FOOZIMAN"|
| 🏆 H-2 | text: "FOOZIMAN" output => "fooziman"|
| 🏆 H-3 | text: "fooziman" output => "Fooziman"|
| 🏆 H-4 | text: "fooziman" output => "foozimaN"|
| 🏆 H-5 | text: "fooziman" output => "f00z1m@n"|
| 🏆 H-6 (FOR) | loop: for [] output => [0,1,2,3,4,5]|
| 🏆 H-7 (WHILE) | loop: while [] output => [5,4,3,2,1,0]|
| 🏆 H-8 | list: [1,3,5,7,9] output => [3,5,7]|
| 🏆 H-9 (WHILE) | loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']|
| 🏆 H-10 | text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]|
