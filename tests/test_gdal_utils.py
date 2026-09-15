"""Example test for the geospatial helpers.

Marked "heavy" because it needs rasterio/GDAL, which are only available in
the conda environment (not in the light CI job). Run with:  make test-all
"""

import numpy as np
import pytest

rasterio = pytest.importorskip("rasterio")
shapely = pytest.importorskip("shapely")

from rasterio.transform import from_origin
from shapely.geometry import LineString

from wrr.gdal_utils import sample_profile_from_raster

pytestmark = pytest.mark.heavy


def test_sample_profile_from_constant_raster(tmp_path):
    # Build a tiny 10x10 raster filled with elevation 42.0 m ...
    raster_path = tmp_path / "dem.tif"
    profile = {
        "driver": "GTiff",
        "width": 10,
        "height": 10,
        "count": 1,
        "dtype": "float32",
        "crs": "EPSG:25832",
        "transform": from_origin(0.0, 10.0, 1.0, 1.0),  # 1 m pixels
    }
    with rasterio.open(raster_path, "w", **profile) as dst:
        dst.write(np.full((10, 10), 42.0, dtype="float32"), 1)

    # ... then sample a profile along a diagonal line through it.
    line = LineString([(1.0, 1.0), (9.0, 9.0)])
    s, xy, z = sample_profile_from_raster(str(raster_path), line, npts=20)

    assert len(s) == len(z) == 20
    assert xy.shape == (20, 2)
    assert s[-1] == pytest.approx(line.length)
    assert np.allclose(z, 42.0)  # every sample must hit the constant elevation
