# Bosch-CNC-Edge-Intelligence## Dataset

This project uses the Bosch CNC Machining Dataset.

The dataset is **not included** in this repository.

Download it from the official repository:

https://github.com/MATnani/CNC-Machining-Data

After downloading, place it here:

```text
datasets/
└── bosch_cnc/
    └── data/
        ├── M01/
        ├── M02/
        └── M03/
```
# Dataset Understanding

## Dataset Reference

**Title:**
Smart Data Collection System for Brownfield CNC Milling Machines: A New Benchmark Dataset for Data-Driven Machine Monitoring

**Authors:**
Mohamed-Ali Tnani, Michael Feil, Klaus Diepold

**Publication:**
Procedia CIRP, 2022

**DOI:**
https://doi.org/10.1016/j.procir.2022.04.022

---

# Dataset Overview

The Bosch CNC Machining Dataset is a publicly available industrial benchmark dataset developed for data-driven machine monitoring and predictive maintenance research. The dataset was collected from a real Bosch production environment using an edge-to-cloud data acquisition system installed on brownfield CNC milling machines.

The primary objective of the dataset is to support the development and evaluation of machine learning algorithms for industrial process monitoring under realistic manufacturing conditions.

---

# Key Characteristics

- **Domain:** Smart Manufacturing / Industry 4.0
- **Application:** CNC Milling Process Monitoring
- **Data Source:** Bosch Production Plant
- **Collection Period:** Approximately two years
- **Storage Format:** HDF5 (.h5)
- **Sensor Type:** Three-axis vibration (accelerometer) measurements
- **Classification Labels:** Good and Bad machining processes
- **Data Type:** Multivariate time-series

---

# Industrial Significance

Compared with laboratory datasets, this benchmark captures vibration data from actual industrial production processes. Consequently, the dataset contains variations introduced by different machines, machining operations, environmental conditions, and production scenarios, making it suitable for evaluating robust machine learning models.

---

# Relevance to This Research

This dataset is selected because it aligns with the objectives of this research in Industrial Internet of Things (IIoT) and Edge Intelligence.

Specifically, it supports investigations in:

- Machine condition monitoring
- Fault and anomaly detection
- Predictive maintenance
- Edge AI for industrial systems
- Resource-aware machine learning
- Intelligent edge deployment

---

# Initial Observations

From the preliminary exploration performed in this notebook:

- The dataset follows a hierarchical directory structure organized by machine, machining operation, and quality label.
- Each machining experiment is stored as an individual HDF5 file.
- Each HDF5 file contains a dataset named `vibration_data`.
- The inspected sample contains three synchronized vibration channels with a shape of **(59184, 3)**.
- The vibration measurements are stored using the **float64** data type.
- No additional metadata (e.g., sampling frequency or sensor attributes) is embedded within the HDF5 files and must be obtained from the accompanying dataset documentation.

---

# Research Objective

The objective of this notebook is to investigate the dataset structure, metadata, sensor information, and signal characteristics before proceeding to preprocessing, feature engineering, and machine learning model development.
