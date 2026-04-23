import traceback
try:
    with open('diary.txt', 'a') as file:
        diary_entry = input("What happened today?")
        diary_line = ""
        while diary_line != "done for now":
            diary_line = input("What else?")
            diary_entry += "\n" + diary_line
        file.write(diary_entry + "\n")
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")  