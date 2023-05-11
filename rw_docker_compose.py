import yaml

def write_docker_compose_file(file_path, extra_hosts_file):
    with open(file_path, 'r') as file:
        compose_data = yaml.safe_load(file)
    if 'services' in compose_data and 'web' in compose_data['services']:
        web_service = compose_data['services']['web']

        with open(extra_hosts_file, 'r') as extra_hosts_file:
            extra_hosts = extra_hosts_file.read().splitlines()
        
        updated_extra_hosts = [host for host in extra_hosts]
        web_service['extra_hosts'] = updated_extra_hosts

    with open(file_path, 'w') as file:
        yaml.safe_dump(compose_data, file, indent=2)

compose_file_path = 'docker-compose.yml'
extra_hosts_file_path = 'extra_hosts.txt'
write_docker_compose_file(compose_file_path, extra_hosts_file_path)

print(" `extra_hosts` Docker Compose file updated successfully.")
