from you_get.extractors import VideoExtractor

def test_p_stream():
    extractor = VideoExtractor()
    extractor.streams = {
        "1080p": {"container": "mp4", "size": 10485760, "quality": "1080p"}
    }
    extractor.p_stream("1080p")
    # Cek apakah data "1080p" muncul sesuai