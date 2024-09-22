const app = require('http');

app.createServer((req, res) => {
  
  res.writeHead(200, { 'Content-Type' : 'text/html' });

  const url = req.url;

  if (url == '/') {
    res.write("Hello Holberton School");
    res.end()
  } else if (url == '/test') {
    res.write("Hello Holberton School");
    res.end();
  }
}).listen(1245);
module.exports = app;
