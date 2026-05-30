# Big Data Analysis — Climate Change & Sustainable Living

> **Module:** COM745 — Big Data | Ulster University  
> **Author:** Emmanuel Mologe (B00911179)

## Overview

This project analyses four global datasets to understand the current state of climate change and attitudes towards sustainable living. Using a full Hadoop Big Data pipeline — HDFS, Hive, PySpark, and Zeppelin — the study examines trends in EV adoption, CO2 emissions, forest cover, and temperature change across multiple countries (2011–2018).

---

## Problem Statement

Climate change poses a major threat to humanity through rising temperatures, deforestation, increased CO2 emissions, and the need for sustainable energy transitions. This study uses Big Data tools to extract insights from real-world environmental datasets and evaluate progress toward sustainability.

---

## Datasets Used

| Dataset | Source |
|---------|--------|
| IEA Electric Vehicle Data 2023 | [IEA](https://www.iea.org/data-and-statistics/data-product/global-ev-outlook-2023) |
| Temperature Change by Country | [Kaggle](https://www.kaggle.com/datasets/sevgisarac/temperature-change) |
| Total Forest Area (km²) | [Kaggle](https://www.kaggle.com/datasets/shakhuat/total-forest-area-km) |
| Global CO2 Emissions, Intensities & Multipliers | [IMF Climate Data](https://climatedata.imf.org/datasets/7cec1228bfbe4a5e876ca5a5abedd64f0/about) |

---

## Technology Stack

| Tool | Purpose |
|------|--------|
| **Hadoop / HDFS** | Distributed data storage and ingestion |
| **Apache Hive** | SQL-like querying of Hadoop-stored data (HiveQL) |
| **PySpark (Google Colab)** | Distributed data processing and analysis |
| **Apache Zeppelin** | Interactive data visualisation |
| **Apache Ambari** | Hadoop cluster monitoring and management |
| **Python / Pandas** | Supporting data scripts |

---

## Methodology

1. **Data Ingestion** — Datasets imported into HDFS for scalable distributed storage
2. **Data Storage** — Stored and retrieved from HDFS
3. **Data Processing** — Hive (HiveQL) and PySpark used for querying and transformation
4. **Data Analysis** — Trend analysis, sector comparison, and regional comparison across all four datasets
5. **Visualisation** — Apache Zeppelin used for interactive charts and dashboards
6. **Insights** — Findings synthesised into actionable conclusions

---

## Analysis Performed

### EV Dataset
- Country-wise comparison of EV adoption across 10 countries (2011–2018)
- Trend analysis of EV sales growth by vehicle type and region

### CO2 Emissions Dataset
- Sector comparison: Air transport vs Motor Vehicles
- Trend analysis of emission intensities and multipliers over time

### Forest Area Dataset
- Regional comparison of forest cover trends across 10 countries
- Trend analysis of deforestation/reforestation patterns (2011–2018)

### Temperature Change Dataset
- Geographic distribution of warming rates
- Correlation with CO2 emissions and EV adoption data

---

## Key Findings

- EV sales showed consistent growth across most countries, indicating a positive shift toward sustainable transport
- CO2 emissions in key sectors showed gradual decreases in some countries, reflecting the impact of environmental policy
- Forest area trends varied significantly by region, with some countries showing deforestation despite sustainability pledges
- Rising temperatures correlated with high CO2-emitting regions, reinforcing the link between emissions and climate impact

---

## Repository Contents

| File | Description |
|------|-------------|
| `BigDatacw2.ipynb` | Main analysis notebook (PySpark/Colab) |
| `globalCO2emissions.py` | CO2 emissions data processing script |
| `globalEVdata.py` | EV dataset processing script |
| `world_forest_area.py` | Forest area analysis script |
| `IEA_Global_EV_Data2023.csv` | IEA EV dataset |
| `globalCO2emissions.csv` | CO2 emissions dataset |
| `forest-area-km.csv` | Forest area dataset |
| `Environment_Temperature_change_Data.csv` | Temperature change dataset |

> **Note:** The full Hadoop/Hive pipeline was executed on university infrastructure using Apache Ambari and Zeppelin. The HiveQL queries and Zeppelin notebooks are not included as they were run on the university's Hadoop cluster.

---

## References

1. IEA Global EV Outlook 2023 — https://www.iea.org/data-and-statistics/data-product/global-ev-outlook-2023
2. Temperature Change Dataset — https://www.kaggle.com/datasets/sevgisarac/temperature-change
3. Total Forest Area Dataset — https://www.kaggle.com/datasets/shakhuat/total-forest-area-km
4. CO2 Emissions Data — https://climatedata.imf.org/datasets/7cec1228bfbe4a5e876ca5a5abedd64f0/about
