from you_get.extractors import VideoExtractor

def test_download():
    extractor = VideoExtractor()
    # Tambahkan stream ID contoh
    extractor.streams = {
        "720p": {"container": "mp4", "size": 5242880, "src": ["http://test.video.com/sample.mp4"]}
    }
    extractor.download(stream_id="720p")
    # Cek apakah file terunduh atau log muncul
