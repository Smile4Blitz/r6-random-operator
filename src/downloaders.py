from pytube import YouTube

async def download_youtube(url, output_dir) -> str:
    try:
        # streams
        yt = YouTube(url)
        streams = await yt.streams
        print(1)
        video = await streams.filter(progressive=False, type='video', mime_type="video/webm").order_by('resolution').desc().first()
        print(2)
        audio = await streams.filter(type='audio', mime_type="audio/webm").order_by('abr').desc().first()
        print(3)
        
        print(10)
        # download
        video.download(output_path=output_dir, filename='video.webm',skip_existing=False, timeout=5, max_retries=5)
        audio.download(output_path=output_dir, filename='audio.webm',skip_existing=False, timeout=5, max_retries=5)

        print(20)
        return video.title + '.webm'
    except Exception as ex:
        raise Exception(f'Download failed: {ex}')