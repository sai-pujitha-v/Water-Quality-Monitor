# 💧 Water Quality Monitoring Node

An IoT system designed for real-time monitoring of water safety parameters (pH and Total Dissolved Solids) to ensure compliance with drinking water standards.

## 🚀 Features
- **Dual-Parameter Tracking:** Monitors pH (Acidity/Alkalinity) and TDS (Purity).
- **Safety Classification:** Automatically classifies water as "Safe," "Alert," or "Contaminated."
- **Calibration Mode:** Dynamic software-based calibration for analog sensors.
- **Dynamic WiFi Provisioning:** Simple network setup via Serial Monitor.

## ⚙️ Engineering Logic
- **Hardware:** ESP32 reads analog values from pH and TDS probes.
- **Software:** Python processes the voltage signals and applies the Nernst equation (for pH) and PPM conversion (for TDS) to display human-readable data.
