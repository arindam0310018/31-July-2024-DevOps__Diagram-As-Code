# Import the Icons for creating diagrams:-

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.general import Subscriptions, Resourcegroups, Azurehome, Helpsupport, Servicehealth
from diagrams.azure.network import VirtualNetworks, Subnets, NetworkSecurityGroupsClassic, ExpressrouteCircuits
from diagrams.azure.integration import APIManagement
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.storage import DataLakeStorage
from diagrams.azure.security import KeyVaults
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.identity import ManagedIdentities, ActiveDirectory
from diagrams.azure.compute import OsImages, AppServices
from diagrams.azure.database import SQLServers

# Create the building blocks:-

with Diagram("Basic Azure App Service Architecture", show=False, direction="TB"):
    usr = Helpsupport("User")

    with Cluster("Compute"):
        components_webapp = [AppServices("AppServices"), KeyVaults("KV"), ManagedIdentities("UMID")]

    with Cluster("Data"):
        components_db = SQLServers("Azure SQL Database")

    with Cluster("Identity"):
        components_identity = [ActiveDirectory("Microsoft Entra ID")]

    with Cluster("Monitoring"):
        components_monitor = [ApplicationInsights("App Insights"), Servicehealth("Azure Monitor")]

# Connect the building blocks:-

    usr >> Edge(color="darkorange") >> components_webapp
    
    components_webapp >> Edge(color="darkgreen") >> components_db