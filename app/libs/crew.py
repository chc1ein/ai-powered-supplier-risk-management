import os
from datetime import datetime

from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, callback
from crewai.memory import ShortTermMemory, EntityMemory, LongTermMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

from .research import SearchAndContents, FindSimilar, GetContents

load_dotenv()


@CrewBase
class SupplierRiskAssessmentCrewPOC:
    """Crew for Supplier Risk Analysis"""

    agents_config = "config/agents_poc.yaml"
    tasks_config = "config/tasks_poc.yaml"

	# Azure OpenAI
    llm = LLM(
		model=f"azure/{os.getenv('DEPLOYMENT_NAME')}",
		api_key=os.getenv("AZURE_OPENAI_API_KEY"),
		base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
		api_version=os.getenv("OPENAI_API_VERSION")
	)

    @agent
    def profiling_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["profiling_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def strategy_ops_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["strategy_ops_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @task
    def profile_supplier_task(self) -> Task:
        return Task(
            config=self.tasks_config["profile_supplier_task"],
            agent=self.profiling_agent(),
            output_file=f"supplier_risk_profile_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        )

    @task
    def search_strategy_ops_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_strategy_ops_task"],
            agent=self.strategy_ops_agent(),
            output_file=f"supplier_risk_strategy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        )

    @crew
    def crew(self) -> Crew:
        """
        Create the Supplier Risk Analysis Crew. 
        The process is sequential here, but you can also define parallel processes 
        or custom flows if your use case demands it.
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # or Process.parallel
            verbose=True,
        )

@CrewBase
class SupplierRiskAssessmentCrew:
    """Crew for Supplier Risk Analysis"""

    agents_config = "config/agents_poc.yaml"
    tasks_config = "config/tasks_poc.yaml"

	# Azure OpenAI
    llm = LLM(
		model=f"azure/{os.getenv('DEPLOYMENT_NAME')}",
		api_key=os.getenv("AZURE_OPENAI_API_KEY"),
		base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
		api_version=os.getenv("OPENAI_API_VERSION")
	)

    ############################################################################
    #                          AGENT DEFINITIONS                               #
    ############################################################################

    @agent
    def profiling_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["profiling_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def strategy_ops_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["strategy_ops_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def financial_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def org_changes_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["org_changes_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def compliance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["compliance_agent"],
            tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analysis_agent"],
            #tools=[SearchAndContents(), FindSimilar(), GetContents()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    @agent
    def reporting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_agent"],
            # tools=[...]
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            memory=True,
        )

    ############################################################################
    #                          TASK DEFINITIONS                                #
    ############################################################################

    @task
    def profile_supplier_task(self) -> Task:
        return Task(
            config=self.tasks_config["profile_supplier_task"],
            agent=self.profiling_agent(),
            output_file="supplier_risk_profile_report.md",
        )

    @task
    def search_strategy_ops_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_strategy_ops_task"],
            agent=self.strategy_ops_agent(),
        )

    @task
    def search_financial_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_financial_task"],
            agent=self.financial_agent(),
        )

    @task
    def search_org_changes_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_org_changes_task"],
            agent=self.org_changes_agent(),
        )

    @task
    def search_compliance_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_compliance_task"],
            agent=self.compliance_agent(),
        )

    @task
    def analyze_risks_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_risks_task"],
            agent=self.analysis_agent(),
        )

    @task
    def create_markdown_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_markdown_report_task"],
            agent=self.reporting_agent(),
            output_file="supplier_risk_report.md",
        )

    ############################################################################
    #                          CREW DEFINITION                                  #
    ############################################################################

    @crew
    def crew(self) -> Crew:
        """
        Create the Supplier Risk Analysis Crew. 
        The process is sequential here, but you can also define parallel processes 
        or custom flows if your use case demands it.
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # or Process.parallel
            memory=True,
            # embedder={
            #     "provider": "openai",
            #     "config": {
            #         "api_key": os.getenv("AZURE_OPENAI_EMBED_API_KEY"),
            #         "api_base": os.getenv("AZURE_OPENAI_EMBED_MODEL_ENDPOINT"),
            #         "api_version": os.getenv("OPENAI_API_VERSION"),
            #         "model_name": os.getenv("EMBEDDING_MODEL")
            #     }
            # },
            #verbose=True,
            # Short-term memory for current context using RAG
            # short_term_memory = ShortTermMemory(
            #     storage = RAGStorage(
            #             embedder_config={
            #                 "provider": "azure",
            #                 "config": {
            #                     "api_key": os.getenv("AZURE_OPENAI_EMBED_API_KEY"),
            #                     "api_base": os.getenv("AZURE_OPENAI_EMBED_MODEL_ENDPOINT"),
            #                     "api_version": os.getenv("OPENAI_API_VERSION"),
            #                     "model_name": os.getenv('EMBEDDING_MODEL')
            #                 }
            #             },
            #             type="short_term",
            #             path=f"{os.path.join(os.path.abspath(__file__),'..')}/short_term/my_crew1/"
            #         )
            # ),
            short_term_memory = ShortTermMemory(
                storage = RAGStorage(
                        embedder_config={
                            "provider": "openai",
                            "config": {
                                "model": 'text-embedding-3-small'
                            }
                        },
                        type="short_term",
                        path=f"{os.path.join(os.path.abspath(__file__), '..')}/short_term/my_crew1/"
                    )
            ),
            # Entity memory for tracking key information about entities
            entity_memory = EntityMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "openai",
                        "config": {
                            "model": 'text-embedding-3-small'
                        }
                    },
                    type="short_term",
                    path=f"{os.path.join(os.path.abspath(__file__), '..')}/short_term/my_crew1/"
                )
            ),
            # Long-term memory for persistent storage across sessions
            long_term_memory = LongTermMemory(
                storage=LTMSQLiteStorage(
                    db_path=f"{os.path.join(os.path.abspath(__file__), '..')}/short_term/my_crew1/long_term_memory_storage.db"
                )
            ),
            # # Entity memory for tracking key information about entities
            # entity_memory = EntityMemory(
            #     storage=RAGStorage(
            #         embedder_config={
            #             "provider": "azure",
            #             "config": {
            #                 "api_key": os.getenv("AZURE_OPENAI_EMBED_API_KEY"),
            #                 "api_base": os.getenv("AZURE_OPENAI_EMBED_MODEL_ENDPOINT"),
            #                 "api_version": os.getenv("OPENAI_EMBED_API_VERSION"),
            #                 "model_name": os.getenv("EMBEDDING_MODEL")
            #             }
            #         },
            #         type="short_term",
            #         path=f"{os.path.join(os.path.abspath(__file__), '..')}/short_term/my_crew1/"
            #     )
            # ),
            verbose=True,
        )