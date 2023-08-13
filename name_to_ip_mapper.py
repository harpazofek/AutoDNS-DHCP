# This module will contain the NameToIPMapper class.
import logging
import json
from groupnameresolver import GroupNameResolver

class DNSGroup:
    def __init__(self, group_name):
        self.group_name = group_name
        self.dns_records = {}

class NameToIPMapper:
    def __init__(self):
        self.groups = {}
        self.last_found_ip = None
        self.group_name_resolver = GroupNameResolver()
    
    def add_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = DNSGroup(group_name)
    
    def add_mapping(self, name, ip):
        group_name = self.group_name_resolver.determine_group_name(name)
        
        if group_name not in self.groups:
            self.add_group(group_name)
        
        group = self.groups[group_name]
        group.dns_records[name] = ip
    
    def get_ip_by_name(self, group_name, name):
        if group_name in self.groups:
            group = self.groups[group_name]
            return group.dns_records.get(name)
        else:
            return None
    
    def search_and_write_to_file(self, name):
        group_name = self.group_name_resolver.determine_group_name(name)
        
        if group_name in self.groups:
            group = self.groups[group_name]
            ip = self.get_ip_by_name(group_name, name)
            if ip:
                self.last_found_ip = ip
                logging.info(f"Found IP address {ip} for {name}")
                with open(f"{group_name}_output_file.txt", "a") as file:
                    file.write(f"{name}: {ip}\n")
            else:
                logging.info(f"No IP address found for {name}")
        else:
            logging.warning(f"Group '{group_name}' not found. Skipping search and write.")

    def store_to_json(self, name, ip, parameters):
        group_name = self.group_name_resolver.determine_group_name(name)
        
        if group_name in self.groups:
            group = self.groups[group_name]
            
            record = {"name": name, "ip": ip, "parameters": parameters}
            
            if name not in group.dns_records:
                group.dns_records[name] = []
            
            group.dns_records[name].append(record)
            
            file_name = f"{group_name}_output_file.json"
            
            if group_name == "YetAnotherGroup":  # XYZ prefix
                template = {
                    "group": group_name,
                    "name": name,
                    "ip": ip,
                    "parameter1": parameters.get("parameter1", ""),
                    "parameter2": parameters.get("parameter2", "")
                }
                
                with open(f"{group_name}_template.json", "w") as template_file:
                    json.dump(template, template_file, indent=4)
                
                file_name = f"{group_name}_output_file_{name}.json"
            
            with open(file_name, "w") as file:
                json.dump(group.dns_records, file, indent=4)
                