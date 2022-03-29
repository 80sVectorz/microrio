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
        if world[4-(plr_pos[1]+2)][plr_pos[0]+1-view_pos[0]] == 0:
            plr_pos = [clamp(plr_pos[0] + 1, 0, len(world[0])), clamp(plr_pos[1] + 2, 0, len(world))]
input.on_button_pressed(Button.A, on_button_pressed_a)

def draw():
    global world, plr_pos,view_pos,t
    for y in range(5):
        for x in range(5):
            if world[y][view_pos[0]+x] > 0:
                led.plot_brightness(x, y, 255)
            else:
                led.plot_brightness(x, y, 0)
            if 4-plr_pos[1] < 5:
                led.plot_brightness(plr_pos[0]-view_pos[0], 4-plr_pos[1], t%2*100+50)

def on_button_pressed_b():
    global plr_pos,view_pos,r_pressed,l_pressed,world
    if not input.button_is_pressed(Button.A):
        if plr_pos[0]+1 >= view_pos[0]+4:
            view_pos[0]+=2
        elif world[4-plr_pos[1]][plr_pos[0]-view_pos[0]+1] == 0:
            plr_pos = [clamp(plr_pos[0] + 1, 0, len(world[0])), plr_pos[1]]
    else:
        if world[4-(plr_pos[1]+2)][plr_pos[0]-view_pos[0]-1] == 0:
            plr_pos = [clamp(plr_pos[0] - 1, 0, len(world[0])), clamp(plr_pos[1] + 2, 0, len(world))]
input.on_button_pressed(Button.B, on_button_pressed_b)
level1 = [
    [0, 0, 0, 0, 0,0,0,0,0],
    [0, 0, 0, 0, 0,1,1,1,0],
    [0, 0, 0, 0, 0,0,0,0,0],
    [0, 1, 1, 1, 1,0,0,0,0],
    [1, 1, 1, 1, 1,0,0,0,0]]

level2 = [
    [0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0,1,1,1,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0, 1, 1, 1, 1,0,0,0,0,0,1,1,1,0,0,0,0],
    [1, 1, 1, 1, 1,0,0,0,0,0,0,0,0,0,0,0,0]]

level3 = [
    [0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0, 1, 1, 1, 1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [1, 1, 1, 1, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0]]

levels = [level1,level2,level3]
level_start_positions = [[0,2],[0,2],[0,2]]



t = 0
lvl = 0
winLvl = 3
won = False
world = levels[lvl]
plr_pos = level_start_positions[lvl]
view_pos = [0,0]
r_pressed = False
l_pressed = False

def reset(lvl):
    global world,plr_pos,view_pos,t, won
    world = levels[lvl]
    plr_pos = [0, 2]
    view_pos = [0,0]
    t = 0   

def on_forever():
    global plr_pos,t,r_pressed,l_pressed, lvl, winLvl
    if t%4==0:
        if plr_pos[1] - 1 < 0:
            basic.show_icon(IconNames.SKULL)
            basic.pause(1000)
            reset(lvl)
        elif plr_pos[1]-1 < len(world)-1 and world[len(world)-plr_pos[1]][plr_pos[0]] == 0 :
            plr_pos[1]-=1
    if plr_pos[0] >= len(world[0])-1:
        lvl += 1
        if lvl == winLvl:
            won = True
            basic.show_string("Win!")
        else:        
            reset(lvl) 
    draw()
    basic.pause(300)
    t+=1

basic.forever(on_forever)
