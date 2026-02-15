# mpv-RIFE

**Real-time AI frame interpolation for any video.** Just play it.

mpv-RIFE is a portable, pre-configured [mpv](https://mpv.io/) bundle that uses [RIFE](https://github.com/hzwer/ECCV2022-RIFE) (Real-Time Intermediate Flow Estimation) to double your video's framerate in real-time using your GPU.

24fps → 48fps. Smooth as butter. Zero setup.

## Demo

Drop any video onto `mpv.exe` — it plays with AI-interpolated frames automatically.

## Features

- 🎬 **Drag & drop** any video file → instant smooth playback
- 🔥 **Real-time** GPU-accelerated interpolation (RIFE v4.6 via ncnn/Vulkan)
- ⌨️ **Ctrl+R** to toggle RIFE on/off during playback
- 📦 **Fully portable** — no installation, no Python, no dependencies
- 🎯 **Scene detection** — no artifacts on cuts
- 🖥️ **Any NVIDIA/AMD/Intel GPU** with Vulkan support

## Requirements

- Windows 10/11 (x86-64)
- GPU with Vulkan support (NVIDIA, AMD, or Intel)
- ~200MB disk space

## Usage

1. Download and extract the zip
2. Drag a video file onto `mpv.exe`
3. That's it

### Keyboard shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+R` | Toggle RIFE on/off |
| `Space` | Play/Pause |
| `←` / `→` | Seek ±5s |
| `↑` / `↓` | Volume |
| `f` | Fullscreen |
| `q` | Quit |

## How it works

mpv-RIFE bundles:
- **mpv** — high-performance video player
- **VapourSynth** — video processing framework (embedded)
- **RIFE ncnn-vulkan** — AI frame interpolation running on GPU via Vulkan
- **RIFE v4.6 model** — state-of-the-art optical flow model

The pipeline: Video → Decode → Scene Detection → RIFE 2x → Display

All processing happens on the GPU in real-time. No temp files, no pre-processing.

## Performance

Tested on RTX 4070 (12GB):
- 1080p 24fps → 48fps: **real-time** (A-V sync: 0.000)
- 4K may require a higher-end GPU

## Configuration

Edit `portable_config/mpv.conf` to customize:

```ini
# Change to 60fps fixed output instead of 2x
# Edit rife.vpy: factor_num=60, factor_den=1, fps_num=60, fps_den=1

# GPU selection (multi-GPU systems)
# Edit rife.vpy: gpu_id=0 (default) or gpu_id=1
```

## Building from source

mpv-RIFE is assembled from:
- [mpv](https://mpv.io/) with VapourSynth support
- [VapourSynth-RIFE-ncnn-Vulkan](https://github.com/styler00dollar/VapourSynth-RIFE-ncnn-Vulkan) plugin
- [RIFE v4.6](https://github.com/hzwer/ECCV2022-RIFE) model weights

## License

MIT License — see [LICENSE](LICENSE)

Components have their own licenses:
- mpv: GPL-2.0+
- VapourSynth: LGPL-2.1
- RIFE ncnn-vulkan: MIT
