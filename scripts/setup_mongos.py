from os import system
from yaml import load

with open('config.yaml', 'r') as config:
    config_yaml = load(config.read())

rs_name = config_yaml.get('repl_name', 'demo_rs')
shard_1 = config_yaml.get('shard_1', 'tic')
shard_2 = config_yaml.get('shard_2', 'tac')
shard_3 = config_yaml.get('shard_3', 'toe')
shard_port = config_yaml.get('start_repl_port', 30000)
non_shard_port = config_yaml.get('non_shard_port', 27018)

system('mkdir -p data')
system('mkdir -p non_shard_data')
system(f'mlaunch init --replicaset --name {rs_name} --sharded {shard_1} {shard_2} {shard_3} --port {shard_port}')
system(f'mlaunch init --single --dir non_shard_data --port {non_shard_port}')
