from crewai.tools import Tool
from typing import Dict, List, Optional, Union

class BudgetAllocatorTool(Tool):
    """Tool to allocate advertising budget based on performance data."""
    
    name: str = "Budget Allocator"
    description: str = (
        "Allocates advertising budget across different platforms based on their performance metrics. "
        "Takes performance data as input and returns budget allocation recommendations."
    )

    def _run(self, performance_data: str) -> str:
        """Allocates budget based on performance data."""
        try:
            # Convert string input to dictionary if needed
            if isinstance(performance_data, str):
                # This is a simplified example - in a real implementation, you'd parse the JSON properly
                import json
                performance_data = json.loads(performance_data)
            
            sorted_platforms = sorted(performance_data.items(), key=lambda x: x[1], reverse=True)
            allocation = {platform: 1000 + i*500 for i, (platform, _) in enumerate(sorted_platforms)}
            return str(allocation)
        except Exception as e:
            return f"Error allocating budget: {str(e)}"


class PostSchedulerTool(Tool):
    """Tool to schedule social media posts."""
    
    name: str = "Post Scheduler"
    description: str = (
        "Schedules social media posts for specific platforms at specified times. "
        "Takes content, platform, and schedule time as input."
    )

    def _run(self, input_data: str) -> str:
        """Schedules a post based on the input data."""
        try:
            # Parse input data
            import json
            data = json.loads(input_data)
            content = data.get("content", "")
            platform = data.get("platform", "")
            schedule_time = data.get("schedule_time", "")
            
            return f"Scheduled {platform} post with content '{content}' at {schedule_time}"
        except Exception as e:
            return f"Error scheduling post: {str(e)}"


class SocialCommentMonitorTool(Tool):
    """Tool to monitor and categorize social media comments."""
    
    name: str = "Social Comment Monitor"
    description: str = (
        "Monitors and categorizes social media comments, providing appropriate responses. "
        "Takes a list of comments as input and returns categorized responses."
    )

    def _run(self, comments_json: str) -> str:
        """Monitors and categorizes social media comments."""
        try:
            # Parse comments from JSON string
            import json
            comments = json.loads(comments_json)
            
            standard_responses = {
                "price": "For pricing info, visit our website or DM us!",
                "support": "Our support team is here to help. Please DM us your concern.",
            }
            grouped = {}
            unknown = []
            for comment in comments:
                if "price" in comment.lower():
                    grouped.setdefault("pricing", []).append(comment)
                elif "help" in comment.lower() or "support" in comment.lower():
                    grouped.setdefault("support", []).append(comment)
                else:
                    unknown.append(comment)
            
            result = {
                "responded": grouped,
                "escalated": unknown,
            }
            
            return json.dumps(result)
        except Exception as e:
            return f"Error monitoring comments: {str(e)}" 