import tkinter as tk
import threading
import time


class RefactorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter GUI")
        self.root.geometry("400x300")
        # 创建控件
        self.label = tk.Label(self.root, text="Tkinter GUI")
        self.label.pack()
        self.button = tk.Button(self.root, text="Start", command=self.start)
        self.button.pack()
        self.text = tk.Text(self.root)
        self.text.pack()

    def start(self):
        # 启动线程
        self.thread = threading.Thread(target=self.update_data)
        # DeprecationWarning: setDaemon() is deprecated, set the daemon attribute instead
        self.thread.setDaemon(True)
        self.thread.start()

    def update_data(self):
        while True:
            # 模拟数据更新
            data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 在GUI主线程中更新控件
            self.root.after(0, self.text.insert, tk.END, data + '\n')
            time.sleep(1)


if __name__ == '__main__':
    root = tk.Tk()
    app = RefactorGUI(root)
    root.mainloop()
