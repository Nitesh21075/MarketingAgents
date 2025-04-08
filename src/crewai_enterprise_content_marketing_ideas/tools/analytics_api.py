from crewai.tools import Tool
from typing import Dict, Optional

class AdsAnalyticsTool(Tool):
    """Tool to retrieve advertising analytics data."""
    
    name: str = "Ads Analytics"
    description: str = (
        "Retrieves advertising analytics data for different platforms. "
        "Provides metrics like CTR, CPC, and ROI for the specified platform."
    )

    def _run(self, platform: str) -> str:
        """Retrieves analytics data for the specified platform."""
        mock_data = {
            "Instagram": {"CTR": 2.4, "CPC": 0.5, "ROI": 140},
            "Facebook": {"CTR": 1.8, "CPC": 0.7, "ROI": 120},
            "Twitter": {"CTR": 1.2, "CPC": 0.9, "ROI": 90},
            "LinkedIn": {"CTR": 0.8, "CPC": 1.2, "ROI": 75},
            "TikTok": {"CTR": 3.1, "CPC": 0.4, "ROI": 160}
        }
        
        if platform in mock_data:
            return str(mock_data[platform])
        return "No data available for the specified platform." 