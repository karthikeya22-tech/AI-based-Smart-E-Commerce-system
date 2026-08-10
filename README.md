# AI-Based Smart E-Commerce Recommendation System

## Overview

This notebook presents an AI-based approach for improving product discovery and catalog management in e-commerce platforms using **OpenAI CLIP (ViT-B/32)**. The system uses visual and semantic representations of fashion products to support three major capabilities:

1. **Complementary product recommendation**
2. **Duplicate and near-duplicate product detection for catalog cleaning**
3. **Text-based product search using CLIP**

The notebook works with the **Fashion Product Images Dataset** and processes product metadata, product images, and CLIP-generated image embeddings.

The objective is to demonstrate how a pretrained vision-language model can be integrated into an e-commerce platform to improve product discovery, recommendation, and catalog quality.

---

## Technology Stack

- **Python**
- **PyTorch**
- **OpenAI CLIP**
- **CLIP ViT-B/32**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Pillow**
- **Matplotlib**
- **tqdm**
- **Kaggle Dataset**

---

# Dataset Preparation

The notebook uses the Fashion Product Images Dataset available through Kaggle.

The dataset contains:

- Product metadata stored as JSON files
- Product images stored as JPG files
- Product IDs
- Gender
- Master category
- Sub-category
- Article type
- Base colour
- Season
- Usage
- Product display name

The notebook first discovers the dataset location and loads the product metadata from the JSON files.

For every product, the following information is extracted:

```text
id
gender
masterCategory
subCategory
articleType
baseColour
season
usage
productDisplayName
image_path
