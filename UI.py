import tkinter as tk

from tkinter import filedialog

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Caller App")

        self.button1 = tk.Button(self.root, text="Call Function 1", command=self.call_function1)
        self.button1.pack(pady=20)

        self.button2 = tk.Button(self.root, text="Call Function 2", command=self.call_function2)
        self.button2.pack(pady=20)

    def call_function1(self):
        file_path = filedialog.askopenfilename(title="Select a JPEG or PNG file",
                                               filetypes=[("JPEG files", "*.jpg *.jpeg"), ("PNG files", "*.png")])
        if file_path:
            print("Selected file:", file_path)
            self.run_model(file_path)
            return file_path
        else:
            print("No file selected")
            return None
        
    def run_model(self, file_path):
        # Call the runmodels.py script with the selected file path
        import subprocess
        subprocess.run(["python", "MLTest//RunModels.py", file_path])
        
    
    

    
    def call_function2(self):
            print("Calling Function 2:")
            import subprocess
            subprocess.run(["python", "MLTest\\RunModels.py", "1"])

    def run_model(self, file_path):
        import subprocess
            # Call the runmodels.py script with the selected file path
        subprocess.run(["python", "MLTest\\RunModels.py", "2", file_path])

            # Replace this with the code for your second function
    print("Function 2 called")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()