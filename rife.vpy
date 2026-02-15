import vapoursynth as vs
import os
import ctypes

core = vs.core

# Load RIFE plugin from same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
core.std.LoadPlugin(os.path.join(script_dir, "librife.dll"))

# Get video from mpv
clip = video_in
src_fps = clip.fps.numerator / clip.fps.denominator

# Detect display refresh rate from Windows
def get_display_refresh_rate():
    try:
        user32 = ctypes.windll.user32
        dc = user32.GetDC(0)
        gdi32 = ctypes.windll.gdi32
        refresh = gdi32.GetDeviceCaps(dc, 116)  # VREFRESH
        user32.ReleaseDC(0, dc)
        return refresh if refresh > 0 else 60
    except Exception:
        return 60

display_hz = get_display_refresh_rate()

# Calculate best RIFE factor to match display
raw_factor = display_hz / src_fps

if raw_factor <= 1.2:
    # Source FPS already matches display, pass through
    clip.set_output()
else:
    # Snap to nearest power-of-2 factor
    if raw_factor <= 2.5:
        factor = 2
    elif raw_factor <= 5:
        factor = 4
    else:
        factor = 8

    # Scene detection
    clip = core.misc.SCDetect(clip, threshold=0.1)

    # YUV → RGBS → RIFE → YUV
    clip_rgb = core.resize.Bicubic(clip, format=vs.RGBS, matrix_in_s="709")

    clip_rgb = core.rife.RIFE(
        clip_rgb,
        model_path=os.path.join(script_dir, "rife-v4.6"),
        factor_num=factor,
        factor_den=1,
        gpu_id=0,
        gpu_thread=3,
        sc=True,
    )

    clip = core.resize.Bicubic(clip_rgb, format=vs.YUV420P8, matrix_s="709")
    clip.set_output()
