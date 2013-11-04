import BaseHTTPServer, shutil, os
from cStringIO import StringIO
class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    #The http path we service and the command we service
    cmds = {'/ping':'ping www.thinkware.se',
            '/netstat': 'netstat -a',
            '/tracert': 'tracert www.thinkware.se',
            '/srvstats': 'net statistics server',
            '/wsstats': 'net statistics workstation',
            '/route': 'route print',
            }

    def do_GET(self):
        """service a GET request"""
        f = self.send_head()
        if f:
            f = StringIO()
            machine = os.popen('hostname').readlines()[0]
            if self.path == '/':
                heading = "Select a command to run on %s" %(machine)
                body = ( self.getMenu() + "<p> The screen won't update until the selected" "command has finished. Please be patient.")
            else:
                heading = "Execution of ''%s'' on %s" %( self.cmds[self.path], machine)
                cmd = self.cmds[self.path]
                body = '<a href="/">Main Menu&lt;/a&gt;<pre>%s</pre>\n' %  os.popen(cmd).read()
                body = body.decode('cp437').encode('latin1')
            f.write("<html><head><title>%s</title></head>\n" %heading)
            f.write('<body><H1>%s</H1>\n' %(heading))
            f.write(body)
            f.write('</body></html>\n')
            f.seek(0)
            self.copyfile(f, self.wfile)
            f.close()

        return f

    def do_HEAD(self):
        """service a head request"""
        f = self.send_head()
        if f:
            f.close()

    def send_head(self):
        path = self.path
        if not path in ['/'] + self.cmds.keys():
            head = 'Command "%s" not found. Try one of three:<ul>' %path
            msg = head + self.getMenu()
            self.send_error(404, msg)
            return None
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()
        f = StringIO()
        f.write("A test %s \n" % self.path)
        f.seek(0)
        return f

    def getMenu(self):
        keys = self.cmds.keys()
        keys.sort()
        msg = []
        for k in keys:
            msg.append('<li><a href = "%s"> %s => %s&lt;/a&gt;</li>' %(k, k, self.cmds[k]))
        msg.append('</ul>')
        return "\n".join(msg)

    def copyfile(self, source, outputfile):
        shutil.copyfileobj(source, outputfile)

def main(HandleClass = MyHTTPRequestHandler, ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandleClass, ServerClass)

if __name__ == '__main__':
    main()