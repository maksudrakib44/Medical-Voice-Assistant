import whisper

class SpeechService:
    _model = None

    def __init__(self, model_name="base"):
        if SpeechService._model is None:
            SpeechService._model = whisper.load_model(model_name)
        self.model = SpeechService._model

    def transcribe(self, file_path: str) -> str:
        result = self.model.transcribe(file_path)
        return result["text"]