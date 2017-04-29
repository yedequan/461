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
    pass

topos = {'part3' : part3_topo}

def configure():
  topo = part3_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()
  
  CLI(net)

  net.stop()


if __name__ == '__main__':
  configure()
