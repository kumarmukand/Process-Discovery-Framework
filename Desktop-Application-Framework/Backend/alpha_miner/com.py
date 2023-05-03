import docker





if __name__ == "__main__":

    client = docker.from_env()
    volumes= ['/Users/kumarmukand/Music/process-mining-lab/Desktop-Application-Framework/app-data/alpha_miner']
    volume_bindings = {
                        '/Users/kumarmukand/Music/process-mining-lab/Desktop-Application-Framework/app-data/alpha_miner': {
                            'bind': '/alpha_miner',
                            'mode': 'rw',
                        },
    }

    host_config = client.api.create_host_config(
                        binds=volume_bindings
    )

    container = client.api.create_container(
                        image='am',
                        name="raghib_alpha_miner",
                        volumes=volumes,
                        host_config=host_config,
                        command='running-example.xes'
    ) 
    response = client.api.start(container=container.get('Id'))