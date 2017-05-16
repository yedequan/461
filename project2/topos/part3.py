#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class part3_topo(Topo):
  def build(self):
    #note the default route addition
    #h10 = self.addHost('h10',mac='00:00:00:00:00:01',ip='10.0.1.10/24',defaultRoute='h10-eth0')
    h10 = self.addHost('h10',ip='10.0.1.10/24',defaultRoute='h10-eth1')	
    h20 = self.addHost('h20',ip='10.0.2.20/24',defaultRoute='h20-eth1')
    h30 = self.addHost('h30',ip='10.0.3.30/24',defaultRoute='h30-eth1')
    hnotrust1 = self.addHost('hnotrust1',ip='172.16.10.100/24',defaultRoute='hnotrust1-eth1')
    serv1 = self.addHost('serv1',ip='10.0.4.10/24',defaultRoute='serv1-eth1')
    s1 = self.addSwitch('s1')   
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    cores21 = self.addSwitch('cores21')
    dcs31 = self.addSwitch('dcs31')
   # self.addLink(h10, s1)
    self.addLink(h10, s1,port1=1,port2=2)
    self.addLink(h20, s2,port1=1,port2=2)
    self.addLink(h30, s3,port1=1,port2=2)
    self.addLink(hnotrust1, cores21,port1=1,port2=4)
    self.addLink(s1, cores21,port1=4,port2=1)
    self.addLink(s2, cores21,port1=4,port2=2)
    self.addLink(s3, cores21,port1=4,port2=3)
    self.addLink(dcs31, cores21,port1=1,port2=5)
    self.addLink(dcs31, serv1,port1=2,port2=1)

topos = {'part3' : part3_topo}

def configure():
  topo = part3_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()
  
  CLI(net)

  net.stop()


if __name__ == '__main__':
  configure()
