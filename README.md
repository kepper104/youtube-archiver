# **YouTube Archiver - README**

## **Overview**
The **YouTube Archiver** is a Python-based program that allows users to download individual YouTube videos, playlists, or even an entire channel's videos. It supports downloading videos in high resolution and ensures compatibility by merging video and audio into widely supported formats.

---

## **Requirements**
1. **Python**:
   - The script requires Python 3.x.
2. **FFmpeg**:
   - Ensure **FFmpeg** is installed and accessible in your system's PATH.
   - Alternatively, place the FFmpeg executable (`ffmpeg.exe` on Windows) in the same directory as this script.
   - [Download FFmpeg](https://ffmpeg.org/download.html)
3. **yt-dlp**:
   - The program uses **yt-dlp** for downloading videos. Ensure **yt-dlp** is installed and accessible in your system's PATH.
   - Alternatively, place the yt-dlp executable (`yt-dlp.exe` on Windows) in the same directory as this script.
   - [Download yt-dlp](https://github.com/yt-dlp/yt-dlp#installation)

---

## **Setup**
1. **Install Python**:
   - Download and install Python 3.x from [python.org](https://www.python.org/).
   - Ensure `pip` (Python's package manager) is installed.

2. **Install Dependencies**:
   - No additional Python dependencies are required for this script.

3. **Place FFmpeg and yt-dlp**:
   - Either ensure both tools are available in your system's PATH or place their executables in the same directory as this script.

---

## **Usage Instructions**
### **Running the Program**
1. **Open a Terminal or Command Prompt**:
   - Navigate to the directory containing the script.
2. **Run the Script**:
   ```bash
   python youtube_archiver.py
   ```

---

### **Program Walkthrough**
1. **Enter the Video or Playlist URL**:
   - For individual videos, paste the video URL.
   - For playlists or channels, paste the playlist URL or channel ID (instructions below).

2. **Specify if It’s a Single Video**:
   - The program asks:
     ```
     Is this a single video? (y/n, default is no):
     ```
   - Type `y` or `yes` if downloading a single video.
   - Press `Enter` for playlists or channels.

3. **Set Resolution**:
   - Default: `1080`
   - You can specify any resolution like `720`, `480`, etc.

4. **Set Output Format**:
   - Default: `mp4`
   - Supports other formats such as `mkv`, `webm`, etc.

5. **Set Output Folder**:
   - Default: `downloads`
   - You can specify a custom directory for saving videos.

---

### **How to Retrieve a Channel ID**
To download all videos from a channel:
1. Open the channel page on YouTube.
2. Navigate to the channel's "About" section (usually on the top, click the "more" button near the channel description).
3. Scroll to the bottom and click **Share channel**.
4. Click on **Copy channel ID** (it will look like `UCjJjavV8vOmu49a3vxPaWtQ`).
5. Paste the Channel ID into the program when prompted.


### **How to Retrieve a playlist link**
YouTube is sometimes wonky about giving the playlist link, so here's how to do it reliably:
1. Open a video from the playlist.
2. Locate the playlist videos box with other videos, right-click on the playlist name and select **Copy link**.
3. Paste the playlist link into the program when prompted.

---

### **Examples**
#### **Downloading a Single Video**
```
Enter the video or playlist URL (or channel ID): https://www.youtube.com/watch?v=wPjHuvulivM
Is this a single video? (y/n, default is no): y  
Enter the desired resolution (default is 1080): 720  
Enter the output file format (default is mp4):  
Enter the output folder (default is 'downloads'):  
```

#### **Downloading a Playlist**
```
Enter the video or playlist URL (or channel ID): https://www.youtube.com/playlist?list=PL03Lrmd9CiGfWBWwmSQS_cFMkUvdLZfV0  
Is this a single video? (y/n, default is no): n  
Enter the desired resolution (default is 1080):  
Enter the output file format (default is mp4):  
Enter the output folder (default is 'downloads'):  
```

#### **Downloading an Entire Channel**
```
Enter the video or playlist URL (or channel ID): UCLHgx4lBoHXxxz6_H_Xm4pA  
Is this a single video? (y/n, default is no): n  
Enter the desired resolution (default is 1080):  
Enter the output file format (default is mp4):  
Enter the output folder (default is 'downloads'):  
```

---

## **Features**
- **Single Video Downloads**: Save any individual YouTube video with ease.
- **Playlist Downloads**: Download complete playlists with one command.
- **Channel Downloads**: Download all videos from a YouTube channel using its Channel ID.
- **Customizable Options**:
  - Resolution (e.g., 1080p, 720p).
  - Output format (e.g., MP4, MKV).
  - Output folder.
- **Merge Audio and Video**: Ensures compatibility by merging video and audio streams using FFmpeg.

---

## **Troubleshooting**
1. **FFmpeg/yt-dlp Not Found**:
   - Ensure FFmpeg and yt-dlp are installed and accessible via PATH or in the same directory as the script.

2. **Invalid Channel/Playlist URL**:
   - Double-check the URL or Channel ID.
   - Follow the instructions in the **How to Retrieve a Channel ID** section.

3. **Script Not Running**:
   - Ensure Python is correctly installed and added to your PATH.

---

## **Roadmap**
- [x] Write a README (with instructions) - Done using chatGPT, but still needs polishing
- [ ] Add option to select absolute download folder path
- [ ] Add option to download video descriptions
- [ ] Add option to download video thumbnails
- [ ] Add option to download video statistics (views, likes, dislikes, comments)
- [ ] Add option to download video captions
- [ ] Add option to download video manual subtitles 
- [ ] Create a text file with the downloaded video information
- [ ] Potentially move to yt-dlp's python API for easier setup and more control
- [ ] Add linux support and instructions
---

Enjoy using the YouTube Archiver! 🚀
