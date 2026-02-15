import vapoursynth as vs
import os

core = vs.core

# Load RIFE plugin from same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
core.std.LoadPlugin(os.path.join(script_dir, "librife.dll"))

# Get video from mpv
clip = video_in

# Scene detection (before color conversion)
clip = core.misc.SCDetect(clip, threshold=0.1)

# Convert to RGBS for RIFE
clip_rgb = core.resize.Bicubic(clip, format=vs.RGBS, matrix_in_s="709")

# RIFE interpolation: 2x frame rate
clip_rgb = core.rife.RIFE(
    clip_rgb,
    model_path=os.path.join(script_dir, "rife-v4.6"),
    factor_num=2,
    factor_den=1,
    gpu_id=0,
    gpu_thread=3,
    sc=True,
)

# Convert back to YUV for output
clip = core.resize.Bicubic(clip_rgb, format=clip.format.id if hasattr(clip, 'format') and clip.format else vs.YUV420P8, matrix_s="709")

clip.set_output()
