# Code repository for the paper: How AI from Automated Vehicles Can Contribute to the Assessment of Human Driving Behavior

This repository contains the code for the paper [How AI from Automated Vehicles Can Contribute to the Assessment of Human Driving Behavior](https://www.researchgate.net/publication/384503616_How_AI_from_automated_driving_systems_can_contribute_to_the_assessment_of_human_driving_behavior) by Tom Driessen, Olger Siebinga, Thomas de Boer, Dimitra Dodou, Dick de Waard, and Joost de Winter.

The purpose of this repository is to:
1. Provide access to the recordings created for the demonstration.
2. Reproduce the figures from the paper using the demonstration data.
3. Provide access to a modified version of Openpilot so it can be used to analyze your own driving recordings. 

## Reproducing the analysis figures
<div align="center">
  <img src="https://github.com/tomdries/AI-driving-assessment/blob/main/output_plot.png" alt="AI Driving Assessment Plot" width="600"/>
</div>

The `analysis.py` code only requires `pandas` and `matplotlib` and uses the files in the `recordings` folder. The full recordings of the scenarios (including video and vehicle data) are in this folder as well. The file naming convention is found in the readme located in that folder.

Cloning the Openpilot submodule from this repository is **not required** to reproduce the images.

## Using Openpilot to analyze other data
To analyze human driving data, we made a fork of the Openpilot repository, which is included in this repository as a submodule. You can clone it directly from the [fork's repository](https://github.com/tomdries/openpilot) (recommended) or from this repository using the `--recurse-submodules` flag in the `git clone` command.

Please follow the installation instructions in `openpilot/tools/README.md` and the replay instructions in `openpilot/tools/sim/README.md`.

## Recording virtual scenarios with JOAN
To record scenarios in the CARLA simulator using the JOAN framework (an extension that allows for human input), please consult the [JOAN repository](https://github.com/tud-hri/joan). Our scenarios were implemented in [CARLA Town 1](https://carla.readthedocs.io/en/latest/map_town01/). The experiment configuration and trajectory for the bus in the surprise scenario can be found in the `joan_experiments/` directory.

## Citations
If you use the data or code presented here, please cite:

```
Driessen, T., Siebinga, O., De Boer, T., Dodou, D., De Waard, D., & De Winter, J. (2024). How AI from Automated Driving Systems Can Contribute to the Assessment of Human Driving Behavior. Robotics, 13(12), 169. https://doi.org/10.3390/robotics13120169
```

