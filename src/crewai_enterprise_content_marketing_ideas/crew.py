from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os

# Import custom tools
from crewai_enterprise_content_marketing_ideas.tools.custom_tool import MyCustomTool
from crewai_enterprise_content_marketing_ideas.tools.advertisement_poster_tool import AdvertisementPosterTool
from crewai_enterprise_content_marketing_ideas.tools.web_scraper import WebScraperTool
from crewai_enterprise_content_marketing_ideas.tools.content_gen_tool import ContentGeneratorTool
from crewai_enterprise_content_marketing_ideas.tools.ad_api import BudgetAllocatorTool, PostSchedulerTool, SocialCommentMonitorTool
from crewai_enterprise_content_marketing_ideas.tools.analytics_api import AdsAnalyticsTool

# Check our tools documentations for more information on how to use them
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Set the Gemini API key
GEMINI_API_KEY = ""
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

my_llm = LLM(
              model='gemini/gemini-2.0-flash',
              api_key=GEMINI_API_KEY
            )

@CrewBase
class CrewaiEnterpriseContentMarketingCrew:
    """CrewaiEnterpriseContentMarketing crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool(), WebScraperTool()],
            llm = my_llm,
            function_calling_llm	= my_llm,
            verbose=True,
        )

    @agent
    def content_generator(self) -> Agent:
        return Agent(config=self.agents_config["content_generator"],
            tools=[ContentGeneratorTool()],
            llm = my_llm,
            function_calling_llm	= my_llm,
             verbose=True)
    
    @agent
    def marketing_designer(self) -> Agent:
        return Agent(
            config=self.agents_config["marketing_designer"],
            tools=[AdvertisementPosterTool()],
            llm = my_llm,
            function_calling_llm = my_llm,
            verbose=True,
        )
    
    @agent
    def marketing_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["marketing_analyst"],
            tools=[AdsAnalyticsTool(), BudgetAllocatorTool()],
            llm = my_llm,
            function_calling_llm = my_llm,
            verbose=True,
        )
    
    @agent
    def social_media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["social_media_manager"],
            tools=[PostSchedulerTool(), SocialCommentMonitorTool()],
            llm = my_llm,
            function_calling_llm = my_llm,
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def content_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["content_generation_task"], output_file="report.md"
        )
    
    @task
    def create_advertisement_poster_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_advertisement_poster_task"],
            output_file="advertisement_poster.png"
        )
    
    @task
    def analyze_marketing_performance_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_marketing_performance_task"],
            output_file="marketing_analysis.md"
        )
    
    @task
    def manage_social_media_task(self) -> Task:
        return Task(
            config=self.tasks_config["manage_social_media_task"],
            output_file="social_media_report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiEnterpriseContentMarketing crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
