
> **Document Version**: V1.0 &nbsp;&nbsp;

# Overview

The GTA1000 Series microphone board is a 4-channel MEMS microphone array module designed specifically for far-field voice capture. It is used for voice pre-processing such as multi-channel sound pickup, sound source localization, and noise reduction.

The board connects to the mainboard via a ribbon cable interface and supports single-stage or multi-stage cascade deployment to meet the needs of different array scales.

## Product Models Overview

| Material Number | Product Part Number | Board Type | Dimensions | MIC Spacing |
|:-------:|:---------|:---:|:--------:|:---------:|
| BOD0038 | ASN_4MIC_H6CM_70_70 | Circular | Approx. 70 × 70 mm | 6 cm |
| BOD0043 | ASN_4MIC_4CM_154_15 | Linear | 154 × 15 mm | 4 cm |
| BOD0044 | ASN_4MIC_3.5CM_160_17 | Linear | 160 × 17 mm | 3.5 cm |
| BOD0046 | ASN_4MIC_3.5CM_115_20 | Linear | 115 × 20 mm | 3.5 cm |

# Board Layout and Module Description

## Board Layout

```{figure} /_static/images/G10001_micboard-circular-layout-v1.png  
:align: center  
:width: 85%  
:alt: GTA01 mic board layout  

GTA1000 Series Microphone Board (Circular) Front Layout
```

```{figure} /_static/images/G10002_micboard-circular-back-layout-v1.png  
:align: center  
:width: 55%  
:alt: GTA01 mic board back layout  

GTA1000 Series Microphone Board (Circular) Back Layout
```

```{figure} /_static/images/G10003_micboard-inear-layout-v1.png  
:align: center  
:width: 100%  
:alt: GTA01 mic board layout  

GTA1000 Series Microphone Board (Linear) Front Layout (Using the 154mm × 15mm specification as an example)
```

```{figure} /_static/images/G10004_micboard-linear-back-layout-v1.jpg
:align: center  
:width: 65%
:alt: GTA01 mic board back layout

GTA1000 Series Microphone Board (Linear) Back Layout (Using the 154mm × 15mm specification as an example)
```

```{important} Dimensions and Layout Instructions
The above illustrations use the `154mm × 15 mm` (BOD0043) linear board specification as a layout reference example only.
The GTA1000 Series provides linear microphone boards in various physical dimensions. Although the external dimensions, MIC spacing, and relative positions of each module may vary, the interface definitions and hardware layout logic remain consistent.
```

## Module Description

All models of microphone boards share the same functional architecture and include the following three core modules:

| Module | Silkscreen Marking | Function |
|:----:|:-------:|:-----|
| **Interface A (Upstream)** | JP2 | Connects to the mainboard or the previous-stage microphone board. When used in a single stage, only this port is connected. |
| **Interface B (Downstream)** | JP1 | Connects to the next-stage microphone board, used only when cascading. |
| **MIC × 4** | / | Bottom-port MEMS microphones. Distributed circularly on the circular board, and arranged linearly along the long edge on the linear board. |

**Polarity Marking**: There is a dot mark next to each interface, and the side with the dot indicates the "+" direction. When wiring, you must ensure that the "+" on both ends are aligned ("+" to "+").

## Interface Polarity Quick Reference Table

| Model | Interface A "+" Direction | Interface B "+" Direction |
|:----:|:-------------:|:-------------:|
| BOD0038 (Circular) | Left dot | Right dot |
| BOD0043 (154×15) | Bottom dot | Top dot |
| BOD0044 (160×17) | Right dot | Right dot |
| BOD0046 (115×20) | Top dot | Bottom dot |

```{note}  
The directions vary; please be sure to double-check the table above before wiring. 
```

# Hardware Connection

## Single-Stage Connection (1 microphone board)

Suitable for basic 4-channel sound pickup scenarios.

1. Connect one end of the ribbon cable to the mainboard input.
2. Connect the other end to Interface A on the microphone board, aligning with the "+" mark.
3. Leave Interface B unconnected; no connection is needed.

## Multi-Stage Cascade Connection (≥ 2 microphone boards)

Use the cascade method when expanding to 8 or more channels.

1. Connect the mainboard via a ribbon cable to Interface A of the 1st-stage microphone board.
2. Connect Interface B of the 1st stage via a ribbon cable to Interface A of the 2nd stage.
3. If further expansion is needed, repeat the cascade. Leave Interface B of the final stage unconnected.

# Typical Applications

| Board Type | Typical Products | Sound Pickup Characteristics |
|:---:|:---------|:---------|
| Circular | Smart speakers, desktop conferencing terminals, voice robots | 360° omnidirectional pickup and sound source localization |
| Linear | Smart TVs/Soundbars, smart panels, wall-mounted terminals | Directional beamforming, suppressing lateral noise |
