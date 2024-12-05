import http.server as h

class ecoHandler(h.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type' ,'html')
        self.end_headers()
        self.wfile.write("İstanbul'da sahte içkiden can kaybı 22'ye yükseldi. Faciada 24 kişinin tedavisi sürerken 10 şüphelinin tutuklandığı kaydedildi".encode())

def main():
    PORT=7000
    httpd=h.HTTPServer(('',PORT),ecoHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()





