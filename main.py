import keyboard
import time

prompt = input("enter type prompt here: ")
target_wpm = 100

while(keyboard.is_pressed('enter') == False):
    pass

for char in prompt:
    keyboard.write(char)
    time.sleep(0.08)

'''
var span_arr = document.getElementsByTagName("span")
var current_longest = 0
var current_index = 0

for(var i=0; i<span_arr.length; i++) {
    if(span_arr[i].className === "") {
        if(span_arr[i].textContent.length > current_longest) {
            current_index = i
            current_longest = span_arr[i].textContent.length
        }
    }
}

if(span_arr[current_index-2].textContent.length === 1) {
    console.log(span_arr[current_index-2].textContent + span_arr[current_index-1].textContent + span_arr[current_index].textContent)
} else {
    console.log(span_arr[current_index-1].textContent + span_arr[current_index].textContent)
}
'''
