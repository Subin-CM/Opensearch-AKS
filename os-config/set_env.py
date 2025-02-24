import os

class SetEnvironment():
    def __init__(self, config_filepath, env) -> None:
        self.config_filepath = config_filepath
        self.env = env
        self.update_variable()

    def update_variable(self):      
        with open(self.config_filepath, 'r') as file:
            content = file.read()
        env = self.env
        content = content.replace('USERNAME_BASE64ENCODED', " "+os.getenv("USERNAME_BASE64ENCODED_" + env, ''))
        content = content.replace('PASSWORD_BASE64ENCODED', ""+os.getenv("PASSWORD_BASE64ENCODED", ''))
        content = content.replace('HASHED_ADMIN_PASSWORD', ""+os.getenv("HASHED_ADMIN_PASSWORD", ''))
        content = content.replace('METADATA_URL', ""+os.getenv("METADATA_URL_" + env, ''))
        content = content.replace('ENTITY_ID_URL', ""+os.getenv("ENTITY_ID_URL_" + env, ''))
        content = content.replace('ENTITY_ID', ""+os.getenv("ENTITY_ID_" + env, ''))
        content = content.replace('OPENSEARCH_DASHBOARD_URL', ""+os.getenv("OPENSEARCH_DASHBOARD_URL_" + env, ''))
        content = content.replace('EXCHANGE_KEY', ""+os.getenv("EXCHANGE_KEY_" + env, ''))
        content = content.replace('STORAGE_SECRET', ""+os.getenv("STORAGE_SECRET_" + env, ''))
        content = content.replace('MASTER_STORAGE_SIZE', ""+os.getenv("MASTER_STORAGE_SIZE_" + env, ''))
        content = content.replace('REPLICA_MASTER', ""+os.getenv("REPLICA_MASTER_" + env, ''))
        content = content.replace('DATA_STORAGE_SIZE', ""+os.getenv("DATA_STORAGE_SIZE_" + env, ''))
        content = content.replace('REPLICA_DATA', ""+os.getenv("REPLICA_DATA_" + env, ''))
        content = content.replace('CLIENT_STORAGE_SIZE', ""+os.getenv("CLIENT_STORAGE_SIZE_" + env, ''))
        content = content.replace('REPLICA_CLIENT', ""+os.getenv("REPLICA_CLIENT_" + env, ''))
        
        with open(self.config_filepath, 'w') as file:
            file.write(content)
    
if __name__ == "__main__":
    env = os.getenv("ENV", '')
    KUBECONFIG_FILEPATH = os.getenv("KUBECONFIG_FILEPATH", '')
    print(f"updating file {KUBECONFIG_FILEPATH}")
    SetEnvironment(KUBECONFIG_FILEPATH, env)


