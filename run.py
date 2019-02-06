import os
from app import create_app

#config_name = os.getenv('CONFIG_TYPE')
config_name = os.getenv('CONFIG_TYPE')
app = create_app('development')

if __name__ == '__main__':
	app.run()
