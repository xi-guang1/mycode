from mitmproxy import http
from scapy.utils import wrpcap
from scapy.sendrecv import sniff

http.HTTPFlow("127.0.0.1","127.0.0.1")