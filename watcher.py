# cobbler mod_python handler for observing kickstart activity
# 
# Copyright 2007, Red Hat, Inc
# Michael DeHaan <mdehaan@redhat.com>
# 
# This software may be freely redistributed under the terms of the GNU
# general public license.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import time
from mod_python import apache

def outputfilter(filter):

    # open the logfile (directory be set writeable by installer)
    logfile = open("/var/log/cobbler/cobbler.log","a+")

    # write the timestamp
    logfile.write(str(time.asctime()))
    logfile.write("\t")

    # write the IP address of the client
    request = filter.req
    connection = request.connection
    (address,port) = connection.remote_addr
    logfile.write(address)
    logfile.write("\t")

    # write the filename being requested
    logfile.write(request.the_request)
    # logfile.write(request.filename)
    logfile.write("\n")

    # pass-through filter
    s = filter.read()
    while s:
        filter.write(s)
        s = filter.read()
    if s is None:
        filter.close()
    logfile.close()
