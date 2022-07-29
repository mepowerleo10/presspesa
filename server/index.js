const express = require("express");

const PORT = process.env.PORT || 5050;

const app = express();

app.get("/api", (request, response) => {
    response.json({message: "hi, client!"});
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});
