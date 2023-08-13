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
    
    name_to_search = "example1"  # Replace with the name you want to search for
    
    schedule.every(1).hour.do(name_mapper.search_and_write_to_file, name_to_search)
    
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
