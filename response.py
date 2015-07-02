__author__ = 'driees'


class Info(object):
   def __init__(self,ID,Containers,Images,Driver,DriverStatus,MemoryLimit,SwapLimit,CpuCfsPeriod,CpuCfsQuota,IPv4Forwarding,Debug,NFd,OomKillDisable,NGoroutines,SystemTime,ExecutionDriver,LoggingDriver,NEventsListener,KernelVersion,OperatingSystem,IndexServerAddress,RegistryConfig,InitSha1,InitPath,NCPU,MemTotal,DockerRootDir,HttpProxy,HttpsProxy,NoProxy,Name,Labels,ExperimentalBuild):
           self.ID=ID
           self.Containers=Containers
           self.Images=Images
           self.Driver=Driver=Driver=Driver
           self.DriverStatus=DriverStatus
           self.MemoryLimit=MemoryLimit
           self.SwapLimit=SwapLimit
           self.CpuCfsPeriod=CpuCfsPeriod
           self.CpuCfsQuota=CpuCfsQuota
           self.IPv4Forwarding=IPv4Forwarding
           self.Debug=Debug
           self.NFd=NFd
           self.OomKillDisable=OomKillDisable
           self.NGoroutines=NGoroutines
           self.SystemTime=SystemTime
           self.ExecutionDriver=ExecutionDriver
           self.LoggingDriver=LoggingDriver
           self.NEventsListener=NEventsListener
           self.KernelVersion=KernelVersion
           self.OperatingSystem=OperatingSystem
           self.IndexServerAddress=IndexServerAddress
           self.RegistryConfig=RegistryConfig
           self.InitSha1=InitSha1
           self.InitPath=InitPath
           self.NCPU=NCPU
           self.MemTotal=MemTotal
           self.DockerRootDir=DockerRootDir
           self.HttpProxy=HttpProxy
           self.HttpsProxy=HttpsProxy
           self.NoProxy=NoProxy
           self.Name=Name
           self.Labels=Labels
           self.ExperimentalBuild=ExperimentalBuild


class Container(object):
    def __init__(self,Id,Names,Image,Command,Created,Ports,Labels,Status):
        self.Id=Id 
        self.Names=Names 
        self.Image=Image 
        self.Command=Command 
        self.Created=Created 
        self.Ports=Ports 
        self.Labels=Labels 
        self.Status=Status

class Version(object):
    def __init__(self,Version,ApiVersion,GitCommit,GoVersion,Os,Arch,KernelVersion):
        self.Version=Version 
        self.ApiVersion=ApiVersion 
        self.GitCommit=GitCommit 
        self.GoVersion=GoVersion 
        self.Os=Os 
        self.Arch=Arch 
        self.KernelVersion=KernelVersion