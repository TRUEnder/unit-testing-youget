from you_get.extractors import VideoExtractor

def test_download_by_url():
    # Misalnya URL dummy untuk pengujian
    url = "https://www.youtube.com/watch?v=7E9Ed9DUQoQ"
    extractor = VideoExtractor()
    extractor.download_by_url(url)
    # Assert apakah extractor berhasil set URL dan title
    assert extractor.url == url
    # Bisa juga cek apakah fungsi download berjalan dengan baik

if __name__ == '__main__' :
    test_download_by_url()