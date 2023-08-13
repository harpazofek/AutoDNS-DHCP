import schedule
import time
import logging
import dnslib.server
from logging.handlers import RotatingFileHandler
from mylogger import setup_logging
from nametoipmapper import NameToIPMapper
from groupnameresolver import GroupNameResolver

# Set up logging
setup_logging()

def main():
    name_mapper = NameToIPMapper()
    
    # Add mappings
    name_mapper.add_mapping("example1", "192.168.1.1")
    name_mapper.add_mapping("example2", "192.168.1.2")
    name_mapper.add_mapping("example3", "192.168.1.3")
    
    # Specify the location where you want to search the IP (e.g., "XYZ" for YetAnotherGroup)
    search_location = "XYZ"
    
    # Specify the name for which you want to search the IP
    name_to_search = "example1"
    
    parameters = {
        "parameter1": "value1",
        "parameter2": "value2"
    }
    
    schedule.every(1).hour.do(name_mapper.store_to_json, name_to_search, "192.168.1.1", parameters)
    
    dns_resolver = dnslib.server.DNSServer(
        resolver=dnslib.server.BaseResolver(address_map={}),
        address="0.0.0.0",
        port=53
    )
    
    dns_resolver.start_thread()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    logging.info("Program started")
    main()
