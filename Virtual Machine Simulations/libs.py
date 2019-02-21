import pickle


class Workload:
    def __init__(self, ip, credentials, storage):
        self.__UP = ip
        self.__Storage = None
        self.__Credentials = None

        self.credentials = credentials
        self.storage = storage

    @property
    def ip(self):
        return self.__UP

    @property
    def credentials(self):
        return self.__Credentials
    @credentials.setter
    def credentials(self, value):
        if isinstance(value, Credentials):
            self.__Credentials = value
        else:
            raise ValueError('credentials must be an instance of Credentials')

    @property
    def storage(self):
        return self.__Storage
    @storage.setter
    def storage(self, value):
        for sub in value:
            if isinstance(sub, MountPoint):
                self.__Storage = value
            else:
                raise ValueError('storage must be an instance of MountPoint')



class Credentials:
    def __init__(self, username, password, domain):
        self.username = username
        self.password = password
        self.domain = domain



class MountPoint:
    def __init__(self, mountname, totalsize):
        self.mountname = mountname
        self.totalsize = totalsize



class Source:
    ip_list = []
    def __init__(self, ip, username, password):
        if None in [ip, username, password]:
            raise ValueError('ip, username or password cant be None')

        if ip in Source.ip_list:
            raise ValueError('IP cant be used twice')

        self.__ip = ip
        self.username = username
        self.password = password
        Source.ip_list.append(ip)

    @property
    def ip(self):
        return self.__ip


class MigrationTarget:
    def __init__(self, cloudType, credentials, targetVm):
        self.__credentials = None
        self.__cloudType = None
        self.__targetVm = None

        self.credentials = credentials
        self.cloudType = cloudType
        self.targetVm = targetVm


    @property
    def cloudType(self):
        return self.__cloudType
    @cloudType.setter
    def cloudType(self, value):
        if value in ['aws', 'azure', 'vsphere', 'vcloud']:
            self.__cloudType = value
        else:
            raise ValueError('Cloud type must be only aws, azure, vsphere or vcloud')

    @property
    def credentials(self):
        return self.__cloudType
    @credentials.setter
    def credentials(self, value):
        if isinstance(value, Credentials):
            self.__credentials = value
        else:
            raise ValueError('credentials must be an instance of Credentials')

    @property
    def targetVm(self):
        return self.__targetVm
    @targetVm.setter
    def targetVm(self, value):
        if isinstance(value, Workload):
            self.__targetVm = value
        else:
            raise ValueError('targetVm must be an instance of Workload')



class Migration:
    def __init__(self, mountPoints, source, migrationTarget):
        self.__MountPoints = []

        self.__Source = None
        self.__MigrationTarget = None
        self.__MigrationState = None

        self.source = source
        self.mountPoints = mountPoints
        self.migrationTarget = migrationTarget

        self.migrationState = 'not started'


    @property
    def mountPoints(self):
        return self.__Storage
    @mountPoints.setter
    def mountPoints(self, value):
        for sub in value:
            if isinstance(sub, MountPoint):
                self.__Storage = value
            else:
                raise ValueError('mountPoints must be an instance of MountPoint')

    @property
    def source(self):
        return self.__Source
    @source.setter
    def source(self, value):
        if isinstance(value, Workload):
            self.__Source = value
        else:
            raise ValueError('source must be an instance of Workload')

    @property
    def migrationTarget(self):
        return self.__MigrationTarget
    @migrationTarget.setter
    def migrationTarget(self, value):
        if isinstance(value, MigrationTarget):
            self.__MigrationTarget = value
        else:
            raise ValueError('migrationTarget must be an instance of MigrationTarget')

    @property
    def migrationState(self):
        return self.__MigrationState
    @migrationState.setter
    def migrationState(self, value):
        if value in ['not started', 'running', 'error', 'success']:
            self.__MigrationState = value
        else:
            raise ValueError('Cloud type must be  not started, running, error or success')


    def run(self,):
        self.migrationState = 'running'

        for mount_point in self.mountPoints:
            if 'C:\\' in mount_point.mountname:
                break
        else:
            self.migrationState = 'error'

        self.migrationTarget.targetVm = self.source
        self.migrationTarget.targetVm.storage = self.mountPoints

        self.migrationState = 'success'



def save_obj(obj, save_path):
    with open(save_path, 'wb') as f:
        pickle.dump(obj, f)


def load_obj(save_path):
    with open(save_path, 'rb') as f:
        return pickle.load(f)


mount1 = MountPoint('C:\\', 50)
mount2 = MountPoint('E:\\', 50)

cred1 = Credentials('username', 'password', 'domain')
cred2 = Credentials('username', 'password', 'domain')

sourse1 = Source('ip1', 'username', 'password')
sourse1 = Source('ip2', 'username', 'password')

wrkld1 = Workload('ip1', cred1, [mount1, mount2])
wrkld2 = Workload('ip2', cred2, [mount1])

mig = Migration([mount1], wrkld2, MigrationTarget('aws', cred1, wrkld1))

mig.run()

print(mig.migrationState)

save_obj(mig, 'a.txt')
x = load_obj('a.txt')

print(x.migrationState)
