from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
        										    

# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        #TODO: Create your Mininet Topology here!

        '''
        h1:0--->1:s1:0--->1:s2:0--->1:s3:0--->1:h2
                             |
                             :2--->0:s4:1--->0:h3
        '''
        
        #Link Configs
        hostConfig = {'cpu': cpu}
        wifiConfig = {'bw': 10, 'delay': 6, 'loss': 3, 'max_queue_size': max_queue_size}
        ethConfig = {'bw': 25 , 'delay': 2, 'loss': 0, 'max_queue_size': max_queue_size}
        cellConfig = {'bw': 3, 'delay': 10, 'loss': 8, 'max_queue_size': max_queue_size}

        #Switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        #Hosts
        h1 = self.addHost('h1',**hostConfig)
        h2 = self.addHost('h2',**hostConfig)
        h3 = self.addHost('h3',**hostConfig)

        #wire everything up
        self.addLink(h1, s1, port1=0, port2=1, **ethConfig)
        self.addLink(s1, s2, port1=0, port2=1, **ethConfig)
        self.addLink(s2, s3, port1=0, port2=1, **ethConfig)
        self.addLink(s3, h2, port1=0, port2=1, **wifiConfig)
        self.addLink(s4, s2, port1=0, port2=2, **ethConfig)
        self.addLink(h3, s4, port1=0, port2=1, **cellConfig)