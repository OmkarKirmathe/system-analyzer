import tkinter as tk
from tkinter import ttk
import psutil
import time
import threading

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Performance Monitor")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Create labels
        self.cpu_label = ttk.Label(root, text="CPU Usage: ", font=("Arial", 12))
        self.cpu_label.pack(pady=10)

        self.memory_label = ttk.Label(root, text="Memory Usage: ", font=("Arial", 12))
        self.memory_label.pack(pady=10)

        self.disk_label = ttk.Label(root, text="Disk Usage: ", font=("Arial", 12))
        self.disk_label.pack(pady=10)

        self.battery_label = ttk.Label(root, text="Battery: ", font=("Arial", 12))
        self.battery_label.pack(pady=10)

        # Start updating
        self.update_data()

    def update_data(self):
        # CPU
        cpu = psutil.cpu_percent(interval=1)
        self.cpu_label.config(text=f"CPU Usage: {cpu}%")

        # Memory
        memory = psutil.virtual_memory()
        self.memory_label.config(text=f"Memory Usage: {memory.percent}%")

        # Disk
        disk = psutil.disk_usage('/')
        self.disk_label.config(text=f"Disk Usage: {disk.percent}%")

        # Battery (if available)
        battery = psutil.sensors_battery()
        if battery:
            plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
            self.battery_label.config(
                text=f"Battery: {battery.percent}% ({plugged})"
            )
        else:
            self.battery_label.config(text="Battery: Not Available")

        # Update every 2 seconds
        self.root.after(2000, self.update_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
