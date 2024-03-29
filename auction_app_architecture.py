from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.integration import SQS
from diagrams.aws.security import IAM
from diagrams.aws.storage import S3
from diagrams.onprem.client import User

with Diagram("Online Auction App Architecture", show=False):
    user = User("User")

    with Cluster("Auction Platform"):
        with Cluster("Frontend Services"):
            frontend = ELB("Load Balancer")

        with Cluster("Backend Services"):
            backend = EC2("Application Server")
            auth = IAM("Authentication Service")
            queue = SQS("Job Queue")

        with Cluster("Data Storage"):
            database = RDS("Database")
            files = S3("File Storage")

    user >> frontend >> backend >> database
    user >> frontend >> backend >> auth
    backend >> queue
    backend >> files
