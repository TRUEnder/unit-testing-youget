from you_get.extractors import VideoExtractor

def test_prepare():
    extractor = VideoExtractor()
    # Langsung panggil prepare dengan data dummy
    extractor.prepare()
    # Pastikan prepare tidak raise error
