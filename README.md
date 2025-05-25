<h1 align="center">
  <img src="https://github.com/LEIII18/MD4LC/blob/main/moon.png" alt="AstroBench Logo" width="35" style="vertical-align: middle; margin-right: 5px;">
  <strong>MD4LC</strong>

<p align="center">
  <sub><em>A Multi-Task Multimodal Remote Sensing Image and Label Dataset for Lunar Craters</em></sub>
</p>

</h1>

<p align="center">
  <img src="https://github.com/LEIII18/MD4LC/blob/main/Illustration%20of%20the%20MD4LC.png" width="600">
</p>

## Dataset Introduction
The MD4LC primarily consists of two components: a multi-source remote sensing dataset of lunar impact craters and a corresponding label set. The remote sensing dataset mainly contains raster data with spatial coordinate information, which is primarily used to represent the topography, morphology, gravitational anomalies, and material composition of lunar impact craters.

The label set is a multi-dimensional knowledge label system formed by team's expert annotators based on the aforementioned Chain of Thought. Specifically, it comprises age classification labels used to assess the relative ages of craters, subtype classification labels representing the morphological features, and bilingual text labels (Chinese and English) that describe the geological characteristics of impact craters.

## Dataset Download
You can download the whole dataset from: https://ondrive/XXXXXXX

## Usage Notes
In order to help users better understand and utilize MDL4L, the detailed construction process and architectural design are outlined below:

### Data Naming Rules
Each label file is linked to the corresponding remote sensing data through a unique crater ID in the format XX_XXE(/W)XX_XXN(/S), which facilitates multimodal data retrieval and matching. This ID represents the crater’s central coordinates in decimal degrees, where the decimal point “.” is replaced by an underscore “_” for programming compatibility. The letters “E” and “W” denote east and west longitudes, while “N” and “S” indicate north and south latitudes, respectively.

### Recommended Application Scenarios
- Classification Tasks: Utilizing multimodal imagery along with age classification labels or crater type labels, the dataset can support the training of models for crater age classification and crater type identification.
- Image-to-Text Task: By combining textual description labels with multimodal imagery, cross-modal generative models can be trained to describe crater morphology, age, and type based on image-text data pairs inputs.
- Extended Application Scenarios: In addition to the aforementioned recommended tasks, this dataset can also be further utilized for other extended scenarios, such as lunar spectral inversion, text-to-image generation, and large-scale tectonic gravity anomaly detection.

### Data Preprocessing Notes
- All image data have been standardized to the Moon 2000 geographical coordinate system and projected using the Azimuthal Equidistant projection, with each crater's center defined as the projection origin.
- •	For multi-source data fusion, it is recommended to perform resampling based on differences in spatial resolution.

### Relative Codes
#### 1. generate_crater_shp_Azimuthal_Equidistant
This code is to Create Azimuthal Equidistant projection shapefiles for lunar impact craters by read the csv file. The CSV must include each crater’s name (in the form XX_XXE(/W)XX_XXN(/S)) and its radius (in km), for example in the table format shown below:
<table align="center">
  <thead>
    <tr>
      <th align="center">filename</th>
      <th align="center">dia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">177_58E58_44S</td>
      <td align="center">25.13</td>
    </tr>
    <tr>
      <td align="center">176_86E59_82S</td>
      <td align="center">26.1</td>
    </tr>
    <tr>
      <td align="center">175_24E61_75S</td>
      <td align="center">28.61</td>
    </tr>
     <td align="center">...</td>
     <td align="center">...</td>
  </tbody>
</table>

#### 2. clip_lunar_raster
After generating the shapefile, users can use this code to clip specified remote sensing raster data, and keeping the clip data's spacial reference is same as the shapefile.

#### 3. calculate_brisque_score
This code is to evaluate the image quality of remote sensing data by calling MATLAB's brisque function, where the handleInvalidValues function is used to handle pixels with NaN, inf and extreme values in the raster data.

## 📧 Contact us
Jianzhong Liu: liujianzhong@mail.gyig.ac.cn

Danhong Lie: leidanhong@mail.gyig.ac.cn
