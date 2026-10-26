# 音视频内容加工台 / Audio and Video Workbench

本地查看媒体信息、提取音轨、剪辑、抽帧，生成 SRT/VTT 字幕；可选本地转录，分段缓存便于继续处理。

Inspect media, extract audio, cut clips and frames, and export SRT/VTT subtitles locally, with optional local speech recognition and resumable chunk caches.

Runtime: Python 3.10+, FFmpeg (or imageio-ffmpeg 0.6+), PyAV 14–16, Pillow 12+; optional faster-whisper 1.2+ for local transcription. Version 1.0.1. MIT-0. See SKILL.md and references/input.md. Run tests/smoke.py with the runtime dependencies installed.
