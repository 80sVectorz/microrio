def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def on_button_pressed_a():
    global plr_pos,view_pos,world
    if plr_pos[0]-1 <= view_pos[0]:
        view_pos[0]-=1
    elif world[ plr_pos[1]][clamp(plr_pos[0] - 1, 0, len(world[0]))] == 0:
        plr_pos = [clamp(plr_pos[0] - 1, 0, len(world[0])), plr_pos[1]]
input.on_button_pressed(Button.A, on_button_pressed_a)

def draw():
    global world, plr_pos,view_pos
    for y in range(5):
        for x in range(5):
            if world[y][view_pos[0]+x] > 0:
                led.plot_brightness(x, y, 255)
            else:
                led.plot_brightness(x, y, 0)
            led.plot_brightness(plr_pos[0]-view_pos[0], 4-plr_pos[1], 150)

def on_button_pressed_b():
    global plr_pos,view_pos

    if plr_pos[0]+1 >= view_pos[0]+4:
        view_pos[0]+=2
    elif world[plr_pos[1]][clamp(plr_pos[0] + 1, 0, len(world[0]))] == 0:
        plr_pos = [clamp(plr_pos[0] + 1, 0, len(world[0])), plr_pos[1]]
input.on_button_pressed(Button.B, on_button_pressed_b)
world = [
    [0, 0, 0, 0, 0,0,0,0,0],
    [0, 0, 0, 0, 0,1,1,1,0],
    [0, 0, 0, 0, 0,0,0,0,0],
    [0, 1, 1, 1, 1,0,0,0,0],
    [1, 1, 1, 1, 1,0,0,0,0]]
plr_pos = [0, 2]
view_pos = [0,0]
t = 0


def on_forever():
    global plr_pos,t
    if t%5==0:
        if plr_pos[1]-1 < len(world)-1 and world[len(world)-plr_pos[1]][plr_pos[0]] == 0 :
            plr_pos[1]-=1

    draw()
    basic.pause(500)
    t+=1
    #basic.pause(50)

basic.forever(on_forever)
