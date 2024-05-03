

<!-- README.md is generated from README.qmd. Please edit that file -->

# Python controls for the OBSBOT Tiny 2

<!-- badges: start -->
<!-- badges: end -->

This Python script allows you to set the AI mode on the OBSBOT Tiny 2
webcam. USB `controlWrite` data was obtained by packet inspection on
Windows with [USBPcap](https://github.com/desowin/usbpcap) and
[Wireshark](https://gitlab.com/wireshark/wireshark), then the Python
script was adapted from the USB replay generated with
[usbrply](https://github.com/JohnDMcMaster/usbrply). Use at your own
risk - hopefully these features will be formally supported on Linux in
the future!

# Usage

To set an AI mode, use: `python obsbot.py -ai <mode>`. The supported
modes include:

- **stop**: Disable the currently active AI mode, returning to a static
  camera
- **normal**: Normal (default) person tracking mode
- **upperbody**: Tracking which focuses on the upper body
- **closeup**: Closeup tracking of the mid-torso and above
- **headless**: Tracking of everything below your head
- **desk**: Tilted down 30 degrees immediately in-front of the camera
  with image warping to show the desk
- **whiteboard**: Using corner indicating stickers, frame the camera and
  warp the image to show a whiteboard
- **hand**: Follows your hands rather than your face/body.
- **group**: Follows a group of people, tracking everyone in frame.

A video showing these tracking modes is available here:
https://www.youtube.com/watch?v=C6RoOf4HDbE
