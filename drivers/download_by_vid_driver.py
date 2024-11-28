def test_download_by_vid():
    # Misalnya ID video untuk pengujian
    vid = "sample123"
    extractor = VideoExtractor()
    extractor.download_by_vid(vid)
    assert extractor.vid == vid
    # Assert apakah fungsi prepare dan download terpanggil