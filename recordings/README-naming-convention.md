## File Naming Conventions
All files in the `recordings` folder follow the naming convention outlined below, using the "aggressive" scenario as an example:

- **aggressive_stretched**: Video file of the driving scenario.
- **aggressive_stretched_overlay**: The same video with an overlay plotting vehicle speed (used to verify synchronization).
- **aggressive_joan**: Data recorded from the Joan simulator.
- **aggressive_settings**: Settings for the Joan simulator during this scenario.
- **aggressive_openpilot_df.csv**: Input data to OpenPilot, where each row corresponds to a frame in the video file.
- **aggressive_openpilot_df.csv.out.csv**: Output data from OpenPilot (used for analysis).
- **aggressive_video_df**: The initial data that was downsampled to match the video frame rate, 