from pynput.keyboard import Key, Listener
import datetime

sentence = "An Ethical Hacker is a skilled professional who has excellent technical knowledge \n" \
           "and skills and knows how to identify and exploit vulnerabilities in target systems. \n" \
           "He works with the permission of the owners of systems. An ethical Hacker must comply \n" \
           "with the rules of the target organization or owner and the law of the land and their aim\n" \
           " is to assess the security posture of a target organization/system."
sentence2 = "the quick brown fox jumped over the lazy dog"
print("Type this as fast as you can!")
print(sentence2)
correct, incorrect = 0, 0
current_index = 0
start_time = datetime.timedelta(0)
keyC = 0
def on_press(key):
    global current_index, correct, incorrect, sentence2, keyC, start_time
    if key == Key.shift:
        pass
    else:
        if key == Key.backspace and current_index > 0:
            current_index -= 1
        elif key == Key.backspace:
            pass
        elif str(key).replace("'", "") == sentence2[current_index] or (key == Key.space and sentence2[current_index] == " "):
            correct += 1
            current_index += 1
            if keyC == 0:
                start_time = datetime.datetime.now()
            keyC += 1

        else:
            incorrect += 1
            current_index += 1
            keyC += 1

def on_release(key):
    global current_index, sentence2, start_time, correct, incorrect
    if current_index >= len(sentence2):
        total_time = datetime.datetime.now() - start_time
        accuracy = (correct / (correct + incorrect))*100
        print(f"Total time taken is {total_time} and with an accuracy of {accuracy}%")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
