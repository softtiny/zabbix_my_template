from tools import  api,asyncio,Base

hostid = Base['hostid']

vmaps=[
                    {
                        "name": "ifOperStatus",
						"hostid": hostid,
                        "mappings": [
                            {
                                "value": "0",
                                "newvalue": "unknown"
                            },
                            {
                                "value": "1",
                                "newvalue": "notpresent"
                            },
                            {
                                "value": "2",
                                "newvalue": "down"
                            },
                            {
                                "value": "3",
                                "newvalue": "lowerlayerdown"
                            },
                            {
                                "value": "4",
                                "newvalue": "testing"
                            },
                            {
                                "value": "5",
                                "newvalue": "dormant"
                            },
                            {
                                "value": "6",
                                "newvalue": "up"
                            }
                        ]
                    },
                    {
                        "name": "Linux::Interface protocol types",
						"hostid": hostid,
                        "mappings": [
                            {
                                "value": "0",
                                "newvalue": "from KA9Q: NET/ROM pseudo"
                            },
                            {
                                "value": "1",
                                "newvalue": "Ethernet"
                            },
                            {
                                "value": "2",
                                "newvalue": "Experimental Ethernet"
                            },
                            {
                                "value": "3",
                                "newvalue": "AX.25 Level 2"
                            },
                            {
                                "value": "4",
                                "newvalue": "PROnet token ring"
                            },
                            {
                                "value": "5",
                                "newvalue": "Chaosnet"
                            },
                            {
                                "value": "6",
                                "newvalue": "IEEE 802.2 Ethernet/TR/TB"
                            },
                            {
                                "value": "7",
                                "newvalue": "ARCnet"
                            },
                            {
                                "value": "8",
                                "newvalue": "APPLEtalk"
                            },
                            {
                                "value": "15",
                                "newvalue": "Frame Relay DLCI"
                            },
                            {
                                "value": "19",
                                "newvalue": "ATM"
                            },
                            {
                                "value": "23",
                                "newvalue": "Metricom STRIP (new IANA id)"
                            },
                            {
                                "value": "24",
                                "newvalue": "IEEE 1394 IPv4 - RFC 2734"
                            },
                            {
                                "value": "27",
                                "newvalue": "EUI-64"
                            },
                            {
                                "value": "32",
                                "newvalue": "InfiniBand"
                            },
                            {
                                "value": "256",
                                "newvalue": "ARPHRD_SLIP"
                            },
                            {
                                "value": "257",
                                "newvalue": "ARPHRD_CSLIP"
                            },
                            {
                                "value": "258",
                                "newvalue": "ARPHRD_SLIP6"
                            },
                            {
                                "value": "259",
                                "newvalue": "ARPHRD_CSLIP6"
                            },
                            {
                                "value": "260",
                                "newvalue": "Notional KISS type"
                            },
                            {
                                "value": "264",
                                "newvalue": "ARPHRD_ADAPT"
                            },
                            {
                                "value": "270",
                                "newvalue": "ARPHRD_ROSE"
                            },
                            {
                                "value": "271",
                                "newvalue": "CCITT X.25"
                            },
                            {
                                "value": "272",
                                "newvalue": "Boards with X.25 in firmware"
                            },
                            {
                                "value": "280",
                                "newvalue": "Controller Area Network"
                            },
                            {
                                "value": "512",
                                "newvalue": "ARPHRD_PPP"
                            },
                            {
                                "value": "513",
                                "newvalue": "Cisco HDLC"
                            },
                            {
                                "value": "516",
                                "newvalue": "LAPB"
                            },
                            {
                                "value": "517",
                                "newvalue": "Digital's DDCMP protocol"
                            },
                            {
                                "value": "518",
                                "newvalue": "Raw HDLC"
                            },
                            {
                                "value": "519",
                                "newvalue": "Raw IP"
                            },
                            {
                                "value": "768",
                                "newvalue": "IPIP tunnel"
                            },
                            {
                                "value": "769",
                                "newvalue": "IP6IP6 tunnel"
                            },
                            {
                                "value": "770",
                                "newvalue": "Frame Relay Access Device"
                            },
                            {
                                "value": "771",
                                "newvalue": "SKIP vif"
                            },
                            {
                                "value": "772",
                                "newvalue": "Loopback device"
                            },
                            {
                                "value": "773",
                                "newvalue": "Localtalk device"
                            },
                            {
                                "value": "774",
                                "newvalue": "Fiber Distributed Data Interface"
                            },
                            {
                                "value": "775",
                                "newvalue": "AP1000 BIF"
                            },
                            {
                                "value": "776",
                                "newvalue": "sit0 device - IPv6-in-IPv4"
                            },
                            {
                                "value": "777",
                                "newvalue": "IP over DDP tunneller"
                            },
                            {
                                "value": "778",
                                "newvalue": "GRE over IP"
                            },
                            {
                                "value": "779",
                                "newvalue": "PIMSM register interface"
                            },
                            {
                                "value": "780",
                                "newvalue": "High Performance Parallel Interface"
                            },
                            {
                                "value": "781",
                                "newvalue": "Nexus 64Mbps Ash"
                            },
                            {
                                "value": "782",
                                "newvalue": "Acorn Econet"
                            },
                            {
                                "value": "783",
                                "newvalue": "Linux-IrDA"
                            },
                            {
                                "value": "784",
                                "newvalue": "Point to point fibrechannel"
                            },
                            {
                                "value": "785",
                                "newvalue": "Fibrechannel arbitrated loop"
                            },
                            {
                                "value": "786",
                                "newvalue": "Fibrechannel public loop"
                            },
                            {
                                "value": "787",
                                "newvalue": "Fibrechannel fabric"
                            },
                            {
                                "value": "800",
                                "newvalue": "Magic type ident for TR"
                            },
                            {
                                "value": "801",
                                "newvalue": "IEEE 802.11"
                            },
                            {
                                "value": "802",
                                "newvalue": "IEEE 802.11 + Prism2 header"
                            },
                            {
                                "value": "803",
                                "newvalue": "IEEE 802.11 + radiotap header"
                            },
                            {
                                "value": "804",
                                "newvalue": "ARPHRD_IEEE802154"
                            },
                            {
                                "value": "805",
                                "newvalue": "IEEE 802.15.4 network monitor"
                            },
                            {
                                "value": "820",
                                "newvalue": "PhoNet media type"
                            },
                            {
                                "value": "821",
                                "newvalue": "PhoNet pipe header"
                            },
                            {
                                "value": "822",
                                "newvalue": "CAIF media type"
                            },
                            {
                                "value": "823",
                                "newvalue": "GRE over IPv6"
                            },
                            {
                                "value": "824",
                                "newvalue": "Netlink header"
                            },
                            {
                                "value": "825",
                                "newvalue": "IPv6 over LoWPAN"
                            },
                            {
                                "value": "826",
                                "newvalue": "Vsock monitor header"
                            }
                        ]
                    },
                    {
                        "name": "zabbix.host.active_agent.available",
						"hostid": hostid,
                        "mappings": [
                            {
                                "value": "0",
                                "newvalue": "unknown"
                            },
                            {
                                "value": "1",
                                "newvalue": "available"
                            },
                            {
                                "value": "2",
                                "newvalue": "not available"
                            }
                        ]
                    },
                    {
                        "name": "Zabbix agent ping status",
						"hostid": hostid,
                        "mappings": [
                            {
                                "value": "1",
                                "newvalue": "Up"
                            }
                        ]
                    }
                ]


async def map_create():
    for data in vmaps:
        res = await api("valuemap.create",data)
        print(res)

asyncio.run(map_create())
