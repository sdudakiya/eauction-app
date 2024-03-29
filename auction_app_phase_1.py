from diagrams import Diagram, Cluster
from diagrams.generic.blank import Blank
from diagrams.custom import Custom

with Diagram("Phase 1: Forward Auctions for Sellers", show=False, direction="TB"):
    farmer = Custom("Farmer", "./icons/farmer.png")  # Path to a farmer icon
    auction_manager = Custom("Auction Manager", "./icons/auction_manager.png")  # Path to an auction manager icon
    buyer = Custom("Buyer", "./icons/buyer.png")  # Path to a buyer icon
    warehouse = Custom("Warehouse", "./icons/warehouse.png")  # Path to a warehouse icon
    lab = Custom("Lab Testing", "./icons/lab.png")  # Path to a lab icon
    auction_platform = Custom("Auction Platform", "./icons/auction_platform.png")  # Path to an auction platform icon
    sample = Custom("Sample Submission", "./icons/sample.png")  # Path to a sample icon
    consent = Custom("Consent Form", "./icons/consent.png")  # Path to a consent form icon
    lock_goods = Custom("Lock & Tag Goods", "./icons/lock_goods.png")  # Path to a lock & tag icon
    upload_documents = Custom("Upload Documents", "./icons/upload_documents.png")  # Path to an upload documents icon
    auction = Custom("Auction", "./icons/auction.png")  # Path to an auction icon
    bid = Custom("Place Bid", "./icons/bid.png")  # Path to a bid icon
    highest_bid = Custom("Highest Bid", "./icons/highest_bid.png")  # Path to a highest bid icon

    farmer >> consent >> sample >> lab
    farmer >> warehouse >> lock_goods >> upload_documents
    upload_documents >> auction_platform
    auction_platform >> auction >> bid >> highest_bid
    highest_bid >> buyer
    lab >> auction_platform

# Note: You'll need to replace "./icons/xyz.png" with the actual paths to your icon images.
