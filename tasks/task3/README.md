# Task 3: Panorama or Bust (The Wider Picture)

**Points: 25** · **Deadline: 31st July, 11:59 PM**

## The Problem

When our systems deploy in the field, documentation is everything. A single narrow photo
of a worksite is useless to the analysis team. We need expansive, highly accurate 1:3
panoramas with scale and directional data. The catch? The camera can only take small,
overlapping snapshots, and naive copy-pasting leaves ugly seams and distorted data.

## Your Mission

Build an image-stitching pipeline — essentially your phone's "Panorama Mode" — that turns
a set of overlapping photos into a single wide, properly annotated panorama, matching the
same standard our field documentation actually needs.

## What You Need To Do

* **Gather Intel** — Go outside and shoot 5–8 overlapping images per site, for 2–3
  different sites.
* **Stitch Them Together** — Build a pipeline that combines your overlapping images into
  a single seamless panorama. You're free to use whatever approach gets you a clean
  result — OpenCV's built-in stitching, a pipeline you build yourself, or anything in
  between.
* **Polish & Annotate** — Blend the seams so they disappear. Crop the final image to a
  strict 1:3 (Height:Width) ratio, and overlay:
  * a scale bar,
  * a cardinal direction arrow (N/E/S/W),
  * and location context for the site (GPS coordinates and elevation — these can be
    approximate/simulated if you're not shooting somewhere you can actually measure them).

## Helpful Resources

* [Image Stitching with OpenCV and Python — PyImageSearch](https://pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/)

Go through this, implement it, and make sure you actually learn the math behind it and
what the code is doing at each step — not just get a panorama out the other end. We will
ask you about this in the next round.

## Working in Docker

This task only needs Python + OpenCV — no ROS or Gazebo required. Run it on your host
machine directly, **or** inside the container, which already has
`opencv-contrib-python` installed. See [`docs/GETTING_STARTED.md`](../../docs/GETTING_STARTED.md)
either way.

If you use the container, work inside `vanguard_ws/src/task3` — it's mounted straight to
this `tasks/task3/` folder, so your files are already in the right place to commit.

## Deliverables

Place everything below directly in this folder (`tasks/task3/`):

1. Your complete Python stitching script.
2. 2–3 finished panoramas that meet the 1:3 ratio and annotation requirements (scale bar,
   cardinal direction, GPS/elevation context).
3. A short, honest report: where did the stitching fail (e.g. repetitive textures, low
   overlap)? How did you fix or bypass these issues?
