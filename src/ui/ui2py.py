import sys, os, time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if event.dest_path.endswith('.ui'):
            print(f'{event.dest_path} has been moved, updating .py file')
            filename, file_extension = os.path.splitext(os.path.basename(event.dest_path))
            output_filename = 'ui_' + filename + '.py'
            output_path = os.path.join(os.path.dirname(event.dest_path), output_filename)
            subprocess.run(['pyuic5.exe', event.dest_path, '-o', output_path])

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

