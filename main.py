import os
import subprocess
import logging
import time

# Configure logging
logging.basicConfig(
    filename="yt_downloader.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console_handler)


def resolve_playlist_url(user_input):
    """
    Resolves user input into a playlist URL starting with 'UU'.
    """
    base_url = "https://www.youtube.com/playlist?list="
    if user_input.startswith("UC"):  # Channel ID (starts with UC)
        resolved_url = base_url + user_input.replace("UC", "UU", 1)
        logging.info(f"Resolved UC to UU: {resolved_url}")
        return resolved_url
    elif user_input.startswith("UU"):  # Playlist ID (starts with UU)
        resolved_url = base_url + user_input
        logging.info(f"Using UU playlist directly: {resolved_url}")
        return resolved_url
    elif user_input.startswith("https://www.youtube.com/playlist?list=UC"):  # Channel playlist (URL, starts with UC)
        resolved_url = user_input.replace("list=UC", "list=UU", 1)
        logging.info(f"Resolved UC URL to UU URL: {resolved_url}")
        return resolved_url
    elif user_input.startswith("https://www.youtube.com/playlist?list=UU"):  # Playlist URL (starts with UU)
        logging.info(f"Using UU playlist URL directly: {user_input}")
        return user_input
    elif user_input.startswith("https://www.youtube.com/playlist?list="):  # Generic playlist URL
        logging.info(f"Using generic playlist URL: {user_input}")
        return user_input
    else:
        logging.error("Invalid input. Please provide a valid channel string or playlist URL.")
        return None


def download_video_or_playlist(resolution="1080", file_format="mp4", input_url=None, output_folder="downloads",
                               is_video=False):
    """
    Downloads an individual video or a playlist in the specified resolution and format.
    Saves videos to the specified output folder.
    """
    if not input_url:
        logging.error("No valid input URL provided.")
        return

    # Validate resolution input
    if not resolution.isdigit():
        logging.error("Resolution must be a numeric value (e.g., 720, 1080).")
        return

    # Create the output folder if it doesn't exist
    if is_video:
        output_folder = os.path.join(output_folder, "individual-videos")

    if not os.path.exists(output_folder):
        logging.info(f"Created output folder: {output_folder}")
        os.makedirs(output_folder)

    # Set the output template
    if is_video:
        # Single video download
        template = "%(title)s.%(ext)s"
        logging.info(f"Downloading single video: {input_url}")
    else:
        # Playlist or channel download
        template = "%(playlist_title)s/%(title)s.%(ext)s"
        logging.info(f"Downloading playlist or channel: {input_url}")

    # Build the yt-dlp command
    command = [
        "yt-dlp",
        "-f",
        f"bestvideo[height<={resolution}][vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[height<={resolution}][vcodec^=avc1][acodec^=mp4a]",
        "--merge-output-format", file_format,
        "-o", os.path.join(output_folder, template),
        input_url
    ]

    try:
        logging.info(f"Starting download: Input URL={input_url}, Resolution={resolution}, Format={file_format}")

        # Run the yt-dlp command and capture its output
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ''):
            if "[download]" in line and "%" in line:
                # Show download percentages directly to the user
                print(line.strip(), end="\r", flush=True)
            else:
                # Log other non-progress output
                logging.info(line.strip())
        for line in iter(process.stderr.readline, ''):
            logging.error(line.strip())  # Log each line of stderr

        process.stdout.close()
        process.stderr.close()
        process.wait()

        if process.returncode == 0:
            logging.info(f"Download completed successfully! Videos saved to: {os.path.abspath(output_folder)}")
        else:
            logging.error(f"yt-dlp exited with return code {process.returncode}. Check logs for details.")

    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred during download: {e}")
    except FileNotFoundError:
        logging.error("yt-dlp is not installed or not found in PATH. Please install it first.")


def main():
    # Get user inputs
    logging.info("=== YouTube Archiver Started ===")
    time.sleep(0.5)  # Give the user some time to read the instructions
    user_input = input("Enter the video or playlist URL (or channel ID): ").strip()
    is_video_input = input("Is this a single video? (y/n, default is no): ").strip().lower() in ["y", "yes"]
    resolution = input("Enter the desired resolution (default is 1080): ").strip() or "1080"
    file_format = input("Enter the output file format (default is mp4): ").strip() or "mp4"
    output_folder = input("Enter the output folder (default is 'downloads'): ").strip() or "downloads"

    # Resolve playlist URL if it's not a video
    if not is_video_input:
        user_input = resolve_playlist_url(user_input)

    # Proceed with the download
    if user_input:
        download_video_or_playlist(resolution, file_format, user_input, output_folder, is_video=is_video_input)
    else:
        logging.error("Could not resolve the input URL.")
    logging.info("=== YouTube Archiver Finished ===")
    time.sleep(0.5)
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
