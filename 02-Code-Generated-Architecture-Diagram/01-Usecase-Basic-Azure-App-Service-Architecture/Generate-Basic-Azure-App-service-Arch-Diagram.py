############################################################
## Architecture Diagram: Basic Azure App Service:-

## Components include:-
# 1. User
# 2. Azure Entra ID
# 3. Azure Monitor
# 4. Azure Application Insights
# 5. Azure User Assigned Managed Identity
# 6. Azure Key Vault 
# 7. Azure App Services
# 8. Azure SQL Servers

############################################################

######################################################
# Import Diagram, Cluster and Edge.
# Import the Provider Icons for creating diagrams.
######################################################

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.general import Helpsupport, Servicehealth
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.security import KeyVaults
from diagrams.azure.identity import ManagedIdentities, ActiveDirectory
from diagrams.azure.compute import AppServices
from diagrams.azure.database import SQLServers

#########################################################
# Creating the building blocks using Nodes and Cluster.
#########################################################

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

############################################
# Connect the building blocks using Edges.
############################################

    usr >> Edge(color="darkorange") >> components_webapp
    
    components_webapp >> Edge(color="darkgreen") >> components_db