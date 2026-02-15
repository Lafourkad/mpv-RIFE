@echo off
:: mpv-RIFE launcher
:: Launches SVP's mpv with RIFE VapourSynth filter
cd /d "%~dp0"
"C:\Program Files\SVP 4\mpv64\mpv.exe" --config-dir="%~dp0portable_config" --hwdec=no --vf=vapoursynth:rife.vpy --demuxer-max-bytes=512MiB %*
