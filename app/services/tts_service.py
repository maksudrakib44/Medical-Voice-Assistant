import pyttsx3
import threading

class TTSService:

    def __init__(self):
        self.thread = None
        self.engine = None
        self.is_speaking = False

    def _init_engine(self):
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        return engine

    def _speak_worker(self, text):

        self.is_speaking = True

        try:
            self.engine = self._init_engine()

            self.engine.say(text)
            self.engine.runAndWait()

        except Exception as e:
            print("TTS Error:", e)

        finally:
            try:
                self.engine.stop()
            except:
                pass

            self.engine = None
            self.is_speaking = False

    def speak(self, text):

        # stop previous speech
        self.stop()

        self.thread = threading.Thread(
            target=self._speak_worker,
            args=(text,),
            daemon=True
        )

        self.thread.start()

    def stop(self):

        try:
            if self.engine:
                self.engine.stop()
        except:
            pass

        self.is_speaking = False