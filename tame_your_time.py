import time
import threading
from plyer import notification
from pynput.mouse import Listener

class TimerApp:
    def __init__(self):
        # Change these values to your liking
        self.notification_time_blocks = 15 # Notify every 15 minutes
        self.inactivity_trigger = 30 # Trigger a pause after 30 seconds of mouse inactivity

        # Initialize the timer
        self.is_running = True
        self.last_activity = time.time()
        self.total_active_time = 0
        self.paused = False

    def on_move(self, x, y):
        self.last_activity = time.time()

    def update_timer(self):
        # Start the mouse listener
        listener = Listener(on_move=self.on_move)
        listener.start()

        while self.is_running:
            # Calculate time elapsed since last activity
            elapsed_time = time.time() - self.last_activity

            if elapsed_time > self.inactivity_trigger:
                # Pause the timer if we are not moving the mouse for a while
                self.paused = True
            else:
                # Increment total active time (seconds)
                self.total_active_time += 1

                # Notify once per block of time
                if self.total_active_time % (self.notification_time_blocks * 60) == 0:
                    blocks_passed = self.total_active_time // (self.notification_time_blocks * 60)
                    notification_text = f"You are on the {self.notification_time_blocks} minutes block number: {blocks_passed}"
                    notification.notify(
                        title='Timer Notification',
                        message=notification_text,
                        app_name='Timer',
                        timeout=2
                    )

                # Convert total active time to minutes and seconds format
                minutes, seconds = divmod(int(self.total_active_time), 60)
                timer_text = f"{minutes:02}:{seconds:02}"
                print("\r" + timer_text, end="", flush=True)

            time.sleep(1)  # Sleep for 1 second before the next iteration

        # Stop the mouse listener
        listener.stop()
        listener.join()

    def run(self):
        # Start the timer thread
        timer_thread = threading.Thread(target=self.update_timer)
        timer_thread.start()

        try:
            while self.is_running:
                time.sleep(1)  # Only need to run the timer thread for mouse tracking
        except KeyboardInterrupt:
            # Handle interruption to stop the program
            self.is_running = False
            timer_thread.join()

# Instantiate and run the TimerApp
TimerApp().run()