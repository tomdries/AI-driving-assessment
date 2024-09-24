# How AI from Automated Vehicles Can Contribute to the Assessment of Human Driving Behavior

This repository contains the data, analysis code, and the modified version of Openpilot used for the paper "*How AI from Automated Vehicles Can Contribute to the Assessment of Human Driving Behavior*" by Tom Driessen, Olger Siebinga, Thomas de Boer, Dimitra Dodou, Dick de Waard, and Joost de Winter.

## Table of Contents
- [Recordings](#recordings)
- [Openpilot](#openpilot)
  - [Fork Features](#fork-features)
  - [Video/CSV Format](#videocsv-format)
- [Analysis](#analysis)
  - [Steps to Reproduce](#steps-to-reproduce)
- [Methodology](#methodology)
- [Cloning Instructions](#cloning-instructions)

## Recordings

The recordings used in this study were generated in a virtual driving simulator using the **JOAN** framework (Beckers et al., 2023) in **CARLA** (Dosovitskiy et al., 2017). The data includes vehicle dynamics and visual information for three driving scenarios: *Aggressive*, *Calm*, and *Surprise*. They were all demonstrated twice, see the Recordings folder for both recordings. The paper contains only the first recordings.

Recordings are available in this repository and include both the forward-facing video files and CSV files containing vehicle state information.

## Openpilot

Recordings were analyzed using a customized version of [Openpilot](https://github.com/commaai/openpilot), an open-source advanced driver assistance system (comma.ai, 2024). Openpilot was adapted to replay pre-recorded driving scenarios, allowing it to observe human driving behavior and compare it to AI-generated plans.

### Fork Features
Our fork introduces a module that supports playback of forward-facing driving videos combined with vehicle dynamics data. In the analysis, we compared human driver actions to AI's decisions, providing a *level-of-agreement* metric that can be used to assess driving style.

The complete fork of Openpilot is available on GitHub at [this link](https://github.com/tomdries/openpilot), with a `.zip` snapshot of the repository included in the 4TU repository for replication purposes.

### Video/CSV Format
- **Video**: 1928×1208 pixel forward-facing driving video at 20 frames per second.
- **CSV File**: Contains vehicle dynamics data, including speed, steering angle, braking, and throttle inputs for each frame of the video.

This format allows the module to simulate real-time input for Openpilot's AI. Example recordings are provided in this repository, and additional example data can be found in the [4TU Data Repository](https://data.4tu.nl/).

## Analysis

To replicate the plots shown in the paper, follow these steps:

### Steps to Reproduce
1. Download the data from the 4TU repository 

2. Clone the repository and install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the analysis script:
    ```bash
    python analysis.py
    ```


## Methodology

Three driving scenarios were recorded:
- **Aggressive Scenario**: The driver brakes abruptly near stationary buses.
- **Calm Scenario**: The same setup as the Aggressive scenario, but with smooth braking.
- **Surprise Scenario**: A bus suddenly appears from behind a wall, forcing an emergency stop.

These scenarios were fed into the adapted Openpilot system. Openpilot's AI was used to generate predictions about the desired speed and driving behavior. The human driver’s behavior was then compared to these predictions, yielding a *discrepancy score* that could indicate aggressive or appropriate responses to the driving context.

For further details about the methodology, refer to the paper's **Method** section.

## Results

The adapted Openpilot system generated predictions about desired vehicle speed, and these were compared with the actual driving behavior. The AI’s *level-of-agreement* metric, calculated from discrepancies between human and AI decisions, distinguished between necessary and unnecessary harsh braking, as detailed in Figure 4 of the paper.

For more on the results and figures, consult the **Results** and **Discussion** sections of the paper.

## Cloning Instructions

**Clone without submodules (reprodicing plots only):**
```bash
git clone https://github.com/your-username/my-new-repo.git
```

**Clone with submodules (including Openpilot):**

```bash
git clone --recurse-submodules https://github.com/your-username/my-new-repo.git
```


