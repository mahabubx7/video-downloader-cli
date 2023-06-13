import argparse
import subprocess

def download_video(url, directory=None, playlist=False, indexing=None, quality=None):
    command = ['yt-dlp', url]

    if directory:
        command.extend(['-o', f'{directory}/%(playlist_index)02d %(title)s.%(ext)s'])
    elif indexing:
        command.extend(['-o', f'{indexing} %(title)s.%(ext)s'])

    if playlist:
        command.append('--yes-playlist')

    if quality:
        command.extend(['-f', f'bestvideo[height<={quality}]+bestaudio/best'])

    subprocess.run(command)

def parse_arguments():
    parser = argparse.ArgumentParser(description='YouTube Video Downloader')
    parser.add_argument('url', help='URL of the video or playlist')
    parser.add_argument('--dir', help='Directory to save the downloaded video(s)')
    parser.add_argument('--playlist', action='store_true', help='Download as playlist')
    parser.add_argument('--indexing', action='store_true', help='indexing format for playlist videos')
    parser.add_argument('--quality', type=int, help='Download video with the specified quality (e.g., 1080)')

    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.playlist and not args.indexing:
        download_video(args.url, args.dir, True, None, args.quality)
    else:
        download_video(args.url, args.dir, args.playlist, args.indexing, args.quality)

if __name__ == '__main__':
    main()
