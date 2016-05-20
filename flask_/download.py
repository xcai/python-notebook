
import os

from tornado.wsgi import WSGIContainer
from tornado.httpserver import  HTTPServer
from tornado.ioloop import IOLoop

from flask import Flask, request, make_response, send_file, send_from_directory, abort


app = Flask(__name__)
app.config['DOWNLOA_DIRECTORY'] = os.path.join(os.getenv('HOME'), 'download_path')


@app.route('/download/<filename>')
def downfile(filename):
    print filename
    path = os.path.join(app.config['DOWNLOA_DIRECTORY'], filename)
    print "path:  ", path
    if not os.path.isfile(path):
        abort(404)

    response = send_from_directory(directory=app.config['DOWNLOA_DIRECTORY'],
                                   filename=filename,
                                   as_attachment=True)
    response.headers['Content-Disposition'] = "attachment; filename=%s" % filename
    print response.headers
    return response


if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=9999, address='121.41.46.212')
    print "start server ...."
    IOLoop.instance().start()