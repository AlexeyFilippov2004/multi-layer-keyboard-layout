import threading
import ast
import os
import subprocess

processes = []  
stop_event = threading.Event() 

def print_output(process):
    global stop_event
    while not stop_event.is_set():  
        output = process.stdout.readline()
        if not output: 
            break
        print(f"Raw output from process: {output.strip()}")
        try:
            result_data = ast.literal_eval(output.strip())
            handle_key_press(result_data)
        except Exception as e:
            print(f"Error processing output: {e}")
def handle_key_press(result_data):
    global k  
    i=0
    for n, key_pressed in result_data.items():
        bool = False
        if key_pressed in k[-1][-1] or key_pressed in k[-1][0]:
            terminate_processes()

        for tlu in range(len(k)):
            if key_pressed == k[tlu][0][0]:
                bool = True
                run_blocking_exe(k[tlu][1])  
            else:
                if len(k[-1]) == 0: continue
                if len(k[-1]) < 0 and tlu < len(k[-1]):
                    if key_pressed == k[-1][tlu] and not bool:
                        bool = True
                        i = (i + 1) % (len(k) - 1)
                        run_blocking_exe(k[i][1])
        if key_pressed == k[-1][-1][0]:
            terminate_processes()
            break
            

def run_blocking_exe(args=['']):
    exe_path = os.path.join('reassignment.exe')
    print(f"Executing: {exe_path}, Arguments: {args}")

    process = subprocess.Popen(
        [exe_path] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    processes.append(process)
    global stop_event
    stop_event.clear()  
    output_thread = threading.Thread(target=print_output, args=(process,))
    output_thread.start()
    try:
        output_thread.join()  
    except:
        terminate_processes()
def terminate_processes():
    for process in processes:
        try:
            process.terminate() 
            process.kill() 
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print(f"Process {process.pid} did not terminate in time; killing it.")
            process.kill() 
        except Exception as e:
            print(f"Error terminating process {process.pid}: {e}")
      
tlu = 0
k=[]
with open('date.txt', 'r') as f:
    for line in f:
        data = ast.literal_eval(line.strip())
        if len(data) == 1:
            k.append(data[0])
        else:
            k.append(data)
key=run_blocking_exe(k[tlu][1])