"""
PCA utility functions for the Manufacturing Analytics Dashboard.

This module includes:
- Fitting PCA
- Extracting explained variance
- Getting PCA scores and loadings
"""

import pandas as pd
from sklearn.decomposition import PCA


def fit_pca(data, n_components=2):
    """Fit PCA model and return fitted model."""
    pca = PCA(n_components=n_components)
    pca.fit(data)
    return pca


def get_explained_variance(pca):
    """Return explained variance ratio."""
    return pca.explained_variance_ratio_


def get_pca_scores(pca, data):
    """Return PCA scores (transformed data)."""
    return pca.transform(data)


def get_pca_loadings(pca, feature_names):
    """Return PCA loadings as a DataFrame."""
    loadings = pd.DataFrame(
        pca.components_.T,
        columns=[f"PC{i+1}" for i in range(pca.n_components_)],
        index=feature_names
    )
    return loadings
