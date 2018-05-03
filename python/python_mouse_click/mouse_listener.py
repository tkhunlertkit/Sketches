from pynput.mouse import Listener

buffer_x = 0
buffer_y = 0

def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    global buffer_x
    global buffer_y
    buffer_x = x
    buffer_y = y
    if not pressed:
        # Stop listener
        return False

# Collect events until released
def start_mouse_listen(text_to_display):
    print text_to_display
    with Listener(
        on_click=on_click) as listener:
    	listener.join()
    return buffer_x, buffer_y
