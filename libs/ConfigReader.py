def get_app_conf(env):
        conf = configparser.ConfigParser()
        conf.read("configs/application.conf")
        app_conf = {}
        for(key,val) in conf.items(env):
                app_conf[key] = val
                return app_conf


def get_app_conf(env):
        conf = configparser.ConfigParser()
        conf.read("configs/pyspark.conf")
        app_conf = {}
        for(key,val) in conf.items(env):
                app_conf[key] = val
                return app_conf
