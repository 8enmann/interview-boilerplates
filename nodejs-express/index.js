const express = require('express')
const app = express();

app.use(express.json());

const port = process.env.port || 3000;

app.get('/hello', (req, res) => {
  res.json({'hello': 'world'});
})

app.post('/hello', (req, res) => {
  res.json(req.body);
})


const server = app.listen(port, () => {
  console.log('Listening on http://localhost:%s', port);
});
module.exports = server;
