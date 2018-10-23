## Raspberry Pi eight LED modes

### Requirements: :airplane:
This program contains several lighting modes using Raspberry Pi (any type, but tested on Zero) and is designed for following connection:
![Scheme](static_files/scheme.png)


### Modes (list is not yet complete) :construction:
- [x] allon - Turns all LEDs on

    :red_circle::red_circle: :red_circle: :red_circle: :red_circle: :red_circle: :red_circle: :red_circle:
    
- [x] alloff  - Turns all LEDs off (used mostly in testing)

    :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: 
    
- [x] kitt - Lights LEDs from center to the edges like in Knight Rider

    :black_circle: :black_circle: :black_circle: :red_circle: :red_circle: :black_circle: :black_circle: :black_circle: 
    
    :black_circle: :black_circle: :red_circle: :black_circle: :black_circle: :red_circle: :black_circle: :black_circle: 
    
    :black_circle: :red_circle: :black_circle: :black_circle: :black_circle: :black_circle: :red_circle: :black_circle: 
    
    :red_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :red_circle:
    
- [x] lefttoright - lights LEDs from left to right in a loop

    :red_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle:
    
    :black_circle: :red_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle:
    
    :black_circle: :black_circle: :red_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: 
    
    :black_circle: :black_circle: :black_circle: :red_circle: :black_circle: :black_circle: :black_circle: :black_circle: 
    
    :black_circle: :black_circle: :black_circle: :black_circle: :red_circle: :black_circle: :black_circle: :black_circle: 
    
    :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :red_circle: :black_circle: :black_circle: 
    
    :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :red_circle: :black_circle: 
    
    :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :red_circle:
    
- [x] righttoleft - as in lefttoright, but in the other direction
- [x] tocenter - as in kitt, but from the edges to the middle
    
### Author: :octocat:
@miskopo