from icecream import ic
import keyboard
import ast
from time import sleep as ts
ic.configureOutput(includeContext=True,prefix='(ic):')
def on_key_press(event):
    if event.event_type == 'down':
        keyhot = ''
        if keyboard.is_pressed('tab'):
            keyhot += 'tab+'
        if keyboard.is_pressed('shift'):
            keyhot += 'shift+'
        if keyboard.is_pressed('ctrl'):
            keyhot += 'ctrl+'
        if keyboard.is_pressed('alt'):
            keyhot += 'alt+'
        if keyboard.is_pressed('win'):
            keyhot += 'win+'
        char = event.name

        return keyhot + char

    # return ''
def rkey(event):
    global tlu,i
    key_pressed = on_key_press(event)
    bool = False
    ic('\n\n')
    if key_pressed in k[-1]:          
        keyboard.unhook_all_hotkeys()

    for tlu in range(len(k)):
        ic(tlu,k[tlu],k[tlu][0],k[tlu][0][0],key_pressed)
        if key_pressed == k[tlu][0][0]:
            bool = True
            ic(k[tlu][0],'ok')
            keyboard.unhook_all_hotkeys()
            # ts(tm)
            for item in k[tlu][1]:
                ic(item)
                hotkey = item[0][0]
                remapped_key = item[1][0]
                keyboard.remap_hotkey(hotkey, remapped_key)
            ts(1)
            break
        else:
            if len(k[-1])==0:continue

            if len(k[-1])==1 and tlu<len(k[-1]):
                if key_pressed == k[-1][tlu] and not bool:
                    bool = True
                    i=i+1
                    if i==len(k)-2:i=0
                    keyboard.unhook_all_hotkeys()
                    # ts(tm)
                    ic('right',i)
                    for item in k[i][1]:
                        hotkey = item[0][0]
                        remapped_key = item[1][0]
                        keyboard.remap_hotkey(hotkey, remapped_key)
                    break
            
            if len(k[-1])==2 and tlu<len(k[-1]):
                ic(k[-1][0])
                ic(k[-1][tlu])
                if key_pressed == k[-1][tlu] and not bool:
                    bool = True
                    i=i+1
                    if i==len(k)-2:i=0
                    keyboard.unhook_all_hotkeys()
                    # ts(tm)
                    ic('left',i)
                    for item in k[i][1]:
                        hotkey = item[0][0]
                        remapped_key = item[1][0]
                        keyboard.remap_hotkey(hotkey, remapped_key)
                    break
                if key_pressed == k[-1][tlu] and not bool:
                    bool = True
                    i=i-1
                    if i==-1:i=len(k)-2
                    keyboard.unhook_all_hotkeys()
                    # ts(tm)
                    ic('right',i)
                    for item in k[i][-2]:
                        hotkey = item[0][0]
                        remapped_key = item[1][0]
                        keyboard.remap_hotkey(hotkey, remapped_key)
                    break
        
tlu = 0
k=[]
with open('date.txt', 'r') as f:
    for line in f:
        data = ast.literal_eval(line.strip())
        if len(data) == 1:
            k.append(data[0])
        else:
            k.append(data)
ic(k[-1])
# ic.disable()
for i in k[tlu][1]:
    keyboard.remap_hotkey(i[0][0],i[1][0])
i=0
keyboard.on_press(rkey)

keyboard.wait('enter+f20+alt')
