from fastapi import APIRouter, HTTPException
from typing import List, Optional, Dict, Any
from pydantic import BaseModel

router = APIRouter()

class VisualizationRequest(BaseModel):
    pipeline_id: str
    visualization_type: str  # histogram, scatter, correlation, etc.
    columns: Optional[List[str]] = None
    parameters: Optional[Dict[str, Any]] = None

class VisualizationUpdate(BaseModel):
    visualization_type: Optional[str] = None
    columns: Optional[List[str]] = None
    parameters: Optional[Dict[str, Any]] = None

@router.get("/visualizations/{visualization_id}")
async def get_visualization(visualization_id: str):
    """
    Get visualization data
    
    Returns the data for a specific visualization.
    """
    pass

@router.post("/visualizations")
async def create_visualization(request: VisualizationRequest):
    """
    Create a new visualization
    
    Generates a visualization based on the specified parameters.
    """
    pass

@router.get("/visualizations")
async def list_visualizations(pipeline_id: Optional[str] = None):
    """
    List all visualizations
    
    Returns all visualizations, optionally filtered by pipeline.
    """
    pass

@router.put("/visualizations/{visualization_id}")
async def update_visualization(visualization_id: str, request: VisualizationUpdate):
    """
    Update a visualization
    
    Updates the configuration of an existing visualization.
    """
    pass

@router.delete("/visualizations/{visualization_id}")
async def delete_visualization(visualization_id: str):
    """
    Delete a visualization
    
    Removes a visualization and its associated data.
    """
    pass

@router.get("/visualizations/{visualization_id}/data")
async def get_visualization_data(visualization_id: str):
    """
    Get visualization data in JSON format
    
    Returns the raw data for a visualization.
    """
    pass

@router.get("/visualizations/{visualization_id}/image")
async def get_visualization_image(visualization_id: str):
    """
    Get visualization as image
    
    Returns a visualization as a PNG/JPEG image.
    """
    pass

@router.get("/visualizations/{visualization_id}/svg")
async def get_visualization_svg(visualization_id: str):
    """
    Get visualization as SVG
    
    Returns a visualization as an SVG image.
    """
    pass

@router.post("/visualizations/{visualization_id}/export")
async def export_visualization(visualization_id: str, format: str = "png"):
    """
    Export visualization
    
    Exports a visualization in the specified format.
    """
    pass

@router.get("/visualizations/types")
async def get_visualization_types():
    """
    Get available visualization types
    
    Returns a list of available visualization types.
    """
    pass

@router.post("/visualizations/{visualization_id}/refresh")
async def refresh_visualization(visualization_id: str):
    """
    Refresh visualization data
    
    Regenerates the visualization with current data.
    """
    pass
