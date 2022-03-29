
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def on_button_pressed_a():
    global plr_pos,view_pos,world,r_pressed,l_pressed
    if not input.button_is_pressed(Button.B):
        if plr_pos[0]-1 <= view_pos[0]:
            view_pos[0]-=1
        elif world[4-plr_pos[1]][clamp(plr_pos[0] - 1, 0, len(world[0]))] == 0:
            plr_pos = [clamp(plr_pos[0] - 1, 0, len(world[0])), plr_pos[1]]
    else:
        if world[5-(plr_pos[1]+2)][plr_pos[0]+1-view_pos[0]] == 0:
            r_pos = [clamp(plr_pos[0] + 1, 0, len(world[0])), clamp(plr_pos[1] + 2, 0, len(world))]
input.on_button_pressed(Button.A, on_button_pressed_a)

def draw():
    global world, plr_pos,view_pos,t
    for y in range(5):
        for x in range(5):
            if world[y][view_pos[0]+x] > 0:
                led.plot_brightness(x, y, 255)
            else:
                led.plot_brightness(x, y, 0)
            led.plot_brightness(plr_pos[0]-view_pos[0], 4-plr_pos[1], t%2*100+50)

def on_button_pressed_b():
    global plr_pos,view_pos,r_pressed,l_pressed,world
    if not input.button_is_pressed(Button.A):
        if plr_pos[0]+1 >= view_pos[0]+4:
            view_pos[0]+=2
        elif world[4-plr_pos[1]][plr_pos[0]-view_pos[0]+1] == 0:
            plr_pos = [clamp(plr_pos[0] + 1, 0, len(world[0])), plr_pos[1]]
    else:
        if world[5-(plr_pos[1]+2)][plr_pos[0]-view_pos[0]-1] == 0:
            plr_pos = [clamp(plr_pos[0] - 1, 0, len(world[0])), clamp(plr_pos[1] + 2, 0, len(world))]
input.on_button_pressed(Button.B, on_button_pressed_b)
level1 = [
    [0, 0, 0, 0, 0,0,0,0,0],
    [0, 0, 0, 0, 0,1,1,1,0],
    [0, 0, 0, 0, 0,0,0,0,0],
    [0, 1, 1, 1, 1,0,0,0,0],
    [1, 1, 1, 1, 1,0,0,0,0]]

levels = {1:level1}
level_start_positions = {1:[0,2]}



t = 0
lvl = 1
world = levels[lvl]
plr_pos = level_start_positions[1]
view_pos = [0,0]
r_pressed = False
l_pressed = False

def reset(lvl):
    world = levels[lvl]
    plr_pos = [0, 2]
    view_pos = [0,0]
    t = 0   

def on_forever():
    global plr_pos,t,r_pressed,l_pressed
    if t%5==0:
        if plr_pos[1] - 1 < 0:
            reset(lvl)
        elif plr_pos[1]-1 < len(world)-1 and world[len(world)-plr_pos[1]][plr_pos[0]] == 0 :
            plr_pos[1]-=1
    draw()
    basic.pause(200)
    t+=1
    #basic.pause(50)

basic.forever(on_forever)
