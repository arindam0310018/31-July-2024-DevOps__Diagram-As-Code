############################################################
## Architecture Diagram: Gaming using Azure Cosmos DB:-

## Components include:-
# 1. User
# 2. Azure Traffic Manager
# 3. Azure Content Delivery Network
# 4. Azure Storage
# 5. Azure API Management 
# 6. Azure Cosmos DB
# 7. Azure Databricks
# 8. Azure Functions
# 9. Azure Notification Hubs

############################################################

######################################################
# Import Diagram, Cluster and Edge.
# Import the Provider Icons for creating diagrams.
######################################################

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.general import Helpsupport
from diagrams.azure.network import TrafficManagerProfiles, CDNProfiles
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.integration import APIManagement
from diagrams.azure.database import CosmosDb
from diagrams.azure.analytics import Databricks
from diagrams.azure.compute import FunctionApps
from diagrams.azure.mobile import NotificationHubs

#########################################################
# Creating the building blocks using Nodes and Cluster.
#########################################################

# with Diagram("GAMING ARCHITECTURE", show=False, direction="TB"):
with Diagram("GAMING ARCHITECTURE", show=False):
    usr = Helpsupport("User")

    # atm = TrafficManagerProfiles("Azure Traffic Manager")

    apim = APIManagement("Azure API Apps")

    cosmos = CosmosDb("Azure Cosmos DB")

    dbks = Databricks("Azure Databricks")

    # cdn = CDNProfiles ("Azure CDN")

    # storage = StorageAccounts("Azure Storage (Media Files)")

    functions = FunctionApps("Azure Functions")

    notifyhub = NotificationHubs("Azure Notification Hubs")

    with Cluster(""):
         atm = TrafficManagerProfiles("Traffic Manager")

    with Cluster(""):
         cdn = CDNProfiles ("Azure CDN")

    with Cluster(""):
         storage = StorageAccounts("Azure Storage")

############################################
# Connect the building blocks using Edges.
############################################

    usr >> Edge(color="darkgreen") >> atm
    cdn >> Edge(color="darkblue") >> atm
    storage >> Edge(color="darkpurple") >> cdn
    atm >> Edge(color="darkorange") >> apim
    apim >> Edge(color="darkred") >> cosmos
    cosmos >> Edge(color="darkred") >> apim
    cosmos >> Edge(color="darkblue") >> dbks
    cosmos >> Edge(color="darkblue") >> functions
    functions >> Edge(color="darkbrown") >> notifyhub 